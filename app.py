from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def hello():
    
    return render_template('index.html')

@app.route('/name', methods = ['GET','POST'])
def name():
    if request.method == 'POST':
        names = request.form['firstname']
        print(names)
        return render_template('name.html', names=names)
    else:
        return render_template('name.html')


if __name__ == "__main__":
    app.run(debug=True)