from django.db import models


class DeployedApp(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    port = models.CharField(max_length=255)

    def url(self):
        return f"http://{self.ip}:{self.port}"

    def __str__(self):
        return self.name

