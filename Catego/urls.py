from django.urls import path

from Catego import views






urlpatterns = [

    # path('<int:pk>/', views.cat_detail_view, name='cat_list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    # path('', views.cat_list_create_view,),
    # path('', views.Catego_view),
    # path('', views.products, name='products'),
    path('', views.ProductListView.as_view()),
    path('<int:pk>/', views.ProductJustList.as_view(), name='product_list'),

    # path('<int:pk>/delete/', views.ch_delete_view),
] 