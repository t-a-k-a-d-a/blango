from django import template
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from blog.models import Post

user_model = get_user_model()

register = template.Library()


@register.filter
# <small>By
# {% if post.author == request.user %}
#     <strong>me</strong>
# {% else %}
#     {% if post.author.email %}
#         <a href="mailto:{{ post.author.email }}">
#     {% endif %}
#         {% if post.author.first_name and post.author.last_name %}
#             {{ post.author.first_name }} {{ post.author.last_name }}
#         {% else %}
#             {{ post.author.username }}
#         {% endif %}
#     {% if post.author.email %}
#         </a>
#     {% endif %}
# {% endif %}
# on {{ post.published_at|date:"M, d Y" }}
# </small>

# def author_details(author, current_user):
#     if not isinstance(author, user_model):
#         # return empty string as safe default
#         return ""

#     if author == current_user:
#         return format_html("<strong>me</strong>")

#     if author.first_name and author.last_name:
#         name = f"{author.first_name} {author.last_name}"
#     else:
#         name = f"{author.username}"

#     if author.email:
#         prefix = format_html('<a href="mailto:{}">', author.email)
#         suffix = format_html("</a>")
#     else:
#         prefix = ""
#         suffix = ""

#     return format_html('{}{}{}', prefix, name, suffix)


# @register.simple_tag
# def row():
#     return format_html('<div class="row">')


# @register.simple_tag
# def endrow():
#     return format_html("</div>")

@register.filter
def author_details(author, current_user):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

# @register.simple_tag
# def col(extra_classes=""):
#     return format_html('<div class="col {}">', extra_classes)


# @register.simple_tag
# def endcol():
#     return format_html("</div>")

@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}