print("Registration Application : ")
username=input("Enter your username : ")
email=input("Enter your email id : ")
password=input("Enter your password : ")
c_password=input("Confirm your password : ")
gender=input("Enter your gender : ")

if username and email and password and c_password and gender:
    if username.isalnum():
        if '@' in email and email.endswith('.com'):
            if password == c_password:
                if len(password) >=8:
                    print("Registration Complete")
                    print("🎉🎉🎉🎉")
                else:
                    print("Password too small")
            else:
                print("Password does not match")
        else:
            print("Invalid Email")
    else:
        print("Invalid Username")
else:
    print("All fields must be filled")

                   
            
            
            
                