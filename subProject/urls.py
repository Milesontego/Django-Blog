from django.urls import path
from . import views
urlpatterns = [
  path('', views.Home, name='home'),
  path('contact/', views.Contact, name='contact'),
  path('post/', views.PostListView.as_view(), name='post'),
  path('post/<int:post_id>', views.Details, name="detail")
]