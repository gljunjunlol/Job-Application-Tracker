from django.db import models
from django.contrib.auth.models import User

# Create your models here, data of collection
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model): # inherit from models.Model
    todoList = models.ForeignKey(ToDoList, on_delete =models.CASCADE) # line 5 char field, django does not know, so need foreign key, cascade special way of removing
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
    	return self.text


class Contact(models.Model):
    PURPOSE_CHOICES = [
        ('FT', 'Full-Time'),
        ('PT', 'Part-Time'),
        ('IS', 'Internship'),
        ('C', 'Contract'),
        ('F', 'Freelancer'),
        ('T', 'Temporary'),
        ('TR', 'Trainee'),

    ]

    name = models.CharField(max_length=100)
    # can put EmailField for email
    email = models.CharField(max_length=100)
    purpose = models.CharField(max_length=2, choices=PURPOSE_CHOICES)
    role = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    date = models.DateField(null=True, editable=True)
    message = models.TextField()

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return("Company Name:----- " + self.name + " at " + self.email + "-----" + "Type is " + self.purpose + " Role:----- " + self.role + "Location:----- " + self.location + "Date" + "                                     " + str(self.date))
        return ' '.join(field_values)
    	