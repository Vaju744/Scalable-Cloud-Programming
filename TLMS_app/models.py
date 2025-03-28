from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetail(models.Model):
    auth_user = models.ForeignKey(User, related_name='auth_user', on_delete=models.CASCADE)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=100)  # e.g., "Truck", "Van", "Bus"
    make = models.CharField(max_length=100)  # Vehicle manufacturer (e.g., Toyota, Ford)
    model = models.CharField(max_length=100)  # Vehicle model (e.g., Corolla, F-150)
    year = models.IntegerField()  # Year of manufacture
    license_plate = models.CharField(max_length=20, unique=True)  # License plate number
    capacity = models.IntegerField()  # Vehicle capacity (e.g., number of parcels it can carry)
    image = models.ImageField(upload_to='vehicle_images/', null=True, blank=True)  # Image field for vehicle photo
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of vehicle entry
    created_by = models.ForeignKey(User, related_name='auth_user1', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)  # Date and time of vehicle entry
    updated_by = models.ForeignKey(User, related_name='auth_user2', on_delete=models.CASCADE)

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)  # Driver's license number
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of vehicle entry
    created_by = models.ForeignKey(User, related_name='auth_user3', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)  # Date and time of vehicle entry
    updated_by = models.ForeignKey(User, related_name='auth_user4', on_delete=models.CASCADE)

class Consignment(models.Model):
    sender_name = models.CharField(max_length=100)  # Name of the sender
    receiver_name = models.CharField(max_length=100)  # Name of the receiver
    sender_address = models.TextField()  # Sender's address
    receiver_address = models.TextField()  # Receiver's address
    weight = models.FloatField()  # Weight of the consignment in kg
    contents = models.TextField()  # Description of the contents
    status = models.CharField(max_length=50, null=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, null=True, related_name="consignments")  # Vehicle transporting the consignment
    driver = models.ForeignKey('Driver', on_delete=models.SET_NULL, null=True, related_name="consignments")  # Driver handling the consignment
    dispatch_date = models.DateField(null=True, blank=True)  # Dispatch date
    delivery_date = models.DateField(null=True, blank=True)  # Delivery date
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time of vehicle entry
    created_by = models.ForeignKey(User, related_name='auth_user5', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)  # Date and time of vehicle entry
    updated_by = models.ForeignKey(User, related_name='auth_user6', on_delete=models.CASCADE)
    
class Feedback(models.Model):
    user = models.CharField(max_length=255)  # Name of the user
    message = models.TextField()  # Feedback message
    rating = models.IntegerField()  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.user} - {self.rating}"

