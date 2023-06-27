from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Most_popular import Most_popular_views





urlpatterns = [

    path('<int:pk>/', Most_popular_views.Most_detail_view, name='Most-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Most_popular_views.Most_list_create_view, ),
    path('<int:pk>/update/', Most_popular_views.Most_put_view),
    path('<int:pk>/delete/', Most_popular_views.Most_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
