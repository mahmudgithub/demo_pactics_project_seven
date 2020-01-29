from django.views.generic import ListView
from .models import Venue
class sos(ListView):
	model = Venue
	template_name = 'home.html'
	context_object_name='app1'