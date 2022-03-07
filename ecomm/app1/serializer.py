from curses import meta
from .models import *
from rest_framework import serializers

# class productSerializer(serializers.ModelSerializer):
#     discount = serializers.SerializerMethodField('get_discount')
#     def get_discount(self, obj):
#         return round(((obj.mrp - obj.csp)/obj.mrp)*100,2)

#     class Meta:
#         model= Products
#         fields = ['name', 'image' , 'mrp' , 'csp' , 'brand' , 'discount']
#         # fields = '__all__'

# class cartSerializer(serializers.ModelSerializer):
#     subtotal = serializers.SerializerMethodField('sub_total')
#     def sub_total(self, obj):
#         return (obj.csp * obj.quantity)
#     class Meta:
#         model= Cart
#         fields=['name', 'image' , 'mrp' , 'csp' , 'quantity', 'subtotal']