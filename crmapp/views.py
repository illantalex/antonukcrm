# from django.shortcuts import render
from .models import Company, Project, Manager, Message
from django.views import generic
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from . import filters
from django_filters.views import FilterView

# Create your views here.


class CompanyListView(generic.ListView):
    model = Company
    paginate_by = 10

    def get_queryset(self):
        return Company.objects.order_by(self.request.GET.get('sort', 'name'))


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 10

    def get_queryset(self):
        return Project.objects.order_by(self.request.GET.get('sort', 'name'))


class MessageListView(FilterView):
    model = Message
    context_object_name = 'message_list'
    template_name = 'message_list'
    filterset_class = filters.MessageFilter
    paginate_by = 10

    def get_queryset(self):
        return Message.objects.order_by(self.request.GET.get('sort', 'name'))


class CompanyDetailView(generic.DetailView):
    model = Company
    paginate_by = 10


class ProjectDetailView(generic.DetailView):
    model = Project
    paginate_by = 10


class MessageDetailView(generic.DetailView):
    model = Message
    paginate_by = 10


class ManagerCabinet(generic.DetailView):
    model = Manager
    # permission_required = 'crmapp.manager.can_view_manager'
    template_name = 'crmapp/manager_page.html'


class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    # fields = '__all__'
    success_url = reverse_lazy('company_list')

    # def get_success_url(self):
    #     return reverse_lazy('manager_page', args=[str(self.pk)])


class CompanyCreate(CreateView):
    model = Company
    fields = '__all__'
    # initial = {}
    success_url = reverse_lazy('company_list')


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name', 'director', 'summary', 'adress', 'email', 'phone']
    success_url = reverse_lazy('company_list')


class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('company_list')


class ProjectCreate(CreateView):
    model = Project
    fields = '__all__'
    # initial = {}
    success_url = reverse_lazy('project_list')


class ProjectUpdate(UpdateView):
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('project_list')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')


class MessageCreate(CreateView):
    model = Message
    fields = '__all__'
    # initial = {'manager': 'user.manager.pk'}
    success_url = reverse_lazy('message_list')


class MessageUpdate(UpdateView):
    model = Message
    fields = ['name', 'project', 'channel', 'description', 'mark', 'kwords']
    success_url = reverse_lazy('message_list')


class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')
