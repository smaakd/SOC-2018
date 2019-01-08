import json

from django.http import HttpResponse


def fresh(request):
    return HttpResponse(json.dumps({'fresh': False}), mimetype='application/json')

