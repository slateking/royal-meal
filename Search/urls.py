
from django.conf.urls.static import static
from django.urls import path
from Search import views






urlpatterns = [

    path('', views.search),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
 
] 