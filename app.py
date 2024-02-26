from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/CRUD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
#Creating model table for our CRUD database
class Estados(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(40))
    clave = db.Column(db.String(5))

    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave
        
class Users(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(100), nullable=False)
    apellido_p  = db.Column(db.String(100), nullable=False)
    apellido_m  = db.Column(db.String(100), nullable=False)
    persona     = db.Column(db.String(10), nullable=False)
    estado      = db.Column(db.String(5), nullable=False)
    curp        = db.Column(db.String(50), nullable=True)
    
    def __init__(self, nombre, apellido_p, apellido_m, persona, estado, curp):
        self.name = nombre
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.persona = persona
        self.estado = estado
        self.curp = curp

#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()
    estados = Estados.query.all()
    users = Users.query.all()
    #users = db.session.query(Estados.nombre, Users.id, Users.name, Users.apellido_p, Users.apellido_m, Users.persona, Users.estado, Users.curp).join(Users, Estados.id == Users.id).all()
    return render_template("index.html", employees = all_data, estados = estados, users = users)

#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name    = request.form['nombre']
        ap_p    = request.form['apellido_p']
        ap_m    = request.form['apellido_m']
        persona = request.form['persona']
        estado  = request.form['estado']
        curp    = request.form['curp']

        my_data = Users(name, ap_p, ap_m, persona, estado, curp)
        db.session.add(my_data)
        db.session.commit()

        flash("Users Inserted Successfully")
        return redirect(url_for('Index'))

#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Users.query.get(request.form.get('id'))
        
        if my_data:
            name    = request.form['nombre']
            ap_p    = request.form['apellido_p']
            ap_m    = request.form['apellido_m']
            persona = request.form['persona']
            estado  = request.form['estado']
            curp    = request.form['curp']
            db.session.commit()
            flash("Users Updated Successfully")
        else:
            flash("Users Not Found")

        return redirect(url_for('Index'))

#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Users.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("User Deleted Successfully")

    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)