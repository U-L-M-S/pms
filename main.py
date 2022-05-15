import typer
import account_management
import password
import connection_flask
app = typer.Typer()


@app.command()
def hibp(pw: str):
    '''[password]   EX: python3 main.py hibp 123abcd'''
    object_hibp = password.Password.hibp(pw)
    int(object_hibp or 0)
    if object_hibp == None:
        print(f"Your password has been 0 times leaked. It is safe")
    else:
        print(f"Your password has been {object_hibp} times leaked. It is NOT safe")


@app.command()
def login(username: str, pw: str):
    '''[username] [password]  for the login  '''
    object_login = account_management.Account.login(username, pw)

@app.command()
def signup(username: str, pw: str):
    '''[username] [password]   EX: signup Tobias 420*69+Zou '''
    object_ca = account_management.Account.create_account(username, pw)
    if object_ca == True:
        print("Account created successfully")
    else:
        print("Ups... something went wrong")


@app.command()
def gpw(file_name: str, quantity_pw: int):
    '''[file_name] [quantity of passwords] Generate Passwords'''
    if quantity_pw == None:
        quantity_pw = 100
    object_gpw = password.Password.generate_pw(file_name, int(quantity_pw))
    if object_gpw == False:
        print("Ups something went wrong")

@app.command()
def flask():
    connection_flask.app.run()

if __name__ == '__main__':
    app()
