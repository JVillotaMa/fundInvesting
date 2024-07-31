# fundInvesting

PROJECT DESCRIPTION

INTRODUCTION

FundInvesting is a program that evaluates the fundamentals of the company that you want in the stock market. This helps you to invest in a safer mode.
The program is designed to use the API of Yahoo Finances. 
The software expects a stock ticker symbol (like AMZN if you search for Amazon) in other case, the software will fail.

As the output you should expect the results of the indicators used in our model and the result of our model.

MODEL DESCRIPTION

This model uses multipliers as the primary indicator for the company valuation. Be aware that this model should be taken in a secondary place in the company valuation. The 
mutlipliers shouldn't replace other fundamental analysis or other models that are more sotisficated.


This models uses different multipliers divided in different categories:

	Profitability : Net Profit Margin , Operating Margin , Gross Margin
    Efficiency : Return on Assets (ROA) , Return on Equity (ROE) , Asset Turnover , Inventory Turnover
    Liquidity : Current Ratio , Quick Ratio
    Leverage : Debt to Equity Ratio , Interest Coverage Ratio
    Market Valuation : P/E Ratio , P/B Ratio , Dividend Yield
	
	
The different categories have within a weight for the final calculation:
	
    Profitability: 0.4
    Efficiency: 0.3
    Liquidity': 0.15
    Leverage : 0.1
    Market Valuation : 0.05
    
SCORE = sum(category_weight * ratio)

RESULT -> MAX RATIO * 0,7 <= SCORE 

0.7 is a limit. All the companies that their score are below of that mark are no good companies to invest in (Using this model).


SOFTWARE PROCESS

1. Data Collection using Yahoo API

2. Identify and sort reliable sources of financial data.

3. Extract key figures from the income statement, balance sheet, and cash flow statement.

4. Calculate Financial Ratios

5. Valuation and result
