items = {1: 'Bread', 2: 'Rice', 3: 'Soap', 4: 'Sugar', 5: 'Tea', 6: 'Snacks', 7: 'Milk', 8: 'Eggs', 9: 'Oil', 10: 'Flour'}

prices = {1: 120, 2: 80, 3: 50, 4: 100, 5: 150, 6: 30, 7: 90, 8: 100, 9: 900, 10: 70}

quantity = {1: 42, 2: 60, 3: 100, 4: 55, 5: 90, 6: 15, 7: 36, 8: 80, 9: 50, 10: 5}

def owner_opt():
    print("1. See Items  2. Add any Item  3. Edit Prices  4. Increase/Decrease Stock")
    return



def item_list():
    print(items.values())

def cashier():
    print("Want to login as a cashier?")
    signin = input("(1) Yes (2) No\n")
    if signin == "1":
        for i in range(3):
            Username = input("Enter Username: ")
            password = input("Enter Password: ")
            if Username == "pari@gmail.com" and password == "7654":
                print("\nProcessing data.....")
                print("**** CASHIER VERIFIED ****")
                print("View items and prices list")
               
                print("Cashier's profile activated")
                print("HAVE A NICE EXPERIENCE")
                break
            else:
                print("INCORRECT USERNAME OR PASSWORD")
    return

def calculation():
    for i in range(4):
        i = input("Enter Item No: ")
        if i.isdigit() and int(i) in items:
            q = int(input("Enter Quantity: "))
            item_no = int(i)
            price = prices[item_no]
            total = price * q
            print("GROCERY STORE")
            print(f"{items[item_no]}: {price}")
            print("Total:", total)
            print("Bill is Checked by Cashier\n")
            print("** THANK YOU FOR SHOPPING WITH US **")
        else:
            print("Invalid Item Number")
    return

print("**********************************************")
print("WELCOME TO GROCERY STORE")
print("SELECT ")
print("1. OWNER  2. CASHIER  3. CUSTOMER")

login = input("Enter number: ")

if login == "1":
    name = input("Enter Name: ")
    vcode = input("Enter password: ")
    if name == "Sweety" and vcode == "09113":
        print("Verification succeeded")
        print("This store is on your command Owner")
        print("You can manage items here")
        print("SELECT")
        print("1. See Items  2. Add any Item  3. Edit Prices  4. Increase/Decrease Stock")
        entr = input("Enter number: ")
        if entr == "1":
            item_list()
        elif entr == "2":
            add1 = input("Want to add any item? (1. Yes / 2. No): ")
            if add1 == "1":
                add_item_no = max(items.keys()) + 1
                add_name = input("Enter item name: ")
                add_price = int(input("Add price of item: "))
                items[add_item_no] = add_name
                prices[add_item_no] = add_price
                quantity[add_item_no] = 0
                print(items)
                print(prices)
                print(quantity)
        elif entr == "3":
            ri = input("Do you want to remove the item? (Yes/No): ")
            if ri.lower() == "yes":
                item_list()
                r = int(input("Enter item number to remove: "))
                if r in items:
                    del items[r]
                    del prices[r]
                    del quantity[r]
                    print("Item removed. Changes saved.")
                else:
                    print("Invalid item number.")
        elif entr == "4":
            inc = input("Do you want to change the quantity of items? (Yes/No): ")
            if inc.lower() == "yes":
                item_list()
                q = int(input("Enter item no.: "))
                if q in quantity:
                    qq = int(input("Enter new quantity: "))
                    quantity[q] = qq
                    print("Quantity changed")
                    print(quantity)
                else:
                    print("Invalid item number.")
            else:
                print("System Closed")
        else:
            print("Invalid selection. Thank You.")
    else:
        print("Verification failed. Thank You.")

elif login == "2":
    cashier()

elif login == "3":
    print("Welcome to Grocery Store Customer Service App")
    logcus = input("Which type of Service you Want\n(1) CREATE ACCOUNT\n(2) LOGIN\n")
    if logcus == "1":
        name = input("Enter your name: ")
        ph_no = input("Enter your phone number: ")
        print("A verification code sent to you on this phone number, please wait....")
        print("Code=8753")
        pin = int(input("Enter verification code: "))
        if pin == 8753:
            print("Processing Data ......")
            print("*****VERIFIED*****")
            
            calculation()
        else:
            print("Invalid password")
    elif logcus == "2":
        name = input("Enter name: ")
        password = input("Enter password: ")
        print("Account Accessed")
        search = input("Search Item: ")
        print("\nDO YOU WANT TO BUY SOMETHING?")
        buy = input("1. YES  2. NO\n")
        if buy == "1":
            
            calculation()
        else:
            print("...Thank You...")
else:
    print("Invalid login selection.")
