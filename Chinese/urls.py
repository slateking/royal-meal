from django.urls import path

from Chinese import Chinese_views






urlpatterns = [

    path('<int:pk>/', Chinese_views.ch_detail_view, name='ch-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', Chinese_views.ch_list_create_view, ),
    path('<int:pk>/update/', Chinese_views.ch_put_view),
    path('<int:pk>/delete/', Chinese_views.ch_delete_view),
] 