from rest_framework.reverse import reverse
from rest_framework import serializers
from customer.models import Category, MenuItem



class MenuItemSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
    class Meta:
        model = MenuItem
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
       return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

    def validate_name(self, value):
        qs = MenuItem.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    


class CategoriesSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
    food_items = MenuItemSerializer(many=True, read_only=True)
    class Meta: 
        model = Category
        fields =  [ 
                  'name',
                  'url',
                  'food_items',
                 ]
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    








# from rest_framework import serializers
# from .models import FoodCategory, FoodItem

# class FoodCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodCategory
#         fields = '__all__'

# class FoodItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodItem
#         fields = '__all__'
    