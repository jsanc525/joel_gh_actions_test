def func(x):
    return x + 2

def greet():
    return "Hello World"

def input_credentials():
    username=input('Please enter your username.')
    email=input('Please enter your email.')
    password=input('Please enter your password.')
    errors=[]
    success=True
    if(len(username)==0):
        errors.append("username cannot be empty.")
    if(' ' in username):
        errors.append('username cannot contain whitespaces.')
    if(not ('.' in email and '@' in email)):
        errors.append('email should contain both a . and an @ character.')
    if(len(password)<8):
        errors.append('password should contain at least 8 characters.')
    letter=False
    number=False
    special=False
    for i in range(len(password)):
        if(password[i].isalpha()):
            letter=True
        elif(password[i].isalnum()):
            number=True
        else:
            special=True
    if(not letter):
        errors.append('password must contain a letter')
    if(not number):
        errors.append('password must contain a number')
    if(not special):
        errors.append('password must contain a special character')
    if(len(errors)>0):
        success=False
    print(errors)
    return success,errors