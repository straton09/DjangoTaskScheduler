from django import forms
from .models import Task
import datetime
from django.utils import timezone

class TaskForm(forms.ModelForm):
	exec_datetime = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M','%Y-%m-%d %H:%M'],required=False)
	class Meta:
		model = Task
		fields = ('task_text','exec_datetime','priority' )
		#widgets = {
        #    'exec_datetime': forms.DateTimeInput(attrs={'class':'timepicker'},format=['%Y-%m-%dT%H:%M','%Y-%m-%d %H:%M']),
        #}
	def clean_exec_datetime(self):
		return self.cleaned_data['exec_datetime'] or timezone.now()
		
	def clean(self):
		cleaned_data = super(TaskForm, self).clean()
		exec_datetime = cleaned_data.get("exec_datetime")
		
		if exec_datetime is None:
			exec_datetime = timezone.now()
		
		if exec_datetime <  timezone.now():
			msg = "Cannot set past execution date!"
			self.add_error('exec_datetime', msg)