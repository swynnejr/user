# class User:
#     # pass    # we'll fill this in shortly

# michael = User()
# anna = User()

# # declare a class and give it name User
# class User:
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# User()
# guido = User()
# monty = User()
# # Accessing the instance's attributes
# # print(guido.name)	# output: Michael
# # print(monty.name)	# output: Michael

# guido.name = "Guido"
# print(guido.name) # output: Guido
# monty.name = "Monty"
# print(monty.name) # output: Monty

# class User:
# #   class attributes get defined in the class
#     bank_name = "First National Dojo"
# #   now our method has 2 parameters!
#     def __init__(self, name, email_address):
#     	# we assign them accordingly
#         self.name = name
#         self.email = email_address
#     	# the account balance is set to $0
#         self.account_balance = 0
# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawl(self, amount): # takes an argument that is the amount of the withdrawl
        self.account_balance -= amount # the specific user's account decreases by the amount of the value withdrawn
    def display_user_balance(self): #  <<< This doesn't work
        print(self.name)
        print(self.account_balance)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

travis = User("Travis Douglass", "TDugzzz@HaloReach.com")
maddox = User("Maddox Womble", "MadFox420@WSMFP.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

#checking display user balance method that doesnt work, but I dont get why it needs to be made when the above works fine...

# monty.display_user_balance # <<<< Doesnt do what its supposed to
