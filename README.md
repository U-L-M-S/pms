PMS

It's a simple password manager system and it allowes the user some tools like: 
HIBP (findout if the user password has been leaked), 
Password Generator(Create new passwords),
etc.

USAGE:

Welcome in the version 4.0 os the Password Management System.

If you don't know how to start the software just do it:

    first you will need to start the virtual machine:
    Linux
        ->put fallowing command on the Terminal (it must be in the same path that the venv file) source venv/bin/activate

        Now you can use it
        -> python main.py --help
            and so it will show your options.
                ex: python main.py gpw 50 -> it will generate a list of passwords for you. You need to put a number behind it,
                it will generate a .txt file with the quantity of passwords that you chose.

    Windows
        ->put fallowing command on the Terminal (it must be in the same path that the venv file) source \env\Scripts\activate.bat OR just source \env\Scripts\activate

        now you can use it
        -> python \.main.py --help
             and so it will show your options.
                 ex: python \.main.py gpw test_file 50 -> it will generate a list of passwords for you. You need to put a number behind it,
                 it will generate a .txt file with the quantity of passwords that you chose.
