import re

def extract_number(price_str):
    # Use regex to find all numeric parts in the string
    match = re.search(r'[\d,.]+', str(price_str))
    if match:
        # Replace commas with empty string and convert to float
        number_str = match.group()
        return float(number_str.replace(',', ''))
    return None

def printRatios(ratios):
    for elem in ratios:
        for e in elem:
            print(e,elem[e])
