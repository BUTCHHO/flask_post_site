from flask import render_template, request
from flask_login import current_user
from business_logic import user_logic
from repository import account_access

def profile_page(user_id):
    profile_owner = account_access.get_record_by_id(user_id)
    if request.method == 'POST' and current_user.is_authenticated:
        form_type = request.form['form_type']
        if form_type == 'follow':
            user_logic.follow_to_account(current_user, profile_owner)



    return render_template('profile_page.html', user=profile_owner)
