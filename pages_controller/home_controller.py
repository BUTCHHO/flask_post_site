from flask import request, render_template
from flask_login import current_user
from repository import post_access
from business_logic import post_logic


def home_page():
    posts = post_access.get_all_records()
    if request.method == 'POST':
        if current_user.is_authenticated:
            form_type = request.form['form_type']
            if form_type == 'like_post':
                liked_post_id = request.form['liked_post_id']
                liked_post = post_access.get_record_by_id(liked_post_id)
                if liked_post not in current_user.liked_posts:
                    post_logic.like_post(liked_post, current_user)
                else:
                    post_logic.unlike_post(liked_post, current_user)
    return render_template('home.html', posts=posts)

