from django.apps import apps
from django.core import signing
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django_comments_xtd.models import XtdComment
from django_comments_xtd.views import get_moderated_tmpl

from catalog.models import Book


def sent(request, using=None):
    comment_pk = request.GET.get("c", None)
    try:
        comment_pk = int(comment_pk)
        comment = XtdComment.objects.get(pk=comment_pk)
    except (TypeError, ValueError, XtdComment.DoesNotExist):
        value = signing.loads(comment_pk)
        ctype, object_pk = value.split(":")
        model = apps.get_model(*ctype.split(".", 1))
        target = model._default_manager.using(using).get(pk=object_pk)
        template_arg = ["django_comments_xtd/posted.html",
                        "comments/posted.html"]
        return render(request, template_arg, {'target': target})
    else:
        if (
                request.is_ajax() and comment.user and
                comment.user.is_authenticated
        ):
            if comment.is_public:
                template_arg = [
                    "django_comments_xtd/%s/%s/comment.html" % (
                        comment.content_type.app_label,
                        comment.content_type.model),
                    "django_comments_xtd/%s/comment.html" % (
                        comment.content_type.app_label,),
                    "django_comments_xtd/comment.html"
                ]
            else:
                template_arg = get_moderated_tmpl(comment)
            return render(request, template_arg, {'comment': comment})
        else:
            if comment.is_public:
                return HttpResponseRedirect('/')
            else:
                moderated_tmpl = get_moderated_tmpl(comment)
                return render(request, moderated_tmpl, {'comment': comment})


class CommentsListView(DetailView):
    model = Book
    template_name = 'commenting/comments_list.html'
    context_object_name = 'book'
