from rest_framework.reverse import reverse
from rest_framework import serializers
from Sushi.models import Sushi







class SushiSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
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
                  'url',
                 ]
        
        
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("Su-list", kwargs={"pk": obj.pk}, request=request)
    
    

    def validate_name(self, value):
        qs = Sushi.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    







