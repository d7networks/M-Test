
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from partner.models import Partner



class PartnerCreateView(CreateView):
	model = Partner
	fields = ['company_name', 'email', 'phone', 'account_type', 'company_url', 'address']
	template_name = 'partner/partner_form.html'
	success_url = reverse_lazy('partner:partner_list')


class PartnerListView(TemplateView):
	template_name = 'partner/partner_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['partners'] = Partner.objects.all()
		return context


class PartnerUpdateView(UpdateView):
	model = Partner
	fields = ['company_name', 'email', 'phone', 'account_type', 'company_url', 'address']
	template_name = 'partner/partner_form.html'
	success_url = reverse_lazy('partner:partner_list')


class PartnerDeleteView(DeleteView):
	model = Partner
	template_name = 'partner/partner_confirm_delete.html'
	success_url = reverse_lazy('partner:partner_list')
