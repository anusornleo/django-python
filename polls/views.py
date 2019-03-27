from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    poll_list = [
        {'id':1,'name':'Anusorn'},
        {'id':2,'name':'Mennkred'},
        {'id':3,'name':'Leo'}
    ]
    context = {
        'page_title':'Wellcome poll pahe',
        'poll_list':poll_list
    }
    return render(request,template_name='polls/index.html',context=context)

def detail(request , poll_id):
    return HttpResponse("detail page %s." % (str(poll_id)))
