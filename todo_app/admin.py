from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # 1. Какие столбцы показывать в списке задач
    list_display = [
        'title',           # название
        'completed',       # статус (галочка)
        'priority',        # приоритет
        'created_at',      # дата создания
    ]

    # 2. По каким полям можно быстро фильтровать (справа)
    list_filter = [
        'completed',       # Выполнено / Не выполнено
        'priority',        # Low / Medium / High
        'created_at',      # по дате (сегодня, неделя, месяц…)
    ]

    # 3. По каким полям искать (поле поиска сверху)
    search_fields = [
        'title',           # по названию
        'description',     # по тексту описания
    ]

    # 4. Быстрое редактирование прямо в таблице (галочка "Выполнено")
    list_editable = [
        'completed',       # можно менять статус не заходя в форму
    ]

    # 5. Сортировка по умолчанию (новые задачи сверху)
    ordering = ['-created_at']

    # 6. Опционально: сколько записей на странице
    list_per_page = 20

    # 7. Опционально: какие поля показывать только для чтения
    readonly_fields = ['created_at']