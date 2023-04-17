menuList = []

def showBill():
    print("----- My Food -----")
    for number in range(len(menuList)):
        print(menuList[number][0],(menuList[number][1]))

def totalPrice():
    print("----- Total Price -----")
    total = 0
    for price in range(len(menuList)):
        total += int(menuList[price][1])
    print(total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])

showBill()
totalPrice()