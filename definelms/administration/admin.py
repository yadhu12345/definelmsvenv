from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
from lmsmainapp.models import *

@admin.register(Department)
class StudentAdmin(ImportExportModelAdmin):
    pass

@admin.register(course)
class courseAdmin(ImportExportModelAdmin):
    pass

@admin.register(exam)
class ExamAdmin(ImportExportModelAdmin):
    pass