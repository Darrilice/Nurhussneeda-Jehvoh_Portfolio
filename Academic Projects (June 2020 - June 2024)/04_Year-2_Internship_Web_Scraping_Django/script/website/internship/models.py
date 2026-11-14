from django.db import models

class Intern_other(models.Model):
    JOB_DESCRIPTION  = models.TextField()
    COMPANY = models.TextField()
    LOCATION = models.TextField()
    EMPLOYMENT_RATE = models.TextField()
    
    