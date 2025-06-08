"""Routes for the application."""
from flask import Flask, render_template, redirect, url_for, flash, request
from app.forms import RegistrationForm
from app import db, bcrypt
from app.models.user import User

app = Flask(__name__)
app.secret_key = 'somerandomvalue'

def register_routes(app): 
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
            return redirect(url_for('login'))
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

    @app.route('/seminar/financial-mindset')
    def seminar_financial_mindset():
        return render_template('event-details-financial-mindset.html')

    @app.route('/seminar/learn-how-to-learn')
    def seminar_learn_how_to_learn():
        return render_template('event-details-learn-how-to-learn.html')

    @app.route('/seminar/talk-by-the-author')
    def seminar_talk_by_author():
        return render_template('event-details-talk-by-the-author.html')

    @app.route('/seminar/ted-talk')
    def seminar_ted_talk():
        return render_template('event-details-ted-talk.html')  

    @app.route('/book-ticket', methods=['POST'])
    def book_ticket():
        name = request.form.get('name')
        email = request.form.get('email')
        flash('Booking successful!', 'success')
        return redirect(url_for('seminar_financial_mindset'))

    @app.route('/update-event', methods=['POST'])
    def update_event():
        return redirect(url_for('seminar_financial_mindset'))

    @app.route('/event-details') 
    def event_details(): 
        return render_template('event-details.html')

    @app.route('/booking-history') 
    def booking_history(): 
        return render_template('booking-history.html')

    @app.route('/select-event', methods=['POST'])
    def select_event(): 
        selected_event = request.form.get('event_type')
        
        if selected_event == "Talk by the Author":
            return redirect(url_for('seminar_talk_by_author'))
        elif selected_event == "Learn how to learn":
            return redirect(url_for('seminar_learn_how_to_learn'))
        elif selected_event == "Ted Talk":
            return redirect(url_for('seminar_ted_talk'))
        elif selected_event == "Financial Mindset":
            return redirect(url_for('seminar_financial_mindset'))
        else:
            flash("Please select a valid event type.")
            return redirect(url_for('home_page'))
            

# Register routes
register_routes(app)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
