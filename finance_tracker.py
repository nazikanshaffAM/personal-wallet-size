#import json module
import json

#import tkinter
import tkinter as tk
from tkinter import ttk #ttk module


#function for addding transactions
def add_transaction():
    '''This block will add transactions'''
    while True: #to keep the amount in float and avoid strings
        try:
            amount = float(input(" Enter The Amount : "))
            break
        except ValueError:
            print("- The Entered Amount is not Valid! -")

    category = str(input(" Enter The Amount Category : "))
    while category.isnumeric(): #to avoid numeric values
        print("Category- Related to the entered amount above,Ex:- Salary,Medical Expense,Groceries ect...")
        category = str(input(" Enter The Amount Category : "))
                        
    #to get the details from the user to add those in the dictionary          
    category = category.capitalize()
    year = input("Enter the Year : ")
    month = input("Enter the month : ")
    day = input("Enter the day : ")
    date = (year+"_"+month+"_"+day)
    if category in transactions:
        transactions[category].append({"amount":amount,"date":date})
    else:
        transactions [category] = [{"amount":amount,"date":date}]
        return



#function for showing transactions                                  
def view_transaction():
    '''This block will show transactions'''
    if not transactions:
        print("- You Have Not Added Anything to show -")
    else:
        print(transactions)
        return



#function for updating transaction
def update_transaction():
    '''This block will update transactions'''
    while True: #to keep the amount in float and avoid strings
        try:
            amount = float(input(" Enter The Amount That You Want To Update : "))
            break
        except ValueError:
            print("- The Entered Amount is not Valid! -")

    category = str(input(" Enter The Amount Category That You Want To Update : "))
    while category.isnumeric(): #to avoid numeric values
        print("Category- Related to the entered amount above,Ex:- Salary,Medical Expense,Groceries ect...")
        category = str(input(" Enter The Amount Category That You want to Update : "))
                       
    #to get the details from the user to update those in the dictionary           
    category = category.capitalize()
    year = input("Enter the Year : ")
    month = input("Enter the month : ")
    day = input("Enter the day : ")
    date = (year+"_"+month+"_"+day)
    list_values = [{"amount":amount,"date":date}]
    transactions [category] = list_values
    return        



#function for deleting transaction
def delete_transaction():
    '''This block will Delete transactions'''
    if not transactions:
        print("- You Have Not Added Anything to Delete - ")
    else:
        while True: #to make the user to type the correct key
            key = (input(" Enter The Category That You Want To Delete : "))
            key = key.capitalize()

            if key in transactions:
                del transactions[key]
                break
            else:
                print("- No Such Category found -")


      
#function for showing summary of transactions
def show_summary():
    '''This block will show transaction Summary'''
    if not transactions:
        print("- You Have Not Added Anything to Show Summary -")
    else:
        for category, category_transactions in transactions.items():
            total_amount = sum(transaction['amount'] for transaction in category_transactions)
            print(f"Category: {category}, Total Amount: {total_amount}, Number of Transactions: {len(category_transactions)}")


       
# function for reading file
def load_transactions():
    
    '''this block of code is used to load json file'''
    try:
        with open(f"{name}'s transactions.json","r")as file:
            return json.load(file)
    except FileNotFoundError:
        print("New transactions.")


          
# function for writing file
def save_transactions():
    
    '''this block of code is used to save the list to json'''
    
    with open(f"{name}'s transactions.json","w")as file:
        json.dump(transactions,file,indent=1)
        



# function for reading bulk file
def read_bulk_transactions(filename):
    '''this block of code is used to read bulk file'''
    transactions = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                category, amount, date = line.strip().split(',')
                add_transaction()
    except FileNotFoundError:
        print("File not found.")
    return transactions



