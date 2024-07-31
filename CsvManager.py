import csv


def toCsv(name,data,ratios):
    with open(name,'w+',newline='') as csvfile:
        writer = csv.writer(csvfile)
        extractData(data,writer)
        extractRatios(ratios,writer)
    csvfile.close()

def extractData(data,writer):
    writer.writerow(['DATA'])
    writer.writerow(['Share Price',data['Share price']])
    data.pop('Share price')
    for elemnt in data:
        for d in data[elemnt]:
            writer.writerow([d,data[elemnt][d]])
    
        

def extractRatios(ratios,writer):  
    writer.writerow(['RATIOS']) 
    for elem in ratios[0]:
        writer.writerow([elem,ratios[0][elem],ratios[1][elem]])