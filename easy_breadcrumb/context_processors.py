from templatetags.breadcrumb_tags import DEFAULT_BREADCRUMB_LINK_SEPARATOR

# TODO  - the default can be overriden in settings.py ^

def crumb_separator(request):
    """Puts the easy breadcrumb link separator into the context.

    (yes, it is a very random symbol =D)   -|-

    """
    return {
        'CRUMB_SEPARATOR': DEFAULT_BREADCRUMB_LINK_SEPARATOR,
        'CRUMBSEP': DEFAULT_BREADCRUMB_LINK_SEPARATOR,
        'CS': DEFAULT_BREADCRUMB_LINK_SEPARATOR,
    }
