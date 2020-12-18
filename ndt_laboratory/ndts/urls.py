from django.urls import path
from ndt_laboratory.ndts import views
from ndt_laboratory.ndts.views import DeleteNdtView, UpdateNdtView

urlpatterns = [
    path('', views.NdtsListView.as_view(), name='ndts list'),
    path('<int:pk>/<slug:slug>/', views.NdtDetailsView.as_view(), name='ndt details'),
    path('create/', views.CreateNdtView.as_view(), name='create ndt'),
    path('edit/<int:pk>/', UpdateNdtView.as_view(), name='edit ndt'),
    path('delete/<int:pk>/', DeleteNdtView.as_view(), name='delete ndt'),
]
