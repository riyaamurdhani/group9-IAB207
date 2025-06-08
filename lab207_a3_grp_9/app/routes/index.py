"""Routes for the application."""
from flask import render_template, redirect, url_for
from app.forms.forms import RegistrationForm

def register_routes(app): 
    """Register routes for the application."""
    @app.route('/') 
    def index(): 
        return render_template('index.html')

    @app.route('/home') 
    def home_page(): 
        return render_template('home-page.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/registration', methods=['GET', 'POST'])
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
            print(new_user)
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful', 'success')

            return redirect(url_for('login'))  # or some success page
        return render_template('registration.html', form=form)

    @app.route('/about-us') 
    def about_us(): 
        return render_template('about-us.html')

    @app.route('/contact-us') 
    def contact_us(): 
        return render_template('contact-us.html')

    @app.route('/create-event') 
    def create_event(): 
        return render_template('create-event.html')
    
    @app.route('/event-details') 
    def event_details(): 
        return render_template('event-details.html')
    
