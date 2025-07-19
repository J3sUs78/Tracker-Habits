from django.contrib import admin
from .models import UserProfile, Category, Habit, HabitRecord

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'notification_enabled', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')
    list_filter = ('notification_enabled', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'habits_count')
    search_fields = ('name', 'description')
    ordering = ('name',)
    
    def habits_count(self, obj):
        return obj.habits.count()
    habits_count.short_description = 'Número de hábitos'

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'user', 'periodicidad', 'meta', 'activo', 'categoria', 'fecha_creacion')
    search_fields = ('nombre', 'user__username', 'descripcion')
    list_filter = ('periodicidad', 'activo', 'categoria', 'fecha_creacion')
    readonly_fields = ('fecha_creacion',)
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)

@admin.register(HabitRecord)
class HabitRecordAdmin(admin.ModelAdmin):
    list_display = ('habit', 'fecha', 'completado', 'user')
    search_fields = ('habit__nombre', 'habit__user__username')
    list_filter = ('completado', 'fecha', 'habit__periodicidad')
    date_hierarchy = 'fecha'
    ordering = ('-fecha',)
    
    def user(self, obj):
        return obj.habit.user.username
    user.short_description = 'Usuario'
