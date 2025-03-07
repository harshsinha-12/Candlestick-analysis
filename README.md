# Candlestick Chart Analyzer with AI

A simple Streamlit application that fetches stock price data from Yahoo Finance and uses Google Generative AI (Gemini) to identify candlestick patterns. The app displays an interactive candlestick chart and provides AI-generated insights on the most recent candlestick.

## Features
- **Live Stock Data**: Fetch real-time or historical data for any stock ticker.
- **Candlestick Chart**: Interactive Plotly candlestick visualization.
- **AI Candlestick Analysis**:
  - Identifies candlestick patterns using Google's Gemini model.
  - Determines whether the pattern is bullish, bearish, or neutral.
- **Easy to Use**: Minimal user input required—just select a stock ticker, timeframe, and interval.

## How It Works
1. **User Input**: Enter a stock ticker, timeframe (e.g., 1d, 5d, 1mo), and interval (e.g., 1m, 5m, 1d).
2. **Fetch Data**: The app retrieves stock data using `yfinance` and processes it into a Pandas DataFrame.
3. **Plot Candlestick Chart**: Displays the stock’s candlestick chart using Plotly.
4. **AI Analysis**:
   - Extracts the latest candlestick data.
   - Queries Google Gemini AI for pattern identification.
   - Displays the AI's interpretation of the pattern.

## Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/harshsinha-12/Candlestick-analysis.git
   cd Candlestick-analysis
   ```

2. **Create a Virtual Environment (Recommended)**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Your API Key**
   - Obtain an API key from Google Cloud for Gemini.
   - Store it securely in `secrets.toml` (for Streamlit Cloud) or set it in your environment variables.

## Usage
1. **Run the App**
   ```sh
   streamlit run candlestick.py
   ```
2. **Open the App in Browser**: Typically runs at `http://localhost:8501`
3. **Enter Your Inputs**: Ticker symbol, timeframe, and interval.
4. **Fetch & Analyze Data**: The app will display the candlestick chart and AI-generated pattern analysis.

## Dependencies
- `streamlit` - Web-based UI framework.
- `yfinance` - Fetches stock market data.
- `pandas` - Data processing and analysis.
- `plotly` - Creates interactive candlestick charts.
- `google-generativeai` - Integrates with Google Gemini AI.

## References
- [Yahoo Finance API (yfinance)](https://github.com/ranaroussi/yfinance)
- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Candlestick Charts](https://plotly.com/python/candlestick-charts/)

