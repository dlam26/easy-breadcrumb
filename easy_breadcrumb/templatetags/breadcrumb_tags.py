"""
Adds a {% breadcrumb %} template tag!

This module is good for maintaining a navigation breadcrumb 
without duplication / copy & pastage.

"""

import os
from django.template import Context, Library, Node, loader, Template
from django.conf import settings

DEFAULT_BREADCRUMB_LINK_SEPARATOR = u'-|-'
register = Library()                                    # pylint: disable=C0103


class BreadcrumbNode(Node):
    """A breadcrumb inside some ol' template."""
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.crumb = loader.get_template('crumb.html')
        self.link_separator = getattr(settings, 'BREADCRUMB_LINK_SEPARATOR',
                                      DEFAULT_BREADCRUMB_LINK_SEPARATOR)

    def render(self, context):
        output = self.nodelist.render(context)
        lines = output.split(os.linesep)
        breadcrumbed_lines = list()
        for i, line in enumerate(lines):
            line = line.strip()
            if line:
                try:
                    text, href = line.split(self.link_separator)
                except ValueError:  # e.g. "need more than 1 value to unpack"
                    text, href = line, "#"
                text, href = text.strip(),  href.strip()
                crumb_context = Context({"text": text, 'href': href, "i": i})
                breadcrumbed_lines.append(self.crumb.render(crumb_context))

        return ''.join(breadcrumbed_lines)


@register.tag('breadcrumb')
def do_breadcrumb(parser, token):                       # pylint: disable=W0613
    """Generate breadcrumb HTML by iterating over text on separate lines.

    Example:

        {% breadcrumb %}
            Grocery Store
            Bakery
            Cake
        {% endbreadcrumb %}

        ==>
            <li> <a href="">Grocery Store</a> </li>
            - <li> <a href="">Bakery</a> </li>
            - <li> <a href="">Cake </a> </li>

    """
    nodelist = parser.parse(('endbreadcrumb'),)
    parser.delete_first_token()
    return BreadcrumbNode(nodelist)
