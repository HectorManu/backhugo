from django.db import models

class VideoResponse(models.Model):
    matricule = models.CharField(max_length=20, null=True)
    video_name = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.video_name
