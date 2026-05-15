from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)
    marks=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
     return self.name
#get means data lana without changing koi validation na krna whether post means kai data mai changes kr kai dikhana yani database ja kr actual changes show krwana 