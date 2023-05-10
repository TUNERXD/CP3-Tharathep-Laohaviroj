class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Tharathep"
customer1.lastName = "Laohaviroj"
customer1.age = 17

customer2 = Customer()
customer2.name = "Anwar"
customer2.lastName = "Jibawi"
customer2.age = 31

customer3 = Customer()
customer3.name = "Adam"
customer3.lastName = "W"
customer3.age = 30

customer4 = Customer()
customer4.name = "Rudy"
customer4.lastName = "Mancuso"
customer4.age = 31

customer5 = Customer()
customer5.name = "Jordan"
customer5.lastName = "Peele"
customer5.age = 31

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()
customer5.addCart()