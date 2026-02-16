from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from client.models import Client
from django.urls import reverse_lazy
from client.forms import ClientCreateForm

class ClientListView(TemplateView):
	template_name = 'client/client_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['client'] = Client.objects.all()
		return context

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client:client_list')


class ClientUpdateView(UpdateView):
	model = Client
	fields = ['client_name', 'partner', 'instance', 'method']
	template_name = 'client/client_form.html'
	success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
	model = Client
	template_name = 'client/client_confirm_delete.html'
	success_url = reverse_lazy('client:client_list')
