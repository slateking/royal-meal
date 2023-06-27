from rest_framework.reverse import reverse
from rest_framework import serializers
from Most_popular.models import Most_popular







class Most_popular_Serializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
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
                  'url',
                 ]
        
        
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("Most-list", kwargs={"pk": obj.pk}, request=request)
    
    

    def validate_name(self, value):
        qs = Most_popular.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    
