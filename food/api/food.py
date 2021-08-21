from django.db.models import Count, Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import Food, Tag
from food.serializers import FoodSerializer, SuggestFoodSerializer


class ListCreateFoodApi(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class DetailUpdateDeleteFoodApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class SuggestFoodApi(APIView):
    serializer_class = SuggestFoodSerializer
    queryset = Food.objects.all()

    tag_ids = openapi.Parameter('tag_ids', in_=openapi.IN_QUERY, description='tags ids', type=openapi.TYPE_ARRAY,
                                items=openapi.Items(type=openapi.TYPE_INTEGER), required=True)

    @swagger_auto_schema(manual_parameters=[tag_ids])
    def get(self, request):
        tag_ids = request.query_params.get('tag_ids')
        tag_ids = list(map(int, tag_ids.split(',')))
        if not isinstance(tag_ids, list):
            return Response('tag_ids must be a list of integer', status=400)
        tags = Tag.objects.filter(pk__in=tag_ids)
        self.queryset = self.queryset.annotate(sub_tag_count=Count('tags', filter=Q(
            tags__in=tags))).order_by('-sub_tag_count')
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=200)
