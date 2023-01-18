from django.contrib import admin
from .models import StudentReg
from .models import TutorReg
from .models import Job
from .models import Application
from .models import User

# Register your models here.    


admin.site.register(StudentReg)
admin.site.register(TutorReg)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(User)


