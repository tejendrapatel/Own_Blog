from django.db import models

class ProjectMade(models.Model):
    name =  models.CharField(max_length=50)
    image = models.FileField(null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name