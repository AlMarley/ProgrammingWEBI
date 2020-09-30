from django.urls import path

from . import views


urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('<int:pk>', views.DetailView.as_view(), name='detail'),
     path('<int:question_id>/vote/', views.VoteView.as_view(), name='vote'),

     path('<int:pk>/mvts/', views.MvotosView.as_view(), name='mvotos'),
     path('<int:question_id>/result', views.MMvotosView.as_view(), name='votemm'),
     path('sobre', views.SobreView.as_view(), name='sobre'),


]