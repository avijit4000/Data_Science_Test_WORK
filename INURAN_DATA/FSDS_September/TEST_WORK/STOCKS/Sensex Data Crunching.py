import pandas as pd              # importiing library
df=pd.read_csv("BSE Sensex Daily Close Jan1990 Oct2020.csv")  # imprting given dataset
price=[]                         # given dataset Closing price converting inside list
for i in df['Close']:
    price.append(int(i))                                      # all closing price transfering inside price
b=[]                             # makeing lists of buying index
s=[]                             # Making lists of selling index
def STOCKS(price, n):            # finding out BUYING DAY SELLING DAY AND NEUTRAL DAY
    profit = 0                   # initializing profit value
    if (n == 1):                 # checking number of values inside the list atlist two
        return
    i = 0                        # initializing i value
    while (i < (n - 1)):
        while ((i < (n - 1)) and (price[i + 1] <= price[i])):  # checking the decreasing values
            i += 1
        if (i == n - 1):         # checking the last value
            break
        buy = i                  # buying value
        i += 1
        while ((i < n) and (price[i] >= price[i - 1])):        # checking the increasing value
            i += 1
        sell = i - 1              # selling value
        profit += sell - buy      # difference added to 'profit'
        b.append(buy)             # collecting buying vaues inside the buying list
        s.append(sell)            # collecting selling vaues inside the selling list
    print('Total profit is ≈',profit)                          # printing the total profit
n = len(price)                     # finding number of values inside the price list
STOCKS(price, n)
li=[]                              # Creating lists of Buying, Selling and neutral
for i in range(len(price)):        # Creating loop of BUY(B),SELL(S) AND NEUTRAL(N)
    if i in b:
        li.append('B')
    elif i in s:
        li.append('S')
    else:
        li.append('N')
print(li)         # VISUALISING the list of BUY(B), SELL(S), NEUTRAL(N)


### This code is contributed by AVIJIT BISWAS