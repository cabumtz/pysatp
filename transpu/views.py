# -*- coding: utf-8 -*-

from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# from demo.forms import *

# from demo.models import *

# Create your views here.

def index(request):
	#return render_to_response('index.html', context_instance=RequestContext(request,{'libros': libros}))
	return render_to_response('index.html', context_instance=RequestContext(request,{}))


def choferes(request):
	pass


