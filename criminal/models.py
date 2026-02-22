from django.db import models

class Criminal(models.Model):
    STATUS_CHOICES = [
        ('wanted', 'Wanted'),
        ('arrested', 'Arrested'),
        ('convicted', 'Convicted'),
        ('released', 'Released'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50, default='Indian')
    address = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='wanted')
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='criminals/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def crime_count(self):
        return self.fir_set.count()