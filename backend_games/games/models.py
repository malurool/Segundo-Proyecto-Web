from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)       # Título
    year = models.PositiveIntegerField()           # Año
    price = models.DecimalField(max_digits=12, decimal_places=2) # Precio
    developer = models.CharField(max_length=100)   # Desarrolladora
    description = models.TextField(blank=True)     # Descripción
    image = models.ImageField(upload_to='game_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
