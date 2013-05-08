import os
import pdb
from django.template import Context, Library, Node, loader, Template

register = Library()

#  TODO  what about href?  maybe make an arbitary delimeter... like |||||
class BreadcrumbNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.template = loader.get_template('crumb.html')

    def render(self, context):
        output = self.nodelist.render(context)
        lines = output.split(os.linesep)
        breadcrumbed_lines = list()

        for line in lines:
            line = line.strip()
            if line:
                ctx = Context({'href': "#", "txt": line})
                breadcrumbed_lines.append(self.template.render(ctx))

        return ''.join(breadcrumbed_lines)


@register.tag('breadcrumb')
def do_breadcrumb(parser, token):
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

#     pdb.set_trace()

    return BreadcrumbNode(nodelist)
