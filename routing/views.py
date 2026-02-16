from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from routing.models import Routers



class ClientCreateView(CreateView):
	model = Routers
	fields = ['partner', 'client', 'country', 'network', 'connector', 'connector_range']
	template_name = 'routing/routing_form.html'
	success_url = reverse_lazy('routing:routing_list')


class ClientListView(TemplateView):
	template_name = 'routing/routing_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['routers'] = Routers.objects.all()
		return context


class ClientUpdateView(UpdateView):
	model = Routers
	fields = ['partner', 'client', 'country', 'network', 'connector', 'connector_range']
	template_name = 'routing/routing_form.html'
	success_url = reverse_lazy('routing:routing_list')


class ClientDeleteView(DeleteView):
	model = Routers
	template_name = 'routing/routing_confirm_delete.html'
	success_url = reverse_lazy('routing:routing_list')
