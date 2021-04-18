from django.urls import reverse
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
from django_comments_xtd.models import XtdComment
from catalog.models import Book


class BookComment(XtdComment):
    pass


class PostCommentModerator(CommentModerator):
    email_notification = True
    auto_moderate_field = 'date_of_publish'
    moderate_after = 365


moderator.register(Book, PostCommentModerator)
