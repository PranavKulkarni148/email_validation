# email authentication
from validate_email import validate_email
email = input("Enter your Email Id:")
password = 'admin'
pass1 = input("Enter password:")
# if email and password are valid
if validate_email(email) == True and pass1 == 'admin':
    print("Login Successful")
else:
    print("Login Failed")