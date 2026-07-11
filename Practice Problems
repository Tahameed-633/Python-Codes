stock=[]
d=int(input("Enter the duration of the stock market:"))
print("Enter the price of the stock:")
for i in range(d):
    price=int(input())
    stock.append(price)
max_profit=0
min_price=stock[0]
for i in range(1,d):
    if(stock[i]<min_price):
        min_price=stock[i]
    else:
         current_profit=stock[i]-min_price
         if(current_profit>max_profit):max_profit=current_profit
print("Max profit=",max_profit)