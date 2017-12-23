# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.shortcuts import render,redirect,get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from .models import Task
from .forms import TaskForm

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
	
def task_list(request):
	tasks = Task.objects.filter(done=False).order_by('exec_datetime','-priority')
	return render(request, 'task_list.html', {'task_list': tasks})

def task_create(request):
	form = TaskForm(request.POST or None)
	context = {'form': form}
	if request.method == 'POST' and form.is_valid():
		form.save()
		return JsonResponse({'success': 1})
		
	html_form = render_to_string('partial_task_create.html',context,request=request)
	return JsonResponse({'html_form': html_form})

def task_delete(request, id):
	task = get_object_or_404(Task, id=id)
	task.delete()
	return JsonResponse({'success': 1})
	
	
