from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from customer import views1





urlpatterns = [

    path('<int:pk>/', views1.Product_detail_view, name='product-detail'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path('', views1.Product_list_create_view, name='product-list'),
    path('<int:pk>/update/', views1.Product_put_view),
    path('<int:pk>/delete/', views1.Product_delete_view),
    path('cat/', views1.Categories_List_APIView),
    path('cat/<int:pk>/', views1.Categories_Detail_APIView),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)