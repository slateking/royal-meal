from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Drinks import Drinks_views





urlpatterns = [

    path('<int:pk>/', Drinks_views.dr_detail_view, name='dr-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Drinks_views.dr_list_create_view, ),
    path('<int:pk>/update/', Drinks_views.dr_put_view),
    path('<int:pk>/delete/', Drinks_views.dr_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)