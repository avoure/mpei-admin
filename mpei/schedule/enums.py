from django.db import models


class CourseYear(models.IntegerChoices):
    UNKNOWN = 0
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
