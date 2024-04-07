from flask import Flask, render_template , request
from datetime import datetime
import json


app = Flask(__name__)

current_time_of_transaction = str(datetime.now())

accounts = []
admins = []
transactions = []



with open("user_data.json", "r") as file:
    accounts = json.load(file)
    print(accounts)

with open("admin_data.json", "r") as file:
    admins = json.load(file)
    print(admins)

with open("transactions_data.json", "r") as file:
    transactions = json.load(file)
    print(transactions) 



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/atm")
def atm():
    return render_template("atm.html")



#Customer


#Log In

@app.route("/balance", methods=['GET', 'POST'])
def balance():
    if request.method == 'POST':
        try:
            account_id = int(request.form['account_id']) -1
            if  accounts[account_id]['password'] == request.form['password'] and account_id + 1 == accounts[account_id]['id'] :
                return render_template("view_balance.html", account=accounts[account_id])
            else:
                return render_template("error_customers.html", error="Wrong account id or pin")
        except ValueError:
            return render_template("error_customers.html", error="Wrong account id or pin")
    else:
        return render_template("balance.html") 



#Withdraw

@app.route("/withdraw", methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        try:
            account_id = int(request.form['account_id']) -1
            withdraw_amount = int(request.form['amount'])
            previous_balance = accounts[account_id]['balance']
            new_balance = accounts[account_id]['balance'] - withdraw_amount
            accounts[account_id]['balance'] = new_balance
            with open('user_data.json', 'w') as file:
                json.dump(accounts, file, indent=4)
                print(accounts)
            if  accounts[account_id]['password'] == request.form['password'] and account_id + 1 == accounts[account_id]['id']:
                if new_balance < 0:
                    return render_template("error_customers.html", error="Negative Amount")
                elif withdraw_amount > 5000:
                    return render_template("error_customers.html", error="High Balance")
                else:
                    id = accounts[account_id]['id']
                    transactions.append({'id': id, 'transaction': {'previous_balance': previous_balance, 'new_balance': new_balance,'type': 'withdraw', 'amount': withdraw_amount, 'date': current_time_of_transaction}})
                    with open('transactions_data.json', 'w') as file:
                        json.dump(transactions, file, indent=4)
                        print(transactions)
                    return render_template("view_balance.html", account=accounts[account_id])
            else:
                return render_template("error_customers.html", error="Wrong account id or pin")
        except ValueError:
            return render_template("error_customers.html", error="Wrong account id or pin")
    else:
        return render_template("withdraw.html") 



#Diposit

@app.route("/deposit", methods=['GET', 'POST'])
def diposit():
    if request.method == 'POST':
        try:
            account_id = int(request.form['account_id']) -1
            deposit_amount = int(request.form['amount'])
            previous_balance = accounts[account_id]['balance']
            new_balance = accounts[account_id]['balance'] + deposit_amount
            accounts[account_id]['balance'] = new_balance
            with open('user_data.json', 'w') as file:
                json.dump(accounts, file, indent=4)
                print(accounts)
            if  accounts[account_id]['password'] == request.form['password'] and account_id + 1 == accounts[account_id]['id']:
                if deposit_amount > 5000:
                    return render_template("error_customers.html", error="High Amount")
                else:
                    id = accounts[account_id]['id']
                    transactions.append({'id': id, 'transaction': {'previous_balance': previous_balance, 'new_balance': new_balance,'type': 'diposit', 'amount': deposit_amount, 'date': current_time_of_transaction}})
                    with open('transactions_data.json', 'w') as file:
                        json.dump(transactions, file, indent=4)
                        print(transactions)
                    return render_template("view_balance.html", account=accounts[account_id])
            else:
                return render_template("error_customers.html", error="Wrong account id or pin")
        except ValueError:
            return render_template("error_customers.html", error="Wrong account id or pin")
    else:
        return render_template("deposit.html") 



#Transactions

@app.route("/transactions", methods=['GET', 'POST'])
def view_transactions():
    if request.method == 'POST':
        try:
            account_id = int(request.form['account_id']) -1
            account_transactions = []
            j = 0
            if  accounts[account_id]['password'] == request.form['password'] and account_id + 1 == accounts[account_id]['id']:
                if transactions == []:
                    return render_template("error_customers.html", error="No Transactions")
                else:

                    for i in range(len(transactions)):
                        if transactions[i]['id'] == account_id + 1:
                            j = j + 1
                            account_transactions.append({'numero': j, 'content': transactions[i]})
                            print(account_transactions)

                    if account_transactions == []:
                        return render_template("error_customers.html", error="No Transactions")
                    else:
                        return render_template("view_transactions.html", account_transactions = account_transactions, account_id = account_id + 1)
            else:
                return render_template("error_customers.html", error="Wrong account id or pin")
        except ValueError:
             return render_template("error_customers.html", error="Wrong account id or pin")
    else:
        return render_template("transactions.html") 



#Bank Administrators


#Log In

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        try:
            admin_id = request.form['admin_id']
            admin_password = request.form['password']
            for i in range(len(admins)):
                if int(admin_id) == admins[i]['id'] and admin_password == admins[i]['password']:
                    return render_template("view_admin.html", admin=admins[i])
            else:
                return render_template("error_admins.html", error="Wrong account id or pin")
        except ValueError:
            return render_template("error_admins.html", error="Wrong account id or pin")
    else:
        return render_template("admin.html")



#User Registration

@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            pin = [int(x) for x in str(password)]
            if len(pin)!= 4:
                return render_template('register.html', message = "Wrong Input")
            else:
                for i in range(len(accounts)):
                    if accounts[i]['username'] == username:
                        return render_template("register.html", message = "Account already exists ")
                else:
                    if accounts == []:
                        id = 1
                        accounts.append({'id': id, 'username': username, 'password': password, 'balance': 0, 'activity': 'active'})
                        with open('user_data.json', 'w') as file:
                            json.dump(accounts, file, indent=4)
                            print(accounts)
                        return render_template('register.html', message = "Account created")
                    else:    
                        password = request.form['password']
                        id = accounts[-1]['id'] + 1
                        accounts.append({'id': id, 'username': username, 'password': password, 'balance': 0, 'activity': 'active'})
                        with open('user_data.json', 'w') as file:
                            json.dump(accounts, file, indent=4)
                            print(accounts)
                        return render_template('register.html', message = "Account created")
        except ValueError:
            return render_template('register.html', message = "Wrong Input")
    else:
        return render_template('register.html')



#User Suspension

@app.route('/suspend', methods= ['GET', 'POST'])
def suspend():
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id']) -1
            user_password = request.form['user_password']
            username = request.form['user_username']
            if user_password == accounts[user_id]['password'] and username == accounts[user_id]['username'] and user_id +1 == accounts[user_id]['id']:
                    if accounts[user_id]['activity'] == 'suspended':
                        return render_template("suspend.html", message = "Account already suspended")
                    else:
                        accounts[user_id]['activity'] = 'suspended'
                        with open('user_data.json', 'w') as file:
                            json.dump(accounts, file, indent=4 )
                            print(accounts)
                        return render_template("suspend.html", message = "Account suspended")
            else:
                return render_template("suspend.html", message = "Wrong Inputs")
        except ValueError:
            return render_template("suspend.html", message = "Wrong Inputs")
    else:
        return render_template("suspend.html")



#User Activation

@app.route('/activate', methods= ['GET', 'POST'])
def activate():
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id']) -1
            user_password = request.form['user_password']
            username = request.form['user_username']
            if user_password == accounts[user_id]['password'] and username == accounts[user_id]['username'] and user_id +1 == accounts[user_id]['id']:
                    if accounts[user_id]['activity'] == 'active':
                        return render_template("activate.html", message = "Account already active")
                    else:
                        accounts[user_id]['activity'] = 'active'
                        with open('user_data.json', 'w') as file:
                            json.dump(accounts, file, indent=4 )
                            print(accounts)
                        return render_template("activate.html", message = "Account activated")
            else:
                return render_template("activate.html", message = "Wrong Inputs")
        except ValueError:
            return render_template("activate.html", message = "Wrong Inputs")
    else:
        return render_template("activate.html")



#Accounts

@app.route('/view_accounts', methods= ['GET', 'POST'])
def view_accounts():
    return render_template("view_accounts.html", accounts = accounts)