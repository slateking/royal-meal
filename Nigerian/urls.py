from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Nigerian import NIGERIAN_views






urlpatterns = [

    path('<int:pk>/', NIGERIAN_views.Ng_detail_view, name='Ng-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', NIGERIAN_views.Ng_list_create_view, ),
    path('<int:pk>/update/', NIGERIAN_views.Ng_put_view),
    path('<int:pk>/delete/', NIGERIAN_views.Ng_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
