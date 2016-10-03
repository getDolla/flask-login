import hashlib

def sha512Pass(password):
    m = hashlib.sha512()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('data/users.txt','r').readlines()
    for line in text:
        if line.split(",")[0] == user:
            return True
    return False

def authenticate(user, password):
    password = sha512Pass(password+user) # you can make this different, but still unique md5Pass(password+user)
    text = open('data/users.txt', 'r').readlines()
    for line in text:
        line = line.strip().split(",")
        if line[0]==user:
            if line[1]==password:
                return True
            else:
                return False
    return False

def createAccount(form):
    result = ""
    if "username" in form and "pass1" in form and "pass2" in form:
        user = form['username']
        password = form['pass1']
        password2 = form['pass2']
        if checkIfNameExists(user):
            result += "User exists: "+ user +"."
        elif password != password2:
            result += "Passwords do not match!"
        else:
            result += "Account "+user+" created!"
            f = open('data/users.txt','a')
            password = sha512Pass(password+user)
            f.write(user+","+password+"\n")
            f.close()
    else:
        result+="Invalid form submission, please fill in all fields"
    return result




