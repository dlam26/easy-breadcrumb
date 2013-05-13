from templatetags.breadcrumb_tags import DEFAULT_BREADCRUMB_LINK_SEPARATOR

# TODO  - the default can be overriden in settings.py ^

def link_separator(request):
    """Puts the easy breadcrumb link separator into the context.

    (yes, it is a very random symbol =D)   -|-

    """
    return {
        'link_separator': DEFAULT_BREADCRUMB_LINK_SEPARATOR,
        'SEP': DEFAULT_BREADCRUMB_LINK_SEPARATOR,
    }
