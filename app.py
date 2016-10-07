#Yikai Wang
#Period 6 SoftDev

from flask import Flask, render_template, request, url_for, session, redirect
from utils import authenticate
import os

app = Flask(__name__) #create Flask object
app.secret_key = "dankMemes"

@app.route( "/" )
def home():
    print request.headers
    print session
    if 'username' in session and 'password' in session:
        return redirect( url_for( "authLogin" ) )
    return render_template( "home.html" )

@app.route( "/login/" )
def login():
    print request.headers
    return render_template( "login.html" )

@app.route( "/register/" )
def register():
    print request.headers
    return render_template( "register.html" )

@app.route( "/msg/loginauth/", methods = ['POST'] )
def authLogin():
    print request.headers
    print request.form[ "username" ]
    print request.form[ "password" ]

    valid = False
    msg = "Invalid Login: Dankness Level Too Low"
    if authenticate.authenticate(request.form[ "username" ], request.form[ "password" ]):
        msg = "Welcome! Access To Meme Collection Granted!"
        valid = True
        session[ "username" ] = request.form[ "username" ]
        session[ "password" ] = request.form[ "password" ]
        return render_template( "welcome.html", message = msg );
    return render_template( "auth.html", message = msg, validation = valid )

@app.route( "/msg/regauth/", methods = ['POST'] )
def authReg():
    print request.headers
    print request.form[ "username" ]
    print request.form[ "pass1" ]
    print request.form[ "pass2" ]

    valid = False
    msg = authenticate.createAccount( request.form )
    if "Account" in msg and " created!" in msg:
        valid = True
    return render_template( "auth.html", message = msg, validation = valid )
    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
