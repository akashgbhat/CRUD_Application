from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)

app.secret_key = "Secret Key"

app.config['SQLALCHEMY DATABASE URI'] = 'mysql://root: ''@localhost/crud'

app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data (db.Model):
    id = db.Column (db.Integer, primary)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    phone = db.Column(db.String(100))

def init (self, name, email, phone):
    self.name = name
    self.email = email
    self.phone = phone

app = Flask(__name__)
@app.route("/")
def Index():
    return render_template("main.html")

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        my_data = Data (name, email, phone) 
        db.session.add(my_data) 
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for(index))

@app.route('/update',methods=['GET','POST'])
def update():
        if request.method == 'POST':
             my_data = Data.query.get(request.form.get('id'))
             my_data.name = request.form['name']
             my_data.name = request.form['Email']
             my_data.name = request.form['phone']

             db.session.commit()
             flash("Employee updated Successfully")

             return redirect(url_for('Index'))
if __name__ == "__main__":
    app.run()