from django.db import models

# Create your models here.

class Task(models.Model):
    # Приоритеты (как choices)
    PRIORITY_CHOICES = [
        ('Low', 'Low'),         # 1 - Низкий
        ('Medium', 'Medium'),   # 2 - Средний
        ('High', 'High'),       # 3 - Высокий
    ]

    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )

    completed = models.BooleanField(
        default=False,
        verbose_name='Выполнено'
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium',
        verbose_name='Приоритет'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )

    def __str__(self):
        # Самый простой и понятный вариант, который часто используют
        status = '✓' if self.completed else '○'
        return f"{status} {self.title}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']          # новые задачи сверху
