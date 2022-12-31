from django.contrib import admin
from .models import Student
from .models import Tutor
from .models import Job
from .models import Application

# Register your models here.


admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Job)
admin.site.register(Application)


