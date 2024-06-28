from flask import Flask,render_template,Response
app=Flask(__name__)
@app.route('/home',methods=["GET","POST"])
def home():
    return ("hello")