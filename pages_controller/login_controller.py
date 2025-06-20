from flask import request, redirect, url_for, render_template
from business_logic import sign_up_logic, sign_in_logic, account_logic
from models import Account
from functions import get_name_and_password_from_form
from repository import account_access


def sign_up_page():

    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        is_successfully_created = sign_up_logic.sign_up(name, password)
        if is_successfully_created:
            return redirect(url_for('sign_in'))
        elif not is_successfully_created:
            return redirect(url_for('sign_up'))
    return render_template('sign_up.html')

def sign_in_page():
    if request.method == 'POST':
        name, password = get_name_and_password_from_form(request.form)
        orig_account = account_access.get_record_by(name=name)
        print(orig_account, type(orig_account))
        if sign_in_logic.login(orig_account, password):
            return redirect(url_for('home'))
        return 'не удалось войти'
    return render_template('sign_in.html')

def sign_out_page():
    # logout_user()
    return redirect(url_for('home'))