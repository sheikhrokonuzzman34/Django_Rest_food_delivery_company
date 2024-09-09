from rest_framework import serializers
from apps.restaurant.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'owner']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'restaurant']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price']

class OrderItemSerializer(serializers.ModelSerializer):
    item = MenuItemSerializer(read_only=True)
    item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source='item', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'item', 'item_id', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='orderitem_set')
    customer_id = serializers.IntegerField(source='customer.id', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer_id', 'restaurant', 'items', 'total_amount', 'status', 'payment_method']

    def create(self, validated_data):
        request = self.context.get('request', None)
        if request and hasattr(request, 'user'):
            validated_data['customer'] = request.user
        else:
            raise serializers.ValidationError({"customer": "Customer information is missing."})

        items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('orderitem_set', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if items_data is not None:
            instance.orderitem_set.all().delete()
            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['customer'] = instance.customer.id
        return representation