import uuid
from django.db import models
from rest_framework.fields import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.


class CategoriesMenu(models.Model):
    name = models.CharField(
        validators=[MinLengthValidator(3)], max_length=25, primary_key=True, auto_created=False)

    def __str__(self):
        return self.name


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    thumbnail = models.ImageField(upload_to='coffee_images')
    description = models.TextField()
    stock = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    categories = models.ManyToManyField(
        CategoriesMenu, related_name='menu', )

    class Meta:
        db_table = 'menu'
        ordering = ['created']

    def __str__(self):
        return self.name

    def get_rating(self):
        rate = []
        rates = self.rating.all()
        length = len(rates)
        if not length:
            return 0

        for i in range(5):
            count = rates.filter(rate=i+1).count()
            count = (i + 1) * count
            rate.append(count)

        rate = sum(rate) / length

        return {'rate': round(rate, 1), 'count': length}


class ImageMenu(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="menu/images")

    def __str__(self):
        return self.image.name


class RatingMenu(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='rating')
    name = models.CharField(max_length=50)
    comment = models.TextField()
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ('rate',)

    def __str__(self):
        return self.name
