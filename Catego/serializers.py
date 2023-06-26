from rest_framework.reverse import reverse
from rest_framework import serializers
from Catego.models import Cat


class CategoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = Cat
        fields =  [ 
                  'id',
                  'name',
                  'image',
                  'url',
                 ]
        
        
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("product_list", kwargs={"pk": obj.pk}, request=request)
    
    

    def validate_name(self, value):
        qs = Cat.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    






