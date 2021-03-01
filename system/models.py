from django.db import models


# Create your models here.

class Member(models.Model):
    full_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=9)  # Example: My id is s3634831
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name


class Event(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name


class KPI(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    communication = models.IntegerField()
    timeliness = models.IntegerField()
    quality_of_work = models.IntegerField()
    daily_communication = models.IntegerField()
    helpful_teammate = models.IntegerField()

