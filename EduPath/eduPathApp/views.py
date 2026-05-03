from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import UserReg, UserAuthentication
from .models import Material
from .models import Subject, Material
from .serializers import SubjectSerializer, MaterialSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

class UserRegView(View):
  def get(self, request:HttpRequest) -> HttpResponse:
    form = UserReg()
    return render(request, 'auth.html', context={"page_name":"Registration", "btn_name": "Register", "form": form, 'is_login': False})
  
  def post(self, request:HttpRequest) -> HttpResponse:
    form = UserReg(request.POST)
    if form.is_valid():
      user = User.objects.create_user(**form.cleaned_data)
      user.is_active = True
      print(f"--- Registration Successful: {user.username} ---")            
      messages.success(request, f"Registration complete for {user.username}! Please log in.")
      user.save()
      return HttpResponseRedirect('/login/')
    return HttpResponseRedirect('/')
  
class UserAuthenticateView(View):
  def get(self, request:HttpRequest) -> HttpResponse:
    form = UserAuthentication()
    return render(request, "auth.html", context={"page_name": "Login", "btn_name":"login", "form": form, 'is_login': True})
  
  def post(self, request:HttpRequest) -> HttpResponse:
    form = UserAuthentication(request.POST)
    if form.is_valid():
      user = authenticate(request, **form.cleaned_data)
      if user:
        login(request, user)
        return HttpResponseRedirect("/")
    return render(request, "auth.html", context={"page_name": "Login", "btn_name":"login", "form": form, 'is_login': True})
      
class UserLogoutView(View):
  def get(self, request:HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
      logout(request)
    return HttpResponseRedirect("/login/")
  
class MaterialListView(LoginRequiredMixin, ListView):
  template_name = 'main.html'
  model = Material
  login_url = '/login/'
  def get_queryset(self):
    return Material.objects.filter(currentUser=self.request.user)

class MaterialDetailView(DetailView):
  template_name = 'detail.html'
  model = Material

class MaterialCreateView(CreateView):
  template_name = 'index.html'
  model = Material
  success_url = '/'
  fields = ['subject', 'title', 'file']
  def form_valid(self, form):
    form.instance.currentUser = self.request.user
    return super().form_valid(form)
  
class MaterialUpdateView(UpdateView):
  template_name = 'index.html'
  model = Material
  success_url = '/'
  fields = ['subject', 'title', 'file']


# class SubjectListAPIView(APIView):
#   def get(self, request):
#     subjects = Subject.objects.all()
#     serializer = SubjectSerializer(subjects, many=True)
#     return Response(serializer.data)

# class MaterialListAPIView(APIView):
#   def get(self, request):
#     materials = Material.objects.all()
#     serializer = MaterialSerializer(materials, many=True)
#     return Response(serializer.data)

#   def post(self, request):
#     serializer = MaterialSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save(currentUser=request.user)
#       return Response(serializer.data)
#     return Response(serializer.errors)
