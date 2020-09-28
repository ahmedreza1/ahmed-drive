import requests
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from ahmed_drive.models import Folder, Fileshare
from . import models
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http.response import HttpResponseRedirect

#### Normal Pages Related Views ####

class HomeView(TemplateView):
	template_name = "ahmed_drive/home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		if user.is_authenticated:
			home_folders = Folder.objects.filter(created_by_id=user).order_by('-cr_date')
			home_files = Fileshare.objects.filter(uploaded_by_id=user).order_by('-id')
			context['home_folders'] = home_folders
			context['home_files'] = home_files
			return context


#### Pages Related Folder Model ####

@method_decorator(login_required, name="dispatch")    
class FolderCreate(CreateView):
    model = Folder
    fields = ["name", "parent"]
    def form_valid(self, form):
    	self.object = form.save()
    	self.object.created_by = self.request.user
    	self.object.save()
    	return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch") 
class FolderListView(ListView):
	model = Folder
	def get_queryset(self):
		si = self.request.GET.get("si")
		if si == None:
			si = ""
		folderList = Folder.objects.filter(Q(name__icontains = si)).order_by("-id");
		return folderList
@method_decorator(login_required, name="dispatch") 
class FolderDetailView(DetailView):
	model = Folder
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		folder_subfolder = Folder.objects.filter(parent_id=self.kwargs['pk']).order_by('-id')
		folder_file = Fileshare.objects.filter(folder_id=self.kwargs['pk']).order_by('-id')
		context['folder_subfolder'] = folder_subfolder
		context['folder_file'] = folder_file
		return context



#### Pages Related Fileshare Model ####
@method_decorator(login_required, name="dispatch")    
class FileshareCreate(CreateView):
    model = Fileshare
    fields = ["fileupload", "folder"]
    def form_valid(self, form):
    	self.object = form.save()
    	self.object.uploaded_by = self.request.user
    	self.object.save()
    	return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch") 
class FileshareListView(ListView):
	model = Fileshare
	def get_queryset(self):
		si = self.request.GET.get("si")
		if si == None:
			si = ""
		fileshareList = Fileshare.objects.order_by("-id");
		return fileshareList