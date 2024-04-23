from django.db import models
from user.constant import DefaultAbstract
from user.models import User

# class Dashboard(DefaultAbstract):
#     balance = models.IntegerField(default=0)
#     sender  = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="yuboruvchi")
#     receiver  = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="oluvchi")
    

class Transfers(DefaultAbstract):
    ext_id = models.IntegerField(default=0)
    ref_name = models.CharField(max_length=250)
    cardnumber = models.CharField(max_length=16)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    commision = models.IntegerField(default=0)
    state = models.CharField(max_length=100)
    amount = models.IntegerField()
    currency = models.IntegerField()


    def __str__(self) -> str:
        return f"{self.ext_id} - {self.owner}"
    



    

