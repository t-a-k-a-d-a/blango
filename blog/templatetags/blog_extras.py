from django import template
from django.contrib.auth.models import User
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.auth import get_user_model
user_model = get_user_model()

register = template.Library()


@register.filter
def author_details(author, current_user):
  <small>By
    {% if post.author == request.user %}
        <strong>me</strong>
    {% else %}
        {% if post.author.email %}
            <a href="mailto:{{ post.author.email }}">
        {% endif %}
            {% if post.author.first_name and post.author.last_name %}
                {{ post.author.first_name }} {{ post.author.last_name }}
            {% else %}
                {{ post.author.username }}
            {% endif %}
        {% if post.author.email %}
            </a>
        {% endif %}
    {% endif %}
    on {{ post.published_at|date:"M, d Y" }}
  </small>

    # if not isinstance(author, user_model):
    #     # return empty string as safe default
    #     return ""

    # if author == current_user:
    #     return format_html("<strong>me</strong>")

    # if author.first_name and author.last_name:
    #     name = f"{author.first_name} {author.last_name}"
    # else:
    #     name = f"{author.username}"

    # if author.email:
    #     prefix = format_html('<a href="mailto:{}">', author.email)
    #     suffix = format_html("</a>")
    # else:
    #     prefix = ""
    #     suffix = ""

    # return format_html('{}{}{}', prefix, name, suffix)