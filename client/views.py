from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from client.models import Client



class ClientCreateView(CreateView):
	model = Client
	fields = ['partner', 'instance', 'user_name', 'password', 'default_smsc']
	template_name = 'client/client_form.html'
	success_url = reverse_lazy('client:client_list')


class ClientListView(TemplateView):
	template_name = 'client/client_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['clients'] = Client.objects.all()
		return context


class ClientUpdateView(UpdateView):
	model = Client
	fields = ['partner', 'instance', 'user_name', 'password', 'default_smsc']
	template_name = 'client/client_form.html'
	success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
	model = Client
	template_name = 'client/client_confirm_delete.html'
	success_url = reverse_lazy('client:client_list')
