from django.db import models
from .enums import CourseYear


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Department(BaseModel):
    code = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Schedule(BaseModel):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.IntegerField(choices=CourseYear.choices, default=CourseYear.UNKNOWN)
    file = models.FileField(upload_to="pics", null=True, blank=True)

    def __str__(self):
        return f"{self.department.name} - {self.year} year"

    class Meta:
        unique_together = ("department", "year",)
