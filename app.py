from flask import Flask,render_template,request,flash

app=Flask(__name__)
app.secret_key="juliana123"
@app.route("/hello")

def index():
	flash('whats your name')
	return render_template("index.html")

@app.route('/greet',methods=['POST','GET'])


def greet():
	flash('hi' + str(request.form[' name_input '])+", great tto see you")
	return render_template('index.html')


if __name__=="__main__":
	app().run()
#to make file and add app : app in it  write this in cmd
# echo >  Procfile
#to make requirements file and get them automatically  write this in cmd
#pip freeze > requirements.txt
#and if any of their requerements are not statifyed @ and u cant see its version so pip install and its name and w
#and when its installed replace @ blah blah with its version numers


