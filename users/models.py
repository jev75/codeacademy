from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Vartotojas')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='Apie save')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics'
                              , blank=True, null=True, verbose_name='Paveikslėlis')

    def __str__(self):
        return f'Profilis {self.user.username}'

    # def save(self, *args, **kwargs):
    #
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (150, 150)
    #         img = img.resize(output_size, Image.LANCZOS)
    #         img.save(self.image.path)

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'
