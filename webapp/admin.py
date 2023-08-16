from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Syllabus)
admin.site.register(Time_Table)
admin.site.register(Faculty)
admin.site.register(Hackathons)
admin.site.register(Research_cell_faculty)
admin.site.register(Paper_published)
admin.site.register(Alumni)
