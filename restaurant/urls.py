# urls.py

# from django.urls import path
# from .views import BookList

# urlpatterns = [
#     path('', BookList.as_view(), name='book-list'),
# ]






from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from restaurant import views





urlpatterns = [

    path('<int:pk>/', views.rs_detail_view, name='rs-list'),  #or u use views.ProductDetailAPIView.as_view() remember this bracket ()
    path( '', views.rs_list_create_view, ),
    path('<int:pk>/update/', views.Product_put_view),
    path('<int:pk>/delete/', views.Product_delete_view),
    path('cat/', views.Categories_List_APIView),
    path('cate/', views.Nigeria_List_APIView),
    path('cat/<int:pk>/', views.Categories_Detail_APIView),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)