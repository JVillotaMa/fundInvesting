def shouldInvest(data):
    weights = {
        'Profitability': 0.4,
        'Efficiency': 0.3,
        'Liquidity': 0.15,
        'Leverage': 0.1,
        'Market Valuation': 0.05
    }
    categories = {
        'Profitability': ['Net Profit Margin', 'Operating Margin', 'Gross Margin'],
        'Efficiency': ['Return on Assets (ROA)', 'Return on Equity (ROE)', 'Asset Turnover', 'Inventory Turnover'],
        'Liquidity': ['Current Ratio', 'Quick Ratio'],
        'Leverage': ['Debt to Equity Ratio', 'Interest Coverage Ratio'],
        'Market Valuation': ['P/E Ratio', 'P/B Ratio', 'Dividend Yield']
    }
    classification_scores = {
        'Good': 3,
        'Medium': 2,
        'Bad': 1,
        'N/A': 0
    }
    total_score = 0
    for category, ratios in categories.items():
        category_score = 0
        for ratio in ratios:
            classification = data[1][ratio]
            category_score += classification_scores[classification]
        weighted_score = category_score * weights[category]
        total_score += weighted_score
     
    max_possible_score = sum([len(ratios) * 3 * weights[category] for category, ratios in categories.items()])
    print("Max possible score",max_possible_score,"Total score",total_score)
    if(max_possible_score*0.7 <= total_score):
        print("You should invest, the company is in good position financially")
    else:
        print("Shouldn't invest")
   
    print("The company has a mark of: "+"{:.2f}".format((total_score*10)/max_possible_score)+" out of 10 \n ")
    print("The csv is ready in software's folder")