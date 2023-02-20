from django.db import models

class Branch(models.Model):
    district = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    sub_area = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.sub_area}, {self.district}"

class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class MaterialsProvide(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
          
class Account(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    branch = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    account_type = models.CharField(max_length=50)
    materials_provide = models.ManyToManyField(MaterialsProvide, blank=True)

    def __str__(self):
        return self.name


