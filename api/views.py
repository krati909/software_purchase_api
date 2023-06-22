from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, F
from api.models import Purchase

class TotalItemsSold(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        department = request.query_params.get('department')

        total_items = Purchase.objects.filter(
            transaction_date__range=[start_date, end_date],
            department__iexact=department
        ).aggregate(total_items=Sum('quantity'))['total_items'] or 0

        return Response(total_items)

class NthMostTotalItem(APIView):
    def get(self, request):
        item_by = request.query_params.get('item_by')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        n = request.query_params.get('n')

        if item_by == 'quantity':
            order_by_field = '-quantity'
        elif item_by == 'price':
            order_by_field = '-price'

        nth_item = Purchase.objects.filter(
            transaction_date__range=[start_date, end_date]
        ).order_by(order_by_field).values_list('item', flat=True).distinct()[int(n) - 1]

        return Response(nth_item)

class PercentageOfDepartmentWiseSoldItems(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        department_counts = Purchase.objects.filter(
            transaction_date__range=[start_date, end_date]
        ).values('department').annotate(count=Count('department'))

        total_count = sum([item['count'] for item in department_counts])
        department_percentages = {
            item['department']: round((item['count'] / total_count) * 100, 2)
            for item in department_counts
        }

        return Response(department_percentages)

class MonthlySales(APIView):
    def get(self, request):
        product = request.query_params.get('product')
        year = request.query_params.get('year')

        monthly_sales = Purchase.objects.filter(
            item__iexact=product,
            transaction_date__year=year
        ).values('transaction_date__month').annotate(total_sales=Sum(F('price') * F('quantity'))).order_by('transaction_date__month').values_list('total_sales', flat=True)

        return Response(list(monthly_sales))
