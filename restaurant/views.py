# views.py

# from rest_framework import generics
# from .models import Book
# from .serializers import BookSerializer

# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer






from restaurant.serializers import CategoriesSerializer, FoodItemSerializer
from .models import Category, FoodItem
from rest_framework import generics
from rest_framework.response import Response











class ProductDetailAPIView(generics.RetrieveAPIView):
   queryset = FoodItem.objects.all()
   serializer_class = FoodItemSerializer
 

def list(self, request, *args, **kwargs):
        # Get the serialized data
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = serializer.data

        # Modify the image URL to include the full domain name
        for item in data:
            item['image'] = request.build_absolute_uri(item['image'])
        
        # for item in data:
        #     item['url'] = request.build_absolute_uri(item['url'])

        # Return the modified data as a JSON response
        return Response({'products': data})
rs_detail_view = ProductDetailAPIView.as_view()







# this is to create and list all products (it is better and fast than creating another list class)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
    
    
    
    # if the description is not give then description is = to name of the given item
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None      
        if description is None:
            description = name
        serializer.save(description=description)
    
   
 

    def list(self, request, *args, **kwargs):
        # Get the serialized data
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = serializer.data

        # Modify the image URL to include the full domain name
        for item in data:
            item['image'] = request.build_absolute_uri(item['image'])
        
        # for item in data:
        #     item['url'] = request.build_absolute_uri(item['url'])

        # Return the modified data as a JSON response
        return Response({'products': data})
          
rs_list_create_view = ProductListCreateAPIView.as_view()
    









class ProductPutAPIView(generics.RetrieveUpdateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    lookup_field = 'pk'
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        data = serializer.save()
        if not data.description:
            data.description = data.name
              
Product_put_view = ProductPutAPIView.as_view()











class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
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



class NigeriaListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
Nigeria_List_APIView = NigeriaListAPIView.as_view()