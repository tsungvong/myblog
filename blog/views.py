from django.shortcuts import render
from blog.models import blogspost
import json
from django.http import HttpResponse 

# Create your views here.

def blog_index(request):
	blog_list= blogspost.objects.all()
	return render(request,'index.html',{'blog_list':blog_list})


def api(request):
    print('get into wordcut')
    dct = {
            'fake': 'test',
            'GET': request.GET,
            'POST': request.POST,
            'body': request.body,
            }
    try:
        dct['json_parsed_body'] = json.loads(request.body)
    except Exception as e:
        print('json loads except:{}'.format(e))
    return HttpResponse(HttpResponse(dct), content_type='application/json')