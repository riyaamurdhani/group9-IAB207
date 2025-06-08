from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms.forms import RegistrationForm
from app.models import User
from app import db, bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/home')
def home_page():
    return render_template('home-page.html')

@auth_bp.route('/login')
def login():
    return render_template('login.html')

@auth_bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            firstname=form.firstname.data,
            middlename=form.middlename.data,
            lastname=form.lastname.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            contact_number=form.contact_number.data,
            address=form.address.data
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful', 'success')
        return redirect(url_for('auth.login'))
    return render_template('registration.html', form=form)

@auth_bp.route('/about-us')
def about_us():
    return render_template('about-us.html')

@auth_bp.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

@auth_bp.route('/create-event')
def create_event():
    return render_template('create-event.html')

@auth_bp.route('/event-details')
def event_details():
    return render_template('event-details.html')

@auth_bp.route('/booking-history')
def booking_history():
    return render_template('booking-history.html')

@auth_bp.route('/event/talk-by-the-author')
def seminar_talk_by_author():
    return render_template('seminar_talk_by_author.html')

@auth_bp.route('/event/learn-how-to-learn')
def seminar_learn_how_to_learn():
    return render_template('seminar_learn_how_to_learn.html')

@auth_bp.route('/event/ted-talk')
def seminar_ted_talk():
    return render_template('seminar_ted_talk.html')

@auth_bp.route('/event/financial-mindset')
def seminar_financial_mindset():
    return render_template('seminar_financial_mindset.html')
