from django import forms
from .models import Routing, RoutingConnector

class RoutingCreateForm(forms.ModelForm):
    class Meta:
        model = Routing
        fields = ['client', 'partner', 'country', 'network']


RoutingConnectorFormSet = forms.inlineformset_factory(
    Routing, 
    RoutingConnector, 
    fields=['connector', 'percentage'], 
    extra=1,
    can_delete=True
)