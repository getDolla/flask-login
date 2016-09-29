#Yikai Wang
#Period 6 SoftDev

from flask import Flask, render_template, request

app = Flask(__name__) #create Flask object
@app.route( "/" )
def write():
    print request.headers
    return render_template( "form.html" )

@app.route( "/msg/", methods = ['POST'] )
def auth():
    print request.headers
    print request.form
    print request.form["username"]
    print request.form[ "password" ]
    return "You good"

if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
