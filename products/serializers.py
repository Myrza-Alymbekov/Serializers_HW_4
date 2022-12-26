from rest_framework import serializers

from .models import Item, Brand, Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data['name'])
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class BrandSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=30)

    def create(self, validated_data):
        brand = Brand.objects.create(name=validated_data['name'], address=validated_data['address'])
        return brand

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        item = Item.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            brand_id=validated_data['brand_id'],
            category_id=validated_data['category_id']
        )
        return item

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.brand_id = validated_data['brand_id']
        instance.category_id = validated_data['category_id']
        instance.save()
        return instance


# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = "__all__"
#
#
# class BrandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Brand
#         fields = "__all__"


