#email validation using regex
import re

email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email_rec=input("Enter Your Email: ")

if re.search(email_condition,email_rec):
    print("Right Email")
else:
    print("wrong email")