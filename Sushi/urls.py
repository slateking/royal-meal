from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Sushi import Sushi_views





urlpatterns = [

    path('<int:pk>/', Sushi_views.Su_detail_view, name='Su-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Sushi_views.Su_list_create_view, ),
    path('<int:pk>/update/', Sushi_views.Su_put_view),
    path('<int:pk>/delete/', Sushi_views.Su_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
