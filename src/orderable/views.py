from django.views.generic.simple import direct_to_template

def javascript(request):
    """
    Return the orderable JavaScript file.
    
    This view is necessary to be able to reference the JavaScript as a Django
    routed URL.
    """
    return direct_to_template(
        request = request,
        template = 'orderable/orderable.js',
    )