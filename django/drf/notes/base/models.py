from django.db import models

class Notes(models.Model):
    title=models.TextField(max_length=120,null=False)
    content=models.CharField(max_length=5000)

    def __str__(self) -> str:
        return self.title






# class Users(models.Model):
#     first_name=models.TextField(max_length=120)
#     last_name=models.TextField(max_length=120)
#     username=models.TextField(max_length=120,null=False)
#     email=models.EmailField(max_length=120,null=False)
#     password=models.TextField(max_length=15,null=False)

#     def __str__(self) -> str:
#         return self.email