import dataExtracter
import ratiosCalculator
import CsvManager
import shouldInvest
import menu
import readMe

def FundInvesting():
    opt=0
    while opt!=3:
        opt = menu.menu()
        if(opt==1):
            try:
                ticker_symbol=input("Give me the name of the stock (e.g: Amazon -> AMZN)\n")
            except:
                print("The stock is not listed or bad typed")
            else:
                data = dataExtracter.get_data(ticker_symbol)
                try:
                    ratios = ratiosCalculator.calculate_and_classify_ratios(data)
                except:
                    print("Couldn't do the ratios")
                else:
                    CsvManager.toCsv(ticker_symbol+".csv",data,ratios)
                    shouldInvest.shouldInvest(ratios)
        if(opt==2):
            readMe.readMe()
    print("BYE BYE")

    




