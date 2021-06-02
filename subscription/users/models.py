from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Plan(models.Model):
    plan_name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    validity = models.IntegerField(default=0)

    def __str__(self):
        return self.plan_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    subs_date = models.DateTimeField(null=True)
    plan_name = models.ForeignKey(Plan, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
