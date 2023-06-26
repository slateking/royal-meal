from rest_framework import serializers
from Chinese.models import Chinese
from Drinks.models import Drinks
from Italian.models import Italian
from Japanese.models import Japanese
from Most_popular.models import Most_popular
from New_mexican.models import New_Mexican
from Nigerian.models import Nigerian
from Sushi.models import Sushi
from Sandwiches.models import Sandwiches





class ModelASerializer(serializers.ModelSerializer):
    class Meta:
        model = Chinese
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]

class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]

class ModelCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Italian
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]

class ModelDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Japanese
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]
    
class ModelESerializer(serializers.ModelSerializer):
    class Meta:
        model = Most_popular
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]


class ModelFSerializer(serializers.ModelSerializer):
    class Meta:
        model = New_Mexican
        fields = '__all__'


class ModelGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nigerian
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]



class ModelHSerializer(serializers.ModelSerializer):
    # url = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = Sandwiches
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',

                 
                 ]
    # def get_url(self, obj):
    #    request = self.context.get('request')
    #    if request is None:
    #        return None
    #    return reverse("ch-detail", kwargs={"pk": obj.pk}, request=request)
    
    

    # def validate_name(self, value):
    #     qs = Sandwiche.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    


class ModelISerializer(serializers.ModelSerializer):
    class Meta:
        model = Sushi
        fields =  [ 
                  'id',
                  'name',
                  'description',
                  'price',
                  'discount',
                  'rating',
                  'sale_price',
                  'image',
                #   'url',
                 ]