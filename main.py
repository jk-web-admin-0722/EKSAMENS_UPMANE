from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('sakums.html')

@app.route('/pavasaris')
def pavasaris():
   return render_template('pavasaris.html')

@app.route('/vasara')
def vasara():
   return render_template('vasara.html')

@app.route('/rudens')
def rudens():
   return render_template('rudens.html')

@app.route('/ziema')
def ziema():
   return render_template('ziema.html')

if __name__ == "__main__":
   app.run(debug = True)