from django.urls import path
from knox import views as knox_views
from .views import RegView, LoginView, BlogView, DocxView, FAQView, ListView

urlpatterns = [
    path('signup/', RegView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('blog/', BlogView.as_view(), name='blog'),
    path('upload/', DocxView.as_view(), name='upload'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('lists/', ListView.as_view(), name='list'),
    path('FAQ/', FAQView.as_view(), name='FAQ'),
]