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
	context = {
		'topMenu': {
			'home': {
				'class': 'active'
			},
			'entidades': {
				'class': ''
			}
		}
	}

	return render_to_response('index.html', context_instance=RequestContext(request,context))


def entidades(request):
	
	context = {
		'topMenu': {
			'home': {
				'class': ''
			},
			'entidades': {
				'class': 'active'
			}
		}
	}

	return render_to_response('entidades.html', context_instance=RequestContext(request, context) )


def evaluacion(request):
	return render_to_response('evaluacion.html', context_instance=RequestContext(request,{}) )


def reportes(request):
	return render_to_response('reportes.html', context_instance=RequestContext(request,{}) )


def choferes(request):
	pass


