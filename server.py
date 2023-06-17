from flask import Flask, jsonify, request,render_template, redirect,url_for, session,flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateTimeField
from functools import wraps



male_meno = 'hellooooo another change'




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/I am faggot/Downloads/DataBase/problem-collection.db'
app.config['SECRET_KEY'] = 'sdiufhiurwdhfs1332423432'

db = SQLAlchemy(app)

class  Problems(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        problem = db.Column(db.String(255))
        description = db.Column(db.String(255))
        time = db.Column(db.DateTime, default=datetime.utcnow)
        
# class Users(db.Model):
#         username = db.Column(db.String(255))
#         password = db.Column(db.String(255))
    
        
        
#!!!!!!!!!!!!!!!!!!!perhaps to hash the cookie, research more variants !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def admin_login_required(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        # Check if user is logged in as admin
        try:
            if session['user'] != 'admin':
                 return redirect(url_for('login'))
        except KeyError:
            # Redirect to login page 
            return redirect(url_for('login'))
        print(session['user'])        
        # User is logged in as admin, proceed to the route function
        return route_function(*args, **kwargs)
    
    return decorated_function

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        

#ROUTE TO MENU ---> REDIRECT 
@app.route('/')
def home():
    return redirect(url_for('login'))


#ROUTE TO MENU
@app.route('/menu')

def menu():
    footer_tag = datetime.now().year
    return render_template('menu.html',footer_el=footer_tag)


#ROUTE TO DB OVERVIEW
@app.route('/problems')
@admin_login_required
def show_problems():   
  
    problems = Problems.query.all()
    footer_tag = datetime.now().year
    return render_template('data.html', problems=problems, footer_el=footer_tag)


#LOGIN ROUTE
@app.route('/login', methods=['GET', 'POST'] )
def login():
    
    class LoginForm(FlaskForm):
        username = StringField('Username')
        password = PasswordField('Password')
        submit = SubmitField('Submit')
        
    form = LoginForm()
    if form.validate_on_submit():
        # Form was submitted and passed validation
        username = form.username.data
        password = form.password.data
        
        # master_account = Users.query
        
        if username == 'admin' and password == 'password123':
            # Username and password are correct
            session['user'] = 'admin'
            return redirect('/menu')
        else:
            # Username and password are incorrect
            return render_template('login.html', form=form, error_message='Incorrect username or password')

    
    footer_tag = datetime.now().year
    return render_template('login.html', footer_el=footer_tag, form=form)





@app.route('/submit', methods=['GET', 'POST'] )
@admin_login_required
def submit():
        footer_tag = datetime.now().year 
        if request.method == 'POST':
            problem= request.form['problem']
            description = request.form['description']
            time = datetime.now()
            if (len(description) and len(problem)) > 0:
                new_record = Problems(problem=problem,
                            description=description,
                            time=time)
                db.session.add(new_record)
                db.session.commit()
                return redirect(url_for('menu'))
            else:
                return render_template('submit_form.html', error_message='Do not leave empty field!', footer_el=footer_tag )
            
        return render_template('submit_form.html', footer_el=footer_tag)



# @app.route('/problem', methods=['GET'] )
# @admin_login_required
# def get_problem():


#     return 'hello'



        
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    