from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import generics
from Catego.models import Cat
from Catego.serializers import CategoSerializer
from rest_framework.response import Response




class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CategoSerializer
    # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
cat_detail_view = ProductDetailAPIView.as_view()







# this is to create and list all products (it is better and fast than creating another list class)
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CategoSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
    
    
    
    # if the description is not give then description is = to name of the given item
    
    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None      
        if description is None:
            description = name
        serializer.save(description=description)
          
cat_list_create_view = ProductListCreateAPIView.as_view()
    









# class ProductPutAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CategoSerializer
#     lookup_field = 'pk'
#     # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
#     # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
#     def perform_update(self, serializer):
#         data = serializer.save()
#         if not data.description:
#             data.description = data.name
              
# cat_put_view = ProductPutAPIView.as_view()











# class ProductDeleteAPIView(generics.DestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CategoSerializer
#     lookup_field = 'pk'
#     # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
#     # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
#     def perform_destroy(self, data):
#         super().perform_destroy(data)
    
# cat_delete_view = ProductDeleteAPIView.as_view()














# this is to create and list all products (it is better and fast than creating another list class)
# class AllApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         serializer_class = Cat.objects.all()
#         model_a_serializer = CategoSerializer(serializer_class, many = True)
     
#         data = {
#             'products': model_a_serializer.data,
#          }
        
#         # data = model_a_serializer + model_b_serializer + model_c_serializer.data + model_d_serializer.data + model_e_serializer.data + model_f_serializer.data + model_g_serializer.data + model_h_serializer.data + model_i_serializer.data
#         return Response(data)
   
# Catego_view = AllApiView.as_view()




# def products(request):
#     products = Cat.objects.all()
#     data = {"products": list(products.values())}
#     return JsonResponse(data)






class ProductListView(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CategoSerializer
 

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





class ProductJustList(generics.RetrieveAPIView):
    queryset = Cat.objects.all()
    serializer_class = CategoSerializer
 

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
