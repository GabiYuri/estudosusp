from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'locais'
urlpatterns = [
    path('', views.LocalListView.as_view(), name='index'),
    path('<int:pk>/', views.LocalDetailView.as_view(), name='detail'),
    path('create/', views.create_local, name='create'),
    path('update/<int:local_id>/', views.update_local, name='update'),
    path('rate/<int:local_id>/', views.rate_local, name='rate'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('create_list/', views.ListCreateView.as_view(), name='create_list'),
    path('detail_list/<int:list_id>/', views.detail_list, name='detail_list'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)