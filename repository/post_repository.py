from models import Post, db
from functions import write_logs
from repository.ParentAccess import ModelAccess


class PostAccess(ModelAccess):
    def __init__(self):
        super().__init__(model=Post)

post_access = PostAccess()










