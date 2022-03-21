from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=image=models.ImageField(default="man.jpg", upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kawrgs):
    #     super().save(self, *args, **kawrgs)
    #
    #     img=Image.open(self.image.path)
    #
    #     if img.height>300 and img.width>200:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    