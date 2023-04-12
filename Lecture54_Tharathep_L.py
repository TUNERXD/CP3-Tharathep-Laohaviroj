def login():
    print("----- Login -----")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    print("-----------------")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Username Or Password incorrect")
        return login()

def showMenu():
    print("------ iShop ------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("-------------------")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()

def vatCalculator():
    print("-----Vat Calculator-----")
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    vat = 7
    print("Vat = ", vat,"%")
    result = totalPrice + (totalPrice * vat / 100)
    print("Total Price + vat(7%): ", result)

def priceCalculator():
    print("----- Price Calculator -----")
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice = price1 + price2
    print("Total Price: ",totalPrice)


login()