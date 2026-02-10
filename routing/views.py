import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View

from partner.models import Partner
from client.models import Client
from network.models import Country, Network, Connector
from .models import Routing

class RouteListView(View):

    template_name = 'list_routes.html'

    def get(self, request):

        partners = Partner.objects.all()
        routings = Routing.objects.all()
        context = {
            'partners': partners,
            'partner_id': None,
            'routings': routings
        }
        return render(request, self.template_name, context)
    
    def post(self, request):

        partners = Partner.objects.all()
        routings = Routing.objects.all()
        context = {
            'partners': partners
        }
        if request.POST.get('partner'):
            partner_id = request.POST.get('partner')
            clients = Client.objects.filter(partner_id=partner_id)
            context['partner_id'] = int(partner_id)
            context['clients'] = clients
        if request.POST.get('client'):
            client_id = request.POST.get('client')
            routings = routings.filter(client_id=client_id)
            context['client_id'] = int(client_id)
        context['routings'] = routings
        return render(request, self.template_name, context)


class AddRoutingView(View):

    template_name = 'add_routing.html'

    def get(self, request):

        partners = Partner.objects.all()
        contries = Country.objects.all()
        connectors = Connector.objects.all()
        context = {
            'partners': partners,
            'partner_id': None,
            'countries': contries,
            'country_id': None,
            'connectors': connectors
        }
        return render(request, self.template_name, context)
    
    def post(self, request):

        partners = Partner.objects.all()
        contries = Country.objects.all()
        connectors = Connector.objects.all()
        context = {
            'partners': partners,
            'countries': contries,
            'connectors': connectors
        }
        if request.POST.get('partner'):
            partner_id = request.POST.get('partner')
            clients = Client.objects.filter(partner_id=partner_id)
            context['partner_id'] = partner_id
            context['clients'] = clients
        if request.POST.get('country'):
            country_id = request.POST.get('country')
            networks = Network.objects.filter(country_id=country_id)
            context['country_id'] = int(country_id)
            context['networks'] = networks
        if request.POST.get('client'):
            client_id = request.POST.get('client')
            context['client_id'] = int(client_id)
        if request.POST.get('network'):
            network_id = request.POST.get('network')
            context['network_id'] = int(network_id)
        if request.POST.get('connector'):
            connector_id = request.POST.get('connector')
            context['connector_id'] = int(connector_id)
        if request.POST.get('is_submit') == 'submitted':
            Routing.objects.create(
                network_id=network_id,
                connector_id=connector_id,
                ratio=request.POST.get('ratio'),
                client_id=client_id

            )
            print("Added route")
        return render(request, self.template_name, context)
    
class ReloadInstance(View):

    def post(self, request):

        routings = Routing.objects.filter(conf_added=False)
        for route in routings:
            service = route.client.name
            receiver_regex = route.network.number_matching
            smsc_id = route.connector.name
            ratio = route.ratio
            file_name = f'routing_{service}.conf'
            file_path = os.path.join(settings.BASE_DIR / file_name)
            data = (
                f"service = {service}\n"
                f"receiver-regex = {receiver_regex}\n"
                f"smsc-id = {smsc_id}\n"
                f"ratio = {ratio}\n"
            )
            existing_data = ''
            try:
                with open(file_path, 'r') as f:
                    existing_data = f.read()
            except:
                pass
            existing_data += data
            with open(file_path, 'w') as f:
                f.write(existing_data)
            route.conf_added = True
            route.save()
        return redirect('RouteListView')