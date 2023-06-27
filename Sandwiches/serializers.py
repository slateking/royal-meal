from rest_framework.reverse import reverse
from rest_framework import serializers
from Sandwiches.models import Sandwiches











class SandwichesSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
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
                  'url',
                 ]
        
        
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("SW-list", kwargs={"pk": obj.pk}, request=request)
    
    

    def validate_name(self, value):
        qs = Sandwiches.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    






