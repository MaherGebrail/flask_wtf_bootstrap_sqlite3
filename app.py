from flask import Flask,render_template,request,url_for,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired,Length,Email,EqualTo
from wtforms import StringField,PasswordField,SubmitField


import sqlite3


app = Flask(__name__)
Bootstrap(app)


app.config["SECRET_KEY"]="this is password"


class LoginForm(FlaskForm):
    username= StringField('username',validators=[InputRequired(),Length(min=3, max=25,message="enter your mail")])
    password=PasswordField('password',validators=[InputRequired(),Length(min=5,max=30)]) #,AnyOf(values=['password'])
    submit_button = SubmitField('Submit Form')

class SignupForm(FlaskForm):
    email_add=StringField('email',validators=[InputRequired(),Email()])
    username=StringField('username',validators=[InputRequired(),Length(min=3, max=25,message="enter your mail")])
    password=PasswordField('password1',validators=[InputRequired(),Length(min=8,max=30)])
    password2=PasswordField('password2',validators=[InputRequired(),Length(min=8,max=30),EqualTo('password',"passwords field must be equal")])
    submit_button = SubmitField('Submit Form')



conn= sqlite3.connect("test.db")#it create file if not exist
c=conn.cursor()





@app.route("/",methods=["GET","POST"])
def index():
    form=LoginForm()

    if form.validate_on_submit():
        print(request.form)
        print(form.username.data)
        try:
            with sqlite3.connect("test.db") as conn:

                c = conn.cursor()
                x=c.execute(""" SELECT * FROM users WHERE name = :name AND pass= :pass""",
                          {"name":form.username.data,"pass":form.password.data}).fetchone()
                if x :
                    return f"{x} are logged in"

            error_="try again , your account , has no exist , or signup"
        except Exception as e:
            print(e)
            return redirect(url_for('sign_up_p'))

    try:
        return render_template('home.html', form=form, er=error_)
    except Exception:
        return render_template('home.html',form=form)


@app.route("/signup",methods=["GET","POST"])
def sign_up_p():
    form=SignupForm()

    if form.validate_on_submit():
        with sqlite3.connect("test.db") as conn:
            c = conn.cursor()
            c.execute("""INSERT INTO users(name,pass,email) VALUES (:name,:pass,:mail)""",
                  {"name":form.username.data,"pass":form.password.data,"mail":form.email_add.data})
            conn.commit()
        return redirect(url_for('index'))

    return render_template('sign_up.html',form=form,)





if __name__ == "__main__":
    app.run(debug=True)