# function for GUI
class PersonalFinanceTrackerGUI(tk.Tk):
    '''this block of code is used to create GUI'''
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Tracker") #title in GUI
        self.geometry("600x400") #Size of the GUI(Window)
        
        self.load_data()  # Load data from JSON file
        self.create_components()  # Create GUI widgets

    def load_data(self):
        try:
            with open(f"{name}'s transactions.json", "r") as file:
                self.transactions = json.load(file)
        except FileNotFoundError:
            self.transactions = {}
            print("No transactions found.")

    def create_components(self):
        '''this block of code is used to create columns, table, search bar and button'''
        self.transaction_tree = ttk.Treeview(self)
        self.transaction_tree["columns"] = ("Category", "Amount", "Date")
        self.transaction_tree.heading("Category", text="Category", command=lambda: self.sort_column("Category"))
        self.transaction_tree.heading("Amount", text="Amount", command=lambda: self.sort_column("Amount"))
        self.transaction_tree.heading("Date", text="Date", command=lambda: self.sort_column("Date"))
        self.transaction_tree.pack(expand=True, fill=tk.BOTH)

        search_label = tk.Label(self, text="Search:")
        search_label.pack()
        self.search_entry = tk.Entry(self)
        self.search_entry.pack()
        search_button = tk.Button(self, text="Search", command=self.search_transactions)
        search_button.pack()

    def display_transactions(self):
        # Display transactions in the treeview
        for category, category_transactions in self.transactions.items():
            for transaction in category_transactions:
                self.transaction_tree.insert("", "end", values=(category, transaction["amount"], transaction["date"]))

    def sort_column(self, column):
        '''this block of code is used to sort the transactions'''
        items = [(self.transaction_tree.set(child, column), child) for child in self.transaction_tree.get_children("")]
        items.sort(reverse=self.sort_reverse)
        for index, (value, child) in enumerate(items):
            self.transaction_tree.move(child, "", index)
        self.sort_reverse = not self.sort_reverse

    def search_transactions(self):
        '''this block of code is used to search the transactions'''
        search_text = self.search_entry.get().lower()
        for child in self.transaction_tree.get_children(""):
            values = self.transaction_tree.item(child)["values"]
            if search_text in str(values).lower():
                self.transaction_tree.selection_add(child)
            else:
                self.transaction_tree.selection_remove(child)



        
#Initialize variables
transactions = {}
update = 0
choice = 0


#ask for user's name    
name = input("Please Enter Your Name : ")#to save the transactions with this name

#print the user instructions
print("\n\t- Personal Finance Tracker -")
print("* This Tracker Helps You To Mainatain Your Transactions *")
while True: #use loop to keep the function run without stopping
    print("\nWhat Do You Want To Do?")
    print('''\nTo Add Transaction - Press 1\nTo View Transactions - press 2\nTo Update Trasaction - press 3\nTo Delete Transaction - press 4\nTo Display Summary - press 5\nTo Exit - Press 6\nTo Read A Bulk File - press 7''')
    choice =(input(" \nEnter Your choice : "))


    if choice == "1":
        add_transaction()
    
    elif choice == "2":
        view_transaction()

    elif choice == "3":
        if not transactions:
            print("- You Have Not Added Anything to Update -")
        else:
            update_transaction()

    elif choice == "4":
        delete_transaction()

    elif choice == "5":
        show_summary()
        
    elif choice == "6":
        print("...Exiting...")
        break
    
    elif choice == "7":
        file_name = input("Enter The Name of The File which Contains Bulk Transactions : ")
        file_name = file_name.capitalize()
        file_name = file_name+".txt"
        read_bulk_transactions(file_name)
        break
         
    else:
        print("- Invalid Choice! Please read the instuctions carefully and try again:( -")


save_transactions()
load_transactions()

while True:
    gui = input("Would You Like to Use GUI version of this Tracker ? :(Yes or No) ")
    if gui.lower()== 'yes':
        app = PersonalFinanceTrackerGUI()
        app.display_transactions()
        app.mainloop()
        break
    
    elif gui.lower()== 'no':
        print(" Thank You ")
        break
        
    else:
        print(" Invalid Input ")
             
        
        
        
        
