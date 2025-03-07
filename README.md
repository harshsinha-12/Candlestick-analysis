Candlestick Chart Analyzer with AI

A simple Streamlit application that downloads stock price data from yfinance and uses Google Generative AI (Gemini) to identify candlestick patterns. The app displays an interactive candlestick chart and provides a brief AI-generated analysis of the most recent candlestick.

Table of Contents
	•	Features
	•	How It Works
	•	Installation & Setup
	•	Usage
	•	Code Explanation
	•	Dependencies
	•	References
	•	License



Features

	1.	Live Stock Data
Fetch real-time or recent historical data for any ticker symbol (e.g., AAPL, TSLA, TATAMOTORS.NS) from Yahoo Finance.

	2.	Candlestick Chart
Display a fully interactive Plotly candlestick chart within Streamlit.

	3.	AI Candlestick Analysis

	•	Automatically generate a text-based explanation of the most recent candlestick pattern using Google’s Gemini model.

	•	Identifies potential bullish/bearish signals and any significance of the pattern.


	4.	Ease of Use

	•	Single-page Streamlit app.
	•	Minimal user input: just the ticker, timeframe, and interval.


How It Works
	1.	User Input
The user types in a ticker symbol, selects a timeframe (e.g., 1d, 5d, 1mo, etc.) and an interval (1m, 5m, 15m, etc.).
	2.	Fetch Data
The app calls yfinance.download(...), returning stock data in a Pandas DataFrame. Columns often include Open, High, Low, Close, Volume.
	3.	Rename Columns
Some tickers return columns with suffixes (e.g., Open_AAPL). The code detects and strips these suffixes so they become Open, High, Low, etc.
	4.	Plot Candlestick
Using Plotly, the code plots the DataFrame in candlestick format and displays it in the Streamlit interface.
	5.	AI Pattern Analysis
	•	The final row (the latest candlestick) is extracted.
	•	That data is passed to the Google Gemini API using the google.generativeai client.
	•	The response is parsed and displayed in Streamlit as a pattern name, brief explanation, and any bullish/bearish implications.

⸻

Installation & Setup
	1.	Clone or Download

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


	2.	Create a Virtual Environment (recommended)

python3 -m venv venv
source venv/bin/activate


	3.	Install Requirements

pip install -r requirements.txt

Make sure your requirements.txt contains:

streamlit
yfinance
pandas
plotly
google-generativeai


	4.	Set Your Google Generative AI Key
	•	Obtain a valid API key from Google Cloud (Gemini).
	•	Replace GEMINI_API_KEY in candlestick.py (or wherever you store your key) with your own.

⸻

Usage
	1.	Run the Streamlit App
From the project folder, run:

streamlit run candlestick.py


	2.	Open the App in Your Browser
Streamlit typically launches at http://localhost:8501.
	3.	Enter Your Preferences
	•	Ticker: A valid stock symbol (e.g., AAPL, TSLA, TATAMOTORS.NS).
	•	Timeframe: How far back you’d like data (1d, 5d, 1mo, 3mo, 6mo, 1y).
	•	Interval: Granularity (1m, 5m, 15m, 30m, 1h, 1d).
	4.	Press “Fetch & Analyze Data”
	•	The app downloads the historical data, flattens the columns, plots a candlestick chart, and queries the AI for pattern analysis.
	•	A short pattern description is displayed below the chart.

⸻

Code Explanation

fetch_data(ticker, period, interval)
	•	Uses yfinance.download() to fetch historical market data for the specified ticker, timeframe, and interval.
	•	Resets the DataFrame index so Date/Datetime is a standard column.
	•	Handles potential multi-level columns and renames columns with _AAPL, _TSLA, etc. suffixes to the base (Open, High, etc.).
	•	Ensures there is a "Datetime" column for plotting.

identify_candlestick_pattern(open_price, high_price, low_price, close_price)
	•	Constructs a prompt string describing the candlestick data.
	•	Calls the Gemini / LLM via google.generativeai.
	•	Returns the AI-generated response (candlestick pattern name, whether it’s bullish or bearish, etc.).

Streamlit UI
	•	Inputs: Ticker, Timeframe, Interval.
	•	Button: “Fetch & Analyze Data.”
	•	Outputs:
	1.	A Plotly candlestick chart.
	2.	AI-provided analysis of the last candlestick.

⸻

Dependencies
	1.	Streamlit
Used to build the interactive web UI in Python.
	2.	yfinance
Fetches historical stock market data from Yahoo Finance.
	3.	pandas
Data manipulation and analysis.
	4.	plotly
Interactive charting library used for the candlestick plot.
	5.	google-generativeai
Python client for accessing Gemini.

⸻

References
	•	yfinance: GitHub Docs
	•	Google Generative AI (Gemini): Official Docs
	•	Plotly: Candlestick Charts
	•	Streamlit: Documentation

⸻