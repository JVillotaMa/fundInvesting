def readMe():
    print("PROJECT DESCRIPTION")

    print("INTRODUCTION")

    print("FundInvesting is a program that evaluates the fundamentals of the company that you want in the stock market. This helps you to invest in a safer mode.")
    print("The program is designed to use the API of Yahoo Finances.") 
    print("The software expects a stock ticker symbol (like AMZN if you search for Amazon) in other case, the software will fail.")

    print("As the output you should expect the results of the indicators used in our model and the result of our model.")

    print("MODEL DESCRIPTION")

    print("This model uses multipliers as the primary indicator for the company valuation. Be aware that this model should be taken in a secondary place in the company valuation. The") 
    print("mutlipliers shouldn't replace other fundamental analysis or other models that are more sotisficated.")


    print("This models uses different multipliers divided in different categories:")

    print("    Profitability : Net Profit Margin , Operating Margin , Gross Margin")
    print("    Efficiency : Return on Assets (ROA) , Return on Equity (ROE) , Asset Turnover , Inventory Turnover")
    print("    Liquidity : Current Ratio , Quick Ratio")
    print("    Leverage : Debt to Equity Ratio , Interest Coverage Ratio")
    print("    Market Valuation : P/E Ratio , P/B Ratio , Dividend Yield")
        
        
    print("The different categories have within a weight for the final calculation:")
        
    print("    Profitability: 0.4")
    print("    Efficiency: 0.3")
    print("    Liquidity': 0.15")
    print("    Leverage : 0.1")
    print("    Market Valuation : 0.05")
        
    print("SCORE = sum(category_weight * ratio)")

    print("RESULT -> MAX RATIO * 0,7 <= SCORE ")

    print("0.7 is a limit. All the companies that their score are below of that mark are no good companies to invest in (Using this model).")


    print("SOFTWARE PROCESS")

    print("1. Data Collection using Yahoo API")

    print("2. Identify and sort reliable sources of financial data.")

    print("3. Extract key figures from the income statement, balance sheet, and cash flow statement.")

    print("4. Calculate Financial Ratios")

    print("5. Valuation and result")