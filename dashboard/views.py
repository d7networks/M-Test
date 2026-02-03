from django.contrib.auth.models import User
from django.views.generic import TemplateView



class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = User.objects.count()
        context['active_users'] = User.objects.filter(is_active=True).count()
        context['staff_users'] = User.objects.filter(is_staff=True).count()
        context['superusers'] = User.objects.filter(is_superuser=True).count()
        
        return context
