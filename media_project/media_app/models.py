from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    LOCATION_CHOICES = [
        ('Palakkad', 'Palakkad'),
        ('Calicut', 'Calicut'),
        ('Kochi', 'Kochi'),
        ('Wayanad', 'Wayanad'),
    ]
    Post_caption = models.TextField()
    image_or_video_content = models.FileField(upload_to='static/image/')
    publication_date = models.DateTimeField( auto_now_add=True)
    location_post = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


