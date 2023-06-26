from rest_framework import serializers

from customer.models import MenuItem




def validate_name(value):
    qs = MenuItem.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    return value