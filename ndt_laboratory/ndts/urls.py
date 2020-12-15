from django.urls import path
from ndt_laboratory.ndts import views

urlpatterns = [
    path('', views.NdtsListView.as_view(), name='ndts list'),
    # path('<int:pk>/', views.NdtDetailsView.as_view(), name='ndt details'),
    path('<int:pk>/<slug:slug>/', views.NdtDetailsView.as_view(), name='ndt details'),
    path('create/', views.CreateBlogView.as_view(), name='create ndt'),
]
