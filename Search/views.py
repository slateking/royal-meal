from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ModelA,ModelB,ModelC
from Nigerian.models import Nigerian
from Chinese.models import Chinese
from Italian.models import Italian
from .serilize import ModelASerializer,ModelBSerializer,ModelCSerializer

# class MyAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         model_a_instances = ModelA.objects.all()
#         model_a_serializer = ModelASerializer(model_a_instances, many=True)
#         model_b_instances = ModelB.objects.all()
#         model_b_serializer = ModelBSerializer(model_b_instances, many=True)
#         model_c_instances = ModelC.objects.all()
#         model_c_serializer = ModelCSerializer(model_c_instances, many=True)
#         data = {
#             'modelA': model_a_serializer.data,
#             'modelB': model_b_serializer.data,
#             'modelC': model_c_serializer.data,
#         }
#         return Response(data)



@api_view(['GET'])
def search(request):
    query = request.GET.get('q')
    
    results1 = Nigerian.objects.filter(name__icontains=query,description__icontains=query,) if query else Nigerian.objects.none() 
      
    results2 = Chinese.objects.filter(name__icontains=query,description__icontains=query,)
    results3 = Italian.objects.filter(name__icontains=query,description__icontains=query,)
    data = {
        'results1': results1,
        'results2': results2,
        'results3': results3,
    }
    return Response(data)