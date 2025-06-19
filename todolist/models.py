from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)  # ⏰ Tambahan field deadline

    def is_overdue(self):
        return self.deadline and self.deadline < timezone.now().date()

    def __str__(self):
        return self.title

