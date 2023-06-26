from customer.serializers import CategoriesSerializer, MenuItemSerializer
from .models import Category, MenuItem
from rest_framework import generics












class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
Product_detail_view = ProductDetailAPIView.as_view()







# this is to create and list all products (it is better and fast than creating another list class)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
    
    
    
    # if the description is not give then description is = to name of the given item
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None      
        if description is None:
            description = name
        serializer.save(description=description)
          
Product_list_create_view = ProductListCreateAPIView.as_view()
    









class ProductPutAPIView(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'pk'
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        data = serializer.save()
        if not data.description:
            data.description = data.name
              
Product_put_view = ProductPutAPIView.as_view()











class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    lookup_field = 'pk'
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_destroy(self, data):
        super().perform_destroy(data)
    
Product_delete_view = ProductDeleteAPIView.as_view()




















class CategoriesListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
Categories_List_APIView = CategoriesListAPIView.as_view()



class CategoriesDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
Categories_Detail_APIView = CategoriesDetailAPIView.as_view()

