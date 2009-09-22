import re
from django.contrib.auth.decorators import user_passes_test
from django.db.models import get_model
from django.http import Http404, HttpResponse
from django.views.generic.simple import direct_to_template

def is_staff(user):
    if user.is_staff:
        return True
    return False

@user_passes_test(is_staff)
def order_objects(request):
    if request.method != "POST" or not request.is_ajax():
        raise Http404
    
    model = get_model(request.POST['app_label'], request.POST['model_name'])
    
    ordering_regex = re.compile(r'^order-(?P<object_id>[\d]+)$')
    for (key, order) in request.POST.iteritems():
        matches = ordering_regex.match(key)
        try:
            obj_id = matches.group('object_id')
            obj = model.objects.get(id__exact=obj_id)
            obj.order = order
            obj.save()
        except AttributeError:
            pass
            
    return HttpResponse(None)

@user_passes_test(is_staff)
def get_orderable_javascript(request):
    return direct_to_template(
        request = request,
        template = 'orderable/orderable.js',
    )