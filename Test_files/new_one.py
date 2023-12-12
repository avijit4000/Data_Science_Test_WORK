price=[5,6,10,11,10,9,7,20,21,18,16,10]
#
# n=len(l)
# profit=0
# max_profit=0
#
# for i in range(n):
#     for j in range(i+1,n):
#         if l[j]>l[i]:
#             l[j]-l[i]>profit
#             profit=l[j]-l[i]
#             print(profit)

buy_lists=[]           # creating buy
sell_lists=[]          # creating selling
def stock(price,n):     # creaging function
    if (n==1):           #checking number of values inside the list atlist two
        return
    i=0                  #initializing i value
    while (i<(n-1)):
        while ((i<n-1) and (price[i+1]<=price[i])):  #checking the decreasing values
            i+=1
        if (i==n-1):     #checking the last value
            break
        buy=i            #buying value
        i+=1
        while((i<n) and (price[i]>=price[i-1])):   #checking the increasing value
            i+=1
            sell=i-1                    # selling value
            print("Buy on day:",buy, "\t",   ##printing the buying and selling value
               "sell on day: ", sell)
            buy_lists.append(buy)     #collecting buying vaues inside the buying list
            sell_lists.append(sell)   #collecting selling vaues inside the selling list
n = len(price)                    #finding number of values inside the price list
stock(price, n)