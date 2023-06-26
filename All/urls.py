from django.urls import path

from All import views






urlpatterns = [

     path('', views.AllApiView.as_view()),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
 
] 