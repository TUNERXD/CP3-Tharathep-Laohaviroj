menuList = []
priceList = []

def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number],(priceList[number]))

def totalPrice():
    print("----- Total Price -----")
    total = 0
    for price in range(len(menuList)):
        total += int(priceList[price])
    print(total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
totalPrice()