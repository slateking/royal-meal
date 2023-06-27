from rest_framework.reverse import reverse
from rest_framework import serializers
from restaurant.models import FoodItem, Category







class CategoriesSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True) 
    class Meta: 
        model = Category
        fields =  [ 
                  'name',
                  'url',
                 ]
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
    #    return reverse("rs-list",  request=request)
    







class FoodItemSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer()
    url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = FoodItem
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
                  'category',
                 ]
        
        
        
    def get_url(self, obj):
       request = self.context.get('request')
       if request is None:
           return None
       return reverse("rs-list", kwargs={"pk": obj.pk}, request=request)
    

    def validate_name(self, value):
        qs = FoodItem.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value
    













































# # serializers.py

# from rest_framework import serializers
# from .models import Category, FoodItem

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = [
#             'id', 
#             'name', 
#             ]

# class FoodItemSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = FoodItem
#         fields = [
#             'id', 
#             'name', 
#             'category', 

#             'publish_date']







# # class JapaneseSerializer(serializers.ModelSerializer):
# #     # url = serializers.SerializerMethodField(read_only=True) 
# #     class Meta:
# #         model = Japanese
# #         fields =  [ 
# #                   'id',
# #                   'name',
# #                   'description',
# #                 #   'price',
# #                 #   'discount',
# #                 #   'rating',
# #                 #   'sale_price',
# #                 #   'image',
# #                 #   'url',
# #                   ]
        
        
        
# #     def get_url(self, obj):
# #        request = self.context.get('request')
# #        if request is None:
# #            return None
# #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# #     def validate_name(self, value):
# #         qs = Japanese.objects.filter(name__iexact=value)
# #         if qs.exists():
# #             raise serializers.ValidationError(f"{value} is already a product name.")
# #         return value
    









# # # class New_MexicanSerializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = New_Mexican
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = New_Mexican.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    









# # # class SushiSerializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = Sushi
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = Sushi.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    










# # # class SandwichesSerializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = Sandwiches
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = Sandwiches.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    









# # # class NigerianSerializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = Nigerian
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = Nigerian.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    










# # # class ChineseSerializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = Chinese
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = Chinese.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    










# # # class DrinksSerializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = Drinks
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = Drinks.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    












# # # class Most_popular_Serializer(serializers.ModelSerializer):
# # #     url = serializers.SerializerMethodField(read_only=True) 
# # #     class Meta:
# # #         model = Most_popular
# # #         fields =  [ 
# # #                   'id',
# # #                   'name',
# # #                   'description',
# # #                   'price',
# # #                   'discount',
# # #                   'rating',
# # #                   'sale_price',
# # #                   'image',
# # #                   'url',
# # #                  ]
        
        
        
# # #     def get_url(self, obj):
# # #        request = self.context.get('request')
# # #        if request is None:
# # #            return None
# # #        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    

# # #     def validate_name(self, value):
# # #         qs = Most_popular.objects.filter(name__iexact=value)
# # #         if qs.exists():
# # #             raise serializers.ValidationError(f"{value} is already a product name.")
# # #         return value
    
