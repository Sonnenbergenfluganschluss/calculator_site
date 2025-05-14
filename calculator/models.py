from django.db import models
from django.contrib.auth.models import User  # стандартная модель пользователя

class Calculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # привязка к пользователю
    expression = models.CharField(max_length=255)  # например, "2+2"
    result = models.FloatField()  # например, 4.0
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания

    def __str__(self):
        return f"{self.expression} = {self.result} (User: {self.user.username})"