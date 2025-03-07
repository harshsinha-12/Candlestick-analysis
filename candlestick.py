import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import google.generativeai as genai

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

def fetch_data(ticker, period, interval):
    df = yf.download(
        tickers=ticker,
        period=period,
        interval=interval,
        actions=False,
        threads=True,
        progress=True
    )
    if df is None or df.empty:
        return df
    df.reset_index(inplace=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ["_".join(tuple(filter(None, col))).strip() for col in df.columns]
    for col in df.columns:
        if "_" in col:
            base, suffix = col.rsplit("_", 1)
            if suffix.upper() == ticker.upper():
                df.rename(columns={col: base}, inplace=True)
    if "Date" in df.columns:
        df.rename(columns={"Date": "Datetime"}, inplace=True)
    elif "Datetime" not in df.columns:
        df.rename(columns={df.columns[0]: "Datetime"}, inplace=True)
    return df

def identify_candlestick_pattern(open_price, high_price, low_price, close_price):
    """Call Gemini model to identify candlestick pattern."""
    prompt = f"""
    Given the following candlestick data:
    - Open: {open_price}
    - High: {high_price}
    - Low: {low_price}
    - Close: {close_price}
    Identify the candlestick pattern and its significance. Provide a brief explanation. How it impacts, is it bearish or bullish signal etc.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Pattern could not be identified."
st.title("📈 Candlestick Chart Analyzer with AI")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, TATAMOTORS.NS etc)", "AAPL")
timeframe = st.selectbox("Select Timeframe", ["1d", "5d", "1mo", "3mo", "6mo", "1y"])
interval = st.selectbox("Select Interval", ["1m", "5m", "15m", "30m", "1h", "1d"])

if st.button("Fetch & Analyze Data"):
    with st.spinner("Fetching data..."):
        df = fetch_data(ticker, timeframe, interval)
    if df is None or df.empty:
        st.error("No data found for the given ticker and timeframe.")
    else:
        st.success(f"Fetched {len(df)} rows of data for {ticker}.")
        df["Datetime"] = pd.to_datetime(df["Datetime"])
        st.write("Columns in df:", df.columns.tolist())
        fig = go.Figure(data=[go.Candlestick(
            x=df["Datetime"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Candlestick"
        )])
        fig.update_layout(
            title=f"{ticker} Candlestick Chart",
            xaxis_title="Date",
            yaxis_title="Price"
        )
        st.plotly_chart(fig)
        last_candle = df.iloc[-1]
        pattern = identify_candlestick_pattern(
            last_candle["Open"],
            last_candle["High"],
            last_candle["Low"],
            last_candle["Close"]
        )
        st.subheader("📊 AI Candlestick Analysis")
        st.write(f"**Timestamp:** {last_candle['Datetime']}")
        st.write(f"**Identified Pattern:** {pattern}")
