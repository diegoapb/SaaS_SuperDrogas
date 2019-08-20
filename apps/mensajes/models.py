from django.db import models


class Mensaje(models.Model):
    mensaje = models.TextField()

    def __str__(self):
        return self.mensaje


