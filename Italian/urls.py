from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Italian import Italian_views



urlpatterns = [

    path('<int:pk>/', Italian_views.It_detail_view, name='it-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Italian_views.It_list_create_view, ),
    path('<int:pk>/update/', Italian_views.It_put_view),
    path('<int:pk>/delete/', Italian_views.It_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
