# Create your views here.
from rest_framework import generics

from Most_popular.models import Most_popular
from Most_popular.serializers import Most_popular_Serializer

from rest_framework.response import Response











class ProductDetailAPIView(generics.RetrieveAPIView):
   queryset = Most_popular.objects.all()
   serializer_class = Most_popular_Serializer
 

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
Most_detail_view = ProductDetailAPIView.as_view()







# this is to create and list all products (it is better and fast than creating another list class)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Most_popular.objects.all()
    serializer_class = Most_popular_Serializer
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
          
Most_list_create_view = ProductListCreateAPIView.as_view()
    









class ProductPutAPIView(generics.RetrieveUpdateAPIView):
    queryset = Most_popular.objects.all()
    serializer_class = Most_popular_Serializer
    lookup_field = 'pk'
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_update(self, serializer):
        data = serializer.save()
        if not data.description:
            data.description = data.name
              
Most_put_view = ProductPutAPIView.as_view()











class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Most_popular.objects.all()
    serializer_class = Most_popular_Serializer
    lookup_field = 'pk'
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_destroy(self, data):
        super().perform_destroy(data)
    
Most_delete_view = ProductDeleteAPIView.as_view()



















