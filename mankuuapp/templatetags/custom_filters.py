import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight_search(value, query):
    if not query:
        return value

    # Escape special characters in the query
    escaped_query = re.escape(query)

    # Replace query with highlighted version
    highlighted = re.sub(
        rf"({escaped_query})",  # Regex to match the query
        r'<span class="highlight">\1</span>',  # Wrap match in span
        str(value),  # Convert value to string
        flags=re.IGNORECASE  # Case insensitive matching
    )
    return mark_safe(highlighted)  # Mark as safe for rendering HTML
