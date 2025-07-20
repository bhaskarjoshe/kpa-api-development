from django.db import models


class WheelSpecification(models.Model):

    formNumber = models.CharField(max_length=100)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()

    def __str__(self):
        return self.formNumber

    class Meta:
        db_table = "wheel_specification"


class BogieChecksheet(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()

    bogieDetails = models.JSONField()
    bogieChecksheet = models.JSONField()
    bmbcChecksheet = models.JSONField()

    status = models.CharField(max_length=50, default="Saved")

    def __str__(self):
        return self.formNumber

    class Meta:
        db_table = "bogie_checksheet"
