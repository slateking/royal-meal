from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Sandwiches import Sandwiches_views






urlpatterns = [

    path('<int:pk>/', Sandwiches_views.SW_detail_view, name='SW-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Sandwiches_views.SW_list_create_view, ),
    path('<int:pk>/update/', Sandwiches_views.Sw_put_view),
    path('<int:pk>/delete/', Sandwiches_views.Sw_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



