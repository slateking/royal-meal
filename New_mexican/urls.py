from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from New_mexican import New_Mexican_views






urlpatterns = [

    path('<int:pk>/', New_Mexican_views.New_detail_view, name='new-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', New_Mexican_views.New_list_create_view, ),
    path('<int:pk>/update/', New_Mexican_views.Nm_put_view),
    path('<int:pk>/delete/', New_Mexican_views.Nm_delete_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

