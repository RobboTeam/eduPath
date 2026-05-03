from django.contrib import admin
from django.urls import path
from eduPathApp.views import UserRegView, MaterialListView, UserAuthenticateView, MaterialDetailView, UserLogoutView, MaterialCreateView, MaterialUpdateView, SubjectListAPIView, MaterialListAPIView

urlpatterns = [
    path('', MaterialListView.as_view()),
    path('material/edit/<int:pk>', MaterialUpdateView.as_view()),
    path('material/<int:pk>', MaterialDetailView.as_view()),
    path('create/', MaterialCreateView.as_view()),
    path('login/', UserAuthenticateView.as_view()),
    path('registration/', UserRegView.as_view()),
    path('logout', UserLogoutView.as_view()),
    path('api/subjects/', SubjectListAPIView.as_view()),
    path('api/materials/', MaterialListAPIView.as_view()),
    path('admin/', admin.site.urls),
]
