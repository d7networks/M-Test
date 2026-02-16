from django.shortcuts import render, redirect
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from routing.models import Client
from routing.forms import RoutingCreateForm, RoutingConnectorFormSet
from routing.models import Routing
from django.urls import reverse_lazy
import os
from django.conf import settings
import json
from django.http import HttpResponse
from datetime import datetime, timedelta

class RoutingListView(TemplateView):
	template_name = 'routing/routing_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['routing'] = Routing.objects.all()
		return context


class RoutingDeleteView(DeleteView):
	model = Routing
	template_name = 'routing/routing_confirm_delete.html'
	success_url = reverse_lazy('routing:routing_list')


def create_routing(request):
    if request.method == "POST":
        form = RoutingCreateForm(request.POST)
        formset = RoutingConnectorFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            routing = form.save()
            formset.instance = routing
            formset.save()
            # creating routing configurations
            create_individual_conf(form)
            return redirect('routing:routing_list')
    else:
        form = RoutingCreateForm()
        formset = RoutingConnectorFormSet()
    
    return render(request, 'routing/routing_form.html', {'form': form, 'formset': formset})


def reload_instance(request):
    routes = Routing.objects.all()
    for i in routes:
        create_conf(i)
    return redirect('routing:routing_list') 


def create_conf(route):
    now = datetime.now()
    custom_data = {
        "network": route.network.name,
        "country": route.country.name,
        "host" : route.client.method.host,
        "port" : route.client.method.port,
        "username" : route.client.method.username,
        "key" : route.client.method.key,
        "timestamp": now.isoformat(),
    }
    file_path = os.path.join(settings.MEDIA_ROOT, 'data', 'gateway.conf')
    if file_path:
        with open(file_path, 'r') as file:
            data = json.load(file)
            keys = data['timestamp']
            current_time = datetime.now() 
            dt1 = datetime.fromisoformat(keys)
            time_difference = abs(current_time - dt1)
            threshold = timedelta(minutes=5)
            #just skipped instead of scheduling
            if time_difference < threshold:
                return redirect('routing:routing_list') 

            
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, 'w') as json_file:
            json.dump(custom_data, json_file, indent=4)
        
        message = f"Successfully wrote data to {file_path}"
        return redirect('routing:routing_list') 

    except IOError as e:
        error_message = f"Error writing to file: {e}"
        return HttpResponse(error_message, status=500)



def reload_instance(request):
    routes = Routing.objects.all()
    for i in routes:
        create_conf(i)
    return redirect('routing:routing_list') 



def create_individual_conf(form):
    partner_name = form.cleaned_data['partner']
    client_name = form.cleaned_data['client']

    network = form.cleaned_data['network']
    country = form.cleaned_data['country']
    custom_data = {
        "network": network.name,
        "country": country.name,
    }

    file_name = f'routing_{partner_name}_{client_name}.conf'
    file_path = os.path.join(settings.MEDIA_ROOT, 'data','routes', file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, 'w') as json_file:
            json.dump(custom_data, json_file, indent=4)
        
        message = f"Successfully wrote data to {file_path}"
        return redirect('routing:routing_list') 

    except IOError as e:
        error_message = f"Error writing to file: {e}"
        return HttpResponse(error_message, status=500)

        field_value = form.cleaned_data.get('field_name')