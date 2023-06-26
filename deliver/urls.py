"""deliver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from customer.views import Index, About, Order, OrderConfirmation, OrderPayConfirmation


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('order/', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),name='payment-confirmation'),
    
    path('api/popular', include('customer.urls')),
    path('best/', include('Search.urls')),
    path('api/auth/', include('authentication.urls')),
    path('cat/', include('Catego.urls')),
    path('api/all/', include('All.urls')),
    path('api/food/', include('restaurant.urls')),
    path('api/products/ch/', include('Chinese.urls')),
    path('api/products/dr/', include('Drinks.urls')),
    path('api/products/it/', include('Italian.urls')),
    path('api/products/jp/', include('Japanese.urls')),
    path('api/products/most/', include('Most_popular.urls')),
    path('api/products/mex/', include('New_mexican.urls')),
    path('api/products/ng/', include('Nigerian.urls')),
    path('api/products/sw/', include('Sandwiches.urls')),
    path('api/products/su/', include('Sushi.urls')),

        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
