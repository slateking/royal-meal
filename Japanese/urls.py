from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Japanese import Japanese_views




urlpatterns = [

    path('<int:pk>/', Japanese_views.Jp_detail_view, name='jp-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Japanese_views.Jp_list_create_view, ),
    path('<int:pk>/update/', Japanese_views.Jp_put_view),
    path('<int:pk>/delete/', Japanese_views.Jp_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
