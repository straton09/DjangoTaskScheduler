from django.core.management.base import BaseCommand, CommandError
import sched, time
from tasks.models import Task
import datetime
import logging

class Command(BaseCommand):
	help = 'Executes tasks that were scheduled'
	
	def __init__(self):
		BaseCommand.__init__(self)
		self.logfile = open('tasks_run.log','a+')

	def handle(self,*args,**kwargs):
		s = sched.scheduler(time.time, time.sleep)
		def do_cron_job(sc,): 
			print "Doing stuff..."    
			self.run_tasks()
			s.enter(60, 1, do_cron_job, (sc,))

		s.enter(60, 1, do_cron_job, (s,))
		s.run()
		
		self.logfile.close()
			
	def run_tasks(self):
		tasks = Task.objects.filter(done=False, exec_datetime__lte=datetime.datetime.now()).order_by('exec_datetime','-priority')
		for task in tasks:
			output = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' Estimated:'+task.exec_datetime.strftime("%Y-%m-%d %H:%M")+' '+task.task_text
			self.logfile.write(output+'\r\n')
			self.stdout.write(output)
			#mark task as done
			task.done = 1
			task.save()
		self.logfile.flush()
			
