print("Tuner Shop")
print("----------Register----------")
User = input("Username: ")
Pass = input("Password: ")

print("Your account has been registered")

print("----------Login----------")
username = input("Username: ")
password = input("Password: ")
if username == User and password == Pass:
    print("Login successful!")
    print("Welcome to Tuner Shop!")
    print("----------Catalog----------")
    print("1.Headphones:          3,000 THB")
    print("2.Mouse:               2,000 THB")
    print("3.Wireless_Mouse:      2,200 THB")
    print("4.Keyboard:              200 THB")
    print("5.Mechanical_Keyboard: 2,500 THB")
    print("------------------------------")
    item = int(input("item number: "))
    Headphones = 3000
    Mouse = 2000
    Wireless_Mouse = 2200
    Keyboard = 200
    Mechanical_Keyboard = 2500

    if item == 1:
        pieces = int(input("How many pieces: "))
        x = pieces
        result1 = Headphones * x
        print("Headphones", str(x), "piece(s):", result1, "THB")
        print("------------------------------")
        print("Thank you for purchasing :>")
        print("see you next time!")
    elif item == 2:
        pieces = int(input("How many pieces: "))
        x = pieces
        result2 = Mouse * x
        print("Mouse", str(x), "piece(s):", result2, "THB")
        print("------------------------------")
        print("Thank you for purchasing :>")
        print("see you next time!")
    elif item == 3:
        pieces = int(input("How many pieces: "))
        x = pieces
        result3 = Wireless_Mouse * x
        print("Wireless_Mouse", str(x), "piece(s):", result3, "THB")
        print("------------------------------")
        print("Thank you for purchasing :>")
        print("see you next time!")
    elif item == 4:
        pieces = int(input("How many pieces: "))
        x = pieces
        result4 = Keyboard * x
        print("Keyboard", str(x), "piece(s):", result4, "THB")
        print("------------------------------")
        print("Thank you for purchasing :>")
        print("see you next time!")
    elif item == 5:
        pieces = int(input("How many pieces: "))
        x = pieces
        result5 = Mechanical_Keyboard * x
        print("Keyboard", str(x), "piece(s):", result5, "THB")
        print("------------------------------")
        print("Thank you for purchasing :>")
        print("see you next time!")
    else:
        print("no item labeled number", item, "!")
    print("------------------------------")
else: print("Invalid Username or Password")