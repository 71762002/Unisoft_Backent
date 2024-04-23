from rest_framework import serializers
from .models import Transfers


class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = ("id", "ext_id", "ref_name", "cardnumber", "owner", "commision", "state", "amount", "currency")

    