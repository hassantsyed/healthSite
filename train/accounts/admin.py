from django.contrib import admin
from .models import User, Weight, Task, JoinTeam

# Register your models here.
admin.site.register(User)
admin.site.register(Weight)
admin.site.register(Task)
admin.site.register(JoinTeam)
