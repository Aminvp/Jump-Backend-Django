from django.contrib import admin

from .models import College, Lesson, UserProfile


class CollegeAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(College, CollegeAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
