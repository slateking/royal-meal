from rest_framework.views import APIView
from rest_framework.response import Response
from Chinese.models import Chinese
from Drinks.models import Drinks
from Italian.models import Italian
from Japanese.models import Japanese
from Most_popular.models import Most_popular
from New_mexican.models import New_Mexican
from Nigerian.models import Nigerian
from Sandwiches.models import Sandwiches
from Sushi.models import Sushi
from All.serilizer import ModelASerializer, ModelBSerializer, ModelCSerializer,ModelDSerializer,ModelESerializer,ModelFSerializer,ModelGSerializer,ModelHSerializer,ModelISerializer




class AllApiView(APIView):
    def get(self, request, *args, **kwargs):
        model_a_instances = Chinese.objects.all()
        model_a_serializer = ModelASerializer(model_a_instances, many=True)
        model_b_instances = Drinks.objects.all()
        model_b_serializer = ModelBSerializer(model_b_instances, many=True)
        model_c_instances = Italian.objects.all()
        model_c_serializer = ModelCSerializer(model_c_instances, many=True)
        model_d_instances = Japanese.objects.all()
        model_d_serializer = ModelDSerializer(model_d_instances, many=True)
        model_e_instances = Most_popular.objects.all()
        model_e_serializer = ModelESerializer(model_e_instances, many=True)
        model_f_instances = New_Mexican.objects.all()
        model_f_serializer = ModelFSerializer(model_f_instances, many=True)
        model_g_instances = Nigerian.objects.all()
        model_g_serializer = ModelGSerializer(model_g_instances, many=True)
        model_h_instances = Sandwiches.objects.all()
        model_h_serializer = ModelHSerializer(model_h_instances, many=True)
        model_i_instances = Sushi.objects.all()
        model_i_serializer = ModelISerializer(model_i_instances, many=True)
        data = {
            'modelA': model_a_serializer.data + model_b_serializer.data + model_c_serializer.data + model_d_serializer.data + model_e_serializer.data + model_f_serializer.data + model_g_serializer.data + model_h_serializer.data + model_i_serializer.data,
            # 'modelB': model_b_serializer.data,
            # 'modelC': model_c_serializer.data,
            # 'modelD': model_d_serializer.data,
            # 'modelE': model_e_serializer.data,
            # 'modelF': model_f_serializer.data,
            # 'modelG': model_g_serializer.data,
            # 'modelH': model_h_serializer.data,
            # 'modelI': model_i_serializer.data,
         }
        
        # data = model_a_serializer + model_b_serializer + model_c_serializer.data + model_d_serializer.data + model_e_serializer.data + model_f_serializer.data + model_g_serializer.data + model_h_serializer.data + model_i_serializer.data
        return Response(data)
   



# class AllApiView2(generics.RetrieveAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CategoSerializer
#     # authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission, permissions.IsAuthenticatedOrReadOnly]
# cat_detail_view = ProductDetailAPIView.as_view()