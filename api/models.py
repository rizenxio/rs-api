from django.db import models
import shortuuid
from django.utils.timezone import now
# Create your models here.
class patient(models.Model):
    PRIORITY = (
    ("kritis", "Kritis"),
    ("mendesak", "Mendesak"),
    ("biasa", "Biasa"),
)
    STATUS = (
    ("waiting", "Waiting"),
    ("called", "Called"),
    ("cancelled", "Cancelled"),
)
    id = models.CharField(unique=True, max_length=50, default=shortuuid.uuid, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    symptoms = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY, default="biasa")
    created_at = models.DateTimeField(default=now, editable=False)
    adjusted_priority = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default="waiting")

    def __str__(self):
        return f"{self.name} ({self.id}) - {self.get_priority_display()} - {self.get_status_display()}"