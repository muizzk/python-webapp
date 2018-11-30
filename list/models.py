from django.db import models

class List(models.Model):
# CharField and BooleanField are datatypes
# For more information visit: https://www.webforefront.com/django/modeldatatypesandvalidation.html
    item = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item # + ' | ' + str(self.completed)