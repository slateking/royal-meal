from rest_framework.reverse import reverse
from rest_framework import serializers
from Chinese.models import Chinese


class ChineseSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
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
                  'url',
                 ]
        
        
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("ch-list", kwargs={"pk": obj.pk}, request=request)
    
    

    def validate_name(self, value):
        qs = Chinese.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    


