from rest_framework import serializers

from .models import *
from utils import validators


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingMenu
        fields = ('name', 'comment', 'rate')


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriesMenu
        fields = ('name', 'url')
        extra_kwargs = {'url': {'lookup_field': 'name'}}


class MenuSerializer(serializers.ModelSerializer):
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(use_url=True, allow_empty_file=True),
        write_only=True,
        required=False,
        default=None
    )
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Menu
        fields = ('url', 'id', 'name', 'price',
                  'thumbnail', 'description', 'stock',
                  'rate', 'created', 'uploaded_images')
        read_only_fields = ('id', 'created', 'rate')
        extra_kwargs = {'stock': {'required': True},
                        'uploaded_images': {'required': True}}

    def create(self, validated_data):
        images = validated_data.pop('uploaded_images')
        menu = Menu.objects.create(**validated_data)

        for image in images:
            ImageMenu.objects.create(menu=menu, image=image)

        return menu

    def get_rate(self, obj):
        return obj.get_rating()


class MenuDetailSerializer(MenuSerializer):
    categories = CategoriesSerializers(many=True, required=False)
    images = serializers.SerializerMethodField(read_only=True)
    rating = RatingSerializers(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ('name', 'price', 'images', 'description',
                  'stock', 'created', 'categories', 'rating', 'uploaded_images', 'thumbnail')
        read_only_fields = ('created',)
        extra_kwargs = {'thumbnail': {'write_only': True, 'required': False}}

    def get_images(self, obj):
        request = self.context.get('request', None)
        url = [url.image.url for url in obj.images.all()]
        if request is not None:
            url = [request.build_absolute_uri(path) for path in url]

        return url

    def update(self, instance, validated_data):
        images = validated_data.pop('uploaded_images')
        images_instance = []

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if images is not None:
            for image in images:
                image, created = ImageMenu.objects.get_or_create(
                    image=image, menu=instance)
                images_instance.append(image)

            instance.images.set(images_instance)

        return instance


class CategoriesDetailSerializers(CategoriesSerializers):
    menu = MenuSerializer(many=True)

    class Meta:
        model = CategoriesMenu
        fields = ('name', 'menu')
