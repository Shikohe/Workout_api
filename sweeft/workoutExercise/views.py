from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ExerciseView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        exercises = Exercise.objects.all()

        return Response(ExerciseSerializer(exercises, many=True).data)

    @swagger_auto_schema(
        operation_description="Add a new exercise",
        request_body=ExerciseSerializer,
        responses={201: openapi.Response("Exercise added successfully")}
    )
    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Exercise added successfully"})

        return Response({"message": "Error"})


class MuscleView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        muscles = Muscle.objects.all()
        return Response(MuscleSerializer(muscles, many=True).data)

    @swagger_auto_schema(
        operation_description="Add a new muscle",
        request_body=MuscleSerializer,
        responses={201: openapi.Response("Muscle added successfully")}
    )
    def post(self, request):
        serializer = MuscleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Muscle added successfully"})

        return Response({"message": "Error"})
