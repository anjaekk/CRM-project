from datetime import datetime

from django.db.models import Sum

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Contract
from .serializers import MonthlyProductTotalSerializer

class MonthlyProductTotalView(APIView):
    serializer_class = MonthlyProductTotalSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        monthly_income = []
        for month_filter in range(1, 6):
            dict = {}
            month = datetime.now().month-month_filter
            income = Contract.objects.filter(start_date__month__gte=month).aggregate(Sum('price'))
            dict["name"] = month
            dict["value"] = round(income["price__sum"]/10000000, 0)
            monthly_income.append(dict)
        return Response(monthly_income, status=status.HTTP_200_OK)