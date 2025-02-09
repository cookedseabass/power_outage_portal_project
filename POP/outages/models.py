from django.db import models
from users.models import User

class OutageReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    report_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=50)
    planned = models.BooleanField(default=False)
    estimated_restoration_time = models.DateTimeField()

    def __str__(self):
        return f"Outage {self.report_id} by {self.username}"