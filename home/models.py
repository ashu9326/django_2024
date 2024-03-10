from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()    django add this field automatically
    name = models.CharField(max_length = 100)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    address = models.TextField()
    image   = models.ImageField()
    file   = models.FileField()

    # python manage.py makemigrations
    #  pyhton manage.py migrate

    # django run all migration and prepare their states and then compair to find changes occure or not, if django didn't get any changes then it understood no changes will apply , otherwise it will migrate.and apply migration.

