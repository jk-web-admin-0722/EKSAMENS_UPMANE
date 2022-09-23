from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def sakums():
    msg = ""
    if request.method == 'POST':
        faveseason = request.form.get('faveseason')
        cutseason = request.form.get('cutseason')
        line = f"{faveseason},{cutseason}\n"
        with open("aptaujas_rez.csv", "a", encoding="utf-8") as f:
            f.write(line)

        msg = "Paldies par dalību aptaujā!"

    return render_template('sakums.html', message = msg)

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