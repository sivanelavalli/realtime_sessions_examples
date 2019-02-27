from django.db import models

class Customer(models.Model):
    cust_id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=20)

    def __str__(self):
        return self.last_name

class Vehicle(models.Model):
    vehicle_id=models.IntegerField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    registration_number=models.CharField(max_length=30)
    engine_number=models.CharField(max_length=30)
    choice_number=models.CharField(max_length=30)
    registration_date=models.DateField()
    policy_end_date=models.DateField()
    def __str__(self):
        return self.customer

class Brand(models.Model):
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    b_name=models.CharField(max_length=30)
    country=models.CharField(max_length=20)

class CarModel(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    m_name=models.CharField(max_length=30)

class Vmv(models.Model):
    v_model=models.ForeignKey(CarModel,on_delete=models.CASCADE)
    v_name=models.CharField(max_length=30)
    colour=models.CharField(max_length=20)
    engine_cc=models.IntegerField()
    fuel_type=models.CharField(max_length=20)
    seating_capacity=models.IntegerField()
