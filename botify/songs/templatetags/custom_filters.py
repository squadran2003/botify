from django import template
import datetime

register = template.Library()


@register.simple_tag
def convert_date(date):
    # return date in a humean readable format like 1 hour ago, 1 day ago, 1 month ago, 1 year ago
    now = datetime.datetime.now().date()
    date = now - date.date()
    if date.days == 0:
        return "Today"
    elif date.days == 1:
        return "Yesterday"
    return "{} days ago".format(date.days)