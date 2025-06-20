from flask import request, redirect, url_for, abort, render_template
from flask_login import current_user, login_required
from business_logic import post_logic, comment_logic
from repository import post_access, comment_access

@login_required
def create_post_page():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        print(title, content)
        if title and content:
            is_successfully_created = post_logic.create_post(title=title, content=content,author=current_user)
            if is_successfully_created:
                return redirect(url_for('home'))
            else:
                abort(500)
        return 'не введён заголовок или содержание статьи'
    return render_template('create.html')

def post_page(post_id):
    target_post = post_access.get_record_by_id(post_id)
    if target_post == None:
        abort(404)
    elif request.method == 'POST':
        if current_user.is_authenticated:
            form_type = request.form.get('form_type')
            if form_type == 'like_post':
                if target_post not in current_user.liked_posts:
                    post_logic.like_post(target_post, current_user)
                else:
                    post_logic.unlike_post(target_post, current_user)
            elif form_type == 'write_comment':
                comment_content = request.form['comment_content']
                if comment_content:
                    comment_logic.create_comment(comment_content, current_user.id, target_post.id)
            elif form_type == 'like_comment':
                liked_comment_id = request.form['liked_comment_id']
                liked_comment = comment_access.get_record_by_id(liked_comment_id)
                if liked_comment not in current_user.liked_comments:
                    comment_logic.like_comment(liked_comment, current_user)
                else:
                    comment_logic.unlike_comment(liked_comment, current_user)
        else:
            return "войдите в аккаунт чтобы комментировать"
    return render_template('post_extended.html', post=target_post)