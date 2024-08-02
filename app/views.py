from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Parameter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ParameterListView(APIView):
    def get(self, request):
        parameters = Parameter.objects.values('name').distinct()
        data = []
        for param in parameters:
            values = Parameter.objects.filter(name=param['name']).values('value').distinct()
            data.append({
                'name': param['name'],
                'values': [v['value'] for v in values],
                'count': Parameter.objects.filter(name=param['name']).count()
            })
        return Response(data)
