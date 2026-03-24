from flask import Flask,render_template,request,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)


class Employee(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        if not name or not email:
            flash("All fields are required", "danger")
            return redirect('/')
        
        employee = Employee(name=name, email=email)
        db.session.add(employee)
        db.session.commit()

        flash("Employee added successfully!", "success")
        return redirect("/")
    
    allemployees = Employee.query.all()
    return render_template("index.html", allemployees=allemployees)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/delete/<int:sno>")
def delete(sno):
    employee = Employee.query.filter_by(sno=sno).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        employee = Employee.query.filter_by(sno=sno).first()
        employee.name = name
        employee.email = email
        db.session.add(employee)
        db.session.commit()
        return redirect("/")

    employee = Employee.query.filter_by(sno=sno).first()
    return render_template("update.html", employee=employee)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()