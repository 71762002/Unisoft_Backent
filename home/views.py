from django.shortcuts import render
from django.db.models import Q
from rest_framework.generics import ListCreateAPIView

from home.serializer import TransfersSerializer
from .models import Transfers
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response




class TransferAPi(ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Transfers.objects.all()
    serializer_class = TransfersSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        q = params.get("q")

        if q:
            queryset = queryset.filter(
                Q(ext_id__icontains=q) | Q(ref_name__icontains=q) | Q(cardnumber__icontains=q) |
                Q(owner__icontains=q) | Q(state__icontains=q) | Q(amount__icontains=q)
            )
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        request.data['owner'] = request.user.pk
        return self.create(request, *args, **kwargs)