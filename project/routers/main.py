import csv 

def result(data):
    price=0.0
    with open('../lm_parameters.csv') as file:
        reader = csv.reader(file)
        thata0=0
        u=0
        for row in reader:
            if u==0:
                thatas=row
            elif u==1:
                thata0=row
            u=u+1
        price = 0.0
        x=data
        thatas=[float(thatas) for thatas in thatas]
        for indx,feature in enumerate(x):

            price += feature * thatas[indx]
        price
        price +=float(thata0[0])
        
    return str(price)

