import yfinance as yf
import pandas as pd
import Utilities

def get_data(ticker_symbol):
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)
    
    # Fetch historical market data
    history = ticker.history(period="1y")
    
    # Get the latest price (close price)
    latest_price = Utilities.extract_number(history['Close'].iloc[-1] if not history.empty else None)
    
    # Fetch financial statements (Income Statement, Balance Sheet, Cash Flow)
    financials = ticker.financials
    balance_sheet = ticker.balance_sheet
    cashflow = ticker.cashflow
    
    # Initialize dictionaries to hold the latest values
    financials_latest = {}
    balance_sheet_latest = {}
    cashflow_latest = {}
    
    # Process financials
    if not financials.empty:
        # Extract the most recent data from financials
        for metric in financials.index:
            financials_latest[metric] = financials.loc[metric].iloc[-2] if not financials.loc[metric].empty else None
    
    # Process balance sheet
    if not balance_sheet.empty:
        # Extract the most recent data from balance sheet
        for metric in balance_sheet.index:
            balance_sheet_latest[metric] = balance_sheet.loc[metric].iloc[-2] if not balance_sheet.loc[metric].empty else None
    
    # Process cash flow
    if not cashflow.empty:
        # Extract the most recent data from cash flow
        for metric in cashflow.index:
            cashflow_latest[metric] = cashflow.loc[metric].iloc[-2] if not cashflow.loc[metric].empty else None
    
    # Combine all data into a single dictionary
    combined_data = {
        'Share price': latest_price,
        'Financials': financials_latest,
        'Balance Sheet': balance_sheet_latest,
        'Cash Flow': cashflow_latest
    }
    
    return combined_data





