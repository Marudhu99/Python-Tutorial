# String formating
price = 50
txt = "The pen price is {}"
txt = "The pen price is {:.2f}" # price.00
print(txt.format(price))

#multiple values
productName = "bat"
amount = 1000
print("I bough a {}. Price is : {:.2f}".format(productName,amount))
#using index
print("I bough a {0}. Price is : {1:.2f}".format(productName,amount))
#named index
print("I bough a {pName}. Price is : {balance}".format(pName="headphone",balance=2000))
