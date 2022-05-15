import random
import requests
import hashlib
import json


class Password:

    def hibp(pw):
        if len(pw) == 0:
            return False
        else:
            hashed_pw = hashlib.sha1(pw.encode()).hexdigest().upper()

            first_5_digits = hashed_pw[:5]
            r = requests.get("https://api.pwnedpasswords.com/range/" + first_5_digits)
            passwords = r.text.split("\r\n")

            for line in passwords:
                pw_list = line.split(":")
                if hashed_pw[5:] == pw_list[0]:
                    return int(0 if pw_list[1] is None else pw_list[1])

    @staticmethod
    def getPolicies():
        # get the policies in the pw_policies.json
        file_name = "pw_policies.json"
        with open(file_name, "r") as f:
            temp = json.load(f)
            for entry in temp:
                pw_minimal_length = entry["pw_min_length"]
                pw_lowercase = entry["pw_lowercase"]
                pw_uppercase = entry["pw_uppercase"]
                pw_symbol = entry["pw_symbols"]
                pw_digits = entry["pw_digits"]
            f.close()

        policies = {'pw_minimal_length': pw_minimal_length, 'pw_lowercase': pw_lowercase, 'pw_uppercase': pw_uppercase,
                    'pw_digits': pw_digits,
                    'pw_symbol': pw_symbol}

        return policies

    @staticmethod
    def generate_pw(file_name, quantity_pw):
        if len(file_name) == 0:
            print("you need to give a name for the file")
            return False

        else:

            policies = Password.getPolicies()
            uppercase = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
            lowercase = uppercase.lower()
            digits = "0123456789"
            symbols = "@#$%^&*()-+?_=,<>/,\\;.:-_"

            list_pw = []
            all_policies = ""

            if policies.get('pw_uppercase') is True:
                all_policies += uppercase
            if policies.get('pw_lowercase') is True:
                all_policies += lowercase
            if policies.get('pw_symbol') is True:
                all_policies += digits
            if policies.get('pw_digits') is True:
                all_policies += symbols

            for passwords in range(quantity_pw):
                pw = "".join(random.sample(all_policies, policies.get('pw_minimal_length')))
                list_pw.append(pw)

            with open(file_name + '.txt', 'w') as f:
                for x in list_pw:
                    f.write('%s\n' % x)

            print(f"Your file {file_name}.txt has been created")
            return True

    @staticmethod
    def check_password_criteria_L_and_CA(pw):
        symbols = "@#$%^&*()-+?_=,<>/,\\;.:-_"
        policies = Password.getPolicies()

        if len(pw) < policies.get('pw_minimal_length'):
            print("ERROR! Password is too short")
            return False
        if policies.get('pw_uppercase') and not any(uc.isupper() for uc in pw):
            print("ERROR! Password does not contains any uppercase")
            return False
        if policies.get('pw_lowercase') and not any(lc.islower() for lc in pw):
            print("ERROR! Password does not contains any lowercase")
            return False
        if policies.get('pw_digits') and not any(dg.isdigit() for dg in pw):
            print("ERROR! Password does not contains any digits")
            return False
        if policies.get('pw_symbol') and not any(sy in symbols for sy in pw):
            print("ERROR! Password contains does not any symbols[@#$%^&*()-+?_=,<>/,\\;.:-_]")
            return False
        return True

    def pw_encrypt(pw):
        pw_encrypted = hashlib.sha512(str(pw).encode("utf-8")).hexdigest()
        return pw_encrypted


    def pw_hash_for_hibp(pw):
        pw_encrypted = hashlib.sha1(str(pw).encode("utf-8")).hexdigest()
        return pw_encrypted

    def pw_comparation(pw, pw_encrypted):
        user_input_hashed = hashlib.sha512(str(pw).encode("utf-8")).hexdigest()
        if user_input_hashed == pw_encrypted:
            return True
        else:
            return False
