from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('cs640/index.html')
    context = RequestContext(request, {
        'name': 'Ritvik Mayank',
        'student_id': '83113',
        'learnings': ['Fundamentals of Web security',
                      'How to build websites using Django',
                      'The class was very practical and Kranthi is awesome!']})

    return HttpResponse(template.render(context))
