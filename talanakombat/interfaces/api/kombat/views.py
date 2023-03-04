import logging

from django.http import HttpResponse, JsonResponse
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status, views
from talanakombat.domain.kombat import processes
from talanakombat.interfaces.api.commons import serializers as commons_serializers
from talanakombat.interfaces.api.kombat import constants, serializers

logger = logging.getLogger("kombat.interfaces")


class Kombat(views.APIView):
    """
    Obtener información de la pelea
    """

    permission_classes = []

    @swagger_auto_schema(
        operation_description="Endpoint descripcion de la pelea",
        request_body=serializers.Kombat(many=False),
        responses={
            200: commons_serializers.ResultSerializer(many=False),
            400: openapi.Response(
                type=openapi.TYPE_OBJECT,
                description="",
                schema=commons_serializers.ExceptionSerializer(many=False),
            ),
        },
    )
    def post(self, request, format=None):
        serializer = serializers.Kombat(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        try:
            kombat = processes.get_kombat_result(
                player1=valid_data["player1"], player2=valid_data["player2"]
            )
            return HttpResponse(kombat, status=status.HTTP_200_OK)
        except Exception:
            return JsonResponse(
                constants.UNEXPECTED_ERROR,
                status=status.HTTP_400_BAD_REQUEST,
                safe=False,
            )
