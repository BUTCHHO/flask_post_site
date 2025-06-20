from functions import write_logs
from models.comment import db, Comment
from repository.ParentAccess import ModelAccess


class CommentAccess(ModelAccess):

    def __init__(self):
        super().__init__(model=Comment)

    def add_comment_to_user_liked_comments(self, comment, user):
        if comment not in user.liked_comments:
            user.liked_comments.append(comment)
        else:
            user.liked_comments.remove(comment)
        comment.likes = len(user.liked_comments)

    @write_logs
    def create_comment(self, content, author_id, commented_post):
        comment = Comment(content=content, author_id=author_id, post_id = commented_post.id)
        commented_post.comments.append(comment)
        db.session.commit()

    @write_logs
    def like_comment(self, liked_comment_id, user):
        liked_comment = ModelAccess.get_record_by_id(liked_comment_id)
        self.access.add_comment_to_user_liked_comments(liked_comment, user)
        db.session.commit()

comment_access = CommentAccess()