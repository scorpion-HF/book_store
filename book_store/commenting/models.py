from django.urls import reverse
from django_comments_xtd.models import XtdComment


class BookComment(XtdComment):
    def get_content_object_url(self):
        """
                Get a URL suitable for redirecting to the content object.
                """
        return reverse(
            'commenting:comments_list',
            args=[self.content_object.id, ]
        )
