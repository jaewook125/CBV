from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class GreetingView(View):
	message = "good day"
	def get(self, *args, **kwargs):
		return HttpResponse(self.message)

greeting = GreetingView.as_view()

class MorningGreetingView(GreetingView):
	message = 'morning to ya'

morning_greeting = MorningGreetingView.as_view()

evening_greeting = GreetingView.as_view(message='eveing to ya')