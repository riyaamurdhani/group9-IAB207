from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db, bcrypt, mail
from app.models.user import User
from flask_mail import Message
from flask_login import login_user
import random, string

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        # Generate random password
        raw_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        hashed_password = bcrypt.generate_password_hash(raw_password).decode('utf-8')

        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        # Send email with username & password
        msg = Message('Your Account Credentials',
                      sender='noreply@example.com',
                      recipients=[email])
        msg.body = f"Hello {username},\n\nYour login password is: {raw_password}"
        mail.send(msg)

        flash('User registered and credentials sent to email.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('auth.dashboard'))  # Create this route later
        else:
            flash('Login failed. Check your email or password.', 'danger')

    return render_template('login.html')
