from django.contrib.auth.models import User
from django.views.generic import TemplateView



class UserListView(TemplateView):
    template_name = 'users/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all().order_by('-date_joined')
        return context
