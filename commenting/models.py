from django.urls import reverse
from django_comments_xtd.models import XtdComment
from jalali_date import date2jalali


class BookComment(XtdComment):
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return '{} درباره کتاب {} در تاریخ {}'.format(self.user.get_full_name(), self.content_object.title,
                                                      date2jalali(self.submit_date).strftime('%y/%m/%d'))

    def get_content_object_url(self):
        """
                Get a URL suitable for redirecting to the content object.
                """
        return reverse(
            'commenting:comments_list',
            args=[self.content_object.id, ]
        )
