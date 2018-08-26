from bf_monitor import app, db, bcrypt
from flask import render_template, flash, redirect, url_for, request
from bf_monitor.forms import RegistrationForm, LoginForm, UpdateAccountForm, MonitorringForm
from bf_monitor.models.user import User
from bf_monitor.models.test_data import TestUser
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/homepage')
def homepage():
    form = MonitorringForm()
    def paste_paym():
        data = form.paym_available.data
        form.test_data_selected.choices = data
    if current_user.is_authenticated:
        form.paym_available.choices = [(paym_user.id, paym_user.username) for paym_user in TestUser.get_paym_list(current_user.id)]
        form.payg_available.choices = [(payg_user.id, payg_user.username) for payg_user in TestUser.get_payg_list(current_user.id)]
    else:
        form.paym_available.choices = []
        form.payg_available.choices = []
    return render_template('home.html', title='Home page', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Please, log in with your new credentials.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_email(form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('homepage'))
        else:
            flash('Please, check email or password!', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route('/managedata', methods=['GET', 'POST'])
@login_required
def manage_data():
    pass