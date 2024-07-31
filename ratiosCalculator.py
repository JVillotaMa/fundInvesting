def classify_ratio(ratio, good, medium, bad):
    if good is not None and ratio > good:
        return 'Good'
    elif medium is not None and ratio > medium:
        return 'Medium'
    else:
        return 'Bad'

def calculate_and_classify_ratios(data):
    ratios = {}
    classifications = {}

    # Current Ratio
    ratios['Current Ratio'] = data['Balance Sheet']['Current Assets'] / data['Balance Sheet']['Current Liabilities'] if data['Balance Sheet']['Current Liabilities'] else None
    classifications['Current Ratio'] = classify_ratio(ratios['Current Ratio'], 1.5, 1, None)

    try:
        # Quick Ratio
        ratios['Quick Ratio'] = (data['Balance Sheet']['Current Assets'] - data['Balance Sheet']['Inventory']) / data['Balance Sheet']['Current Liabilities'] if data['Balance Sheet']['Current Liabilities'] else None
    except:
        ratios['Quick Ratio']=0.5
    finally:
        classifications['Quick Ratio'] = classify_ratio(ratios['Quick Ratio'], 1, 0.5, None)
    

    # Gross Margin
    ratios['Gross Margin'] = ((data['Financials']['Total Revenue'] - data['Financials']['Reconciled Cost Of Revenue']) / data['Financials']['Total Revenue']) * 100 if data['Financials']['Total Revenue'] else None
    classifications['Gross Margin'] = classify_ratio(ratios['Gross Margin'], 40, 20, None)

    # Operating Margin
    ratios['Operating Margin'] = (data['Financials']['Operating Income'] / data['Financials']['Total Revenue']) * 100 if data['Financials']['Total Revenue'] else None
    classifications['Operating Margin'] = classify_ratio(ratios['Operating Margin'], 15, 10, None)

    # Net Profit Margin
    ratios['Net Profit Margin'] = (data['Financials']['Net Income'] / data['Financials']['Total Revenue']) * 100 if data['Financials']['Total Revenue'] else None
    classifications['Net Profit Margin'] = classify_ratio(ratios['Net Profit Margin'], 10, 5, None)

    # Return on Assets (ROA)
    ratios['Return on Assets (ROA)'] = (data['Financials']['Net Income'] / data['Balance Sheet']['Total Assets']) * 100 if data['Balance Sheet']['Total Assets'] else None
    classifications['Return on Assets (ROA)'] = classify_ratio(ratios['Return on Assets (ROA)'], 5, 2, None)

    # Return on Equity (ROE)
    ratios['Return on Equity (ROE)'] = (data['Financials']['Net Income'] / data['Balance Sheet']['Total Equity Gross Minority Interest']) * 100 if data['Balance Sheet']['Total Equity Gross Minority Interest'] else None
    classifications['Return on Equity (ROE)'] = classify_ratio(ratios['Return on Equity (ROE)'], 15, 10, None)

    # Debt to Equity Ratio
    ratios['Debt to Equity Ratio'] = data['Balance Sheet']['Total Debt'] / data['Balance Sheet']['Total Equity Gross Minority Interest'] if data['Balance Sheet']['Total Equity Gross Minority Interest'] else None
    classifications['Debt to Equity Ratio'] = classify_ratio(ratios['Debt to Equity Ratio'], 1, 2, None)

    # Interest Coverage Ratio
    ratios['Interest Coverage Ratio'] = data['Financials']['EBIT'] / data['Financials']['Interest Expense'] if data['Financials']['Interest Expense'] else None
    classifications['Interest Coverage Ratio'] = classify_ratio(ratios['Interest Coverage Ratio'], 5, 2, None)

    try:
        # Inventory Turnover
        ratios['Inventory Turnover'] = data['Financials']['Reconciled Cost Of Revenue'] / data['Balance Sheet']['Inventory'] if data['Balance Sheet']['Inventory'] else None
    except: 
        ratios['Inventory Turnover'] = 3
    finally:
        classifications['Inventory Turnover'] = classify_ratio(ratios['Inventory Turnover'], 5, 3, None)

    # Asset Turnover
    ratios['Asset Turnover'] = data['Financials']['Total Revenue'] / data['Balance Sheet']['Total Assets'] if data['Balance Sheet']['Total Assets'] else None
    classifications['Asset Turnover'] = classify_ratio(ratios['Asset Turnover'], 1, 0.5, None)

    # P/E Ratio
    ratios['P/E Ratio'] = data['Share price'] / (data['Financials']['Net Income'] / data['Balance Sheet']['Ordinary Shares Number']) if data['Balance Sheet']['Ordinary Shares Number'] else None
    classifications['P/E Ratio'] = classify_ratio(ratios['P/E Ratio'], 20, 10, None) if ratios['P/E Ratio'] is not None else None

    # P/B Ratio
    ratios['P/B Ratio'] = data['Share price'] / (data['Balance Sheet']['Total Equity Gross Minority Interest'] / data['Balance Sheet']['Ordinary Shares Number']) if data['Balance Sheet']['Ordinary Shares Number'] else None
    classifications['P/B Ratio'] = classify_ratio(ratios['P/B Ratio'], 3, 1, None) if ratios['P/B Ratio'] is not None else None

    # Dividend Yield
    try:
        dividends_per_share = (data["Cash Flow"]["Cash Dividends Paid"]*-1)/data["Financials"]["Basic Average Shares"]  # Replace with actual value if available 
    except:
        ratios['Dividend Yield'] = 3
    finally:
        classifications['Dividend Yield'] = classify_ratio(ratios['Dividend Yield'], 3, 1, None)
    return ratios, classifications
