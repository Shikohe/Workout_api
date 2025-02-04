from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *


class WorkoutPlanView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        workout_plans = WorkoutPlan.objects.all()
        serializer = WorkoutPlanSerializer(workout_plans, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Add a new workout plan",
        request_body=WorkoutPlanSerializer,
        responses={201: openapi.Response("Workout plan added successfully")}
    )
    def post(self, request):
        serializer = WorkoutPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Workout plan added successfully"}, status=201)
        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_description="Delete workout plan",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the user', example=1),
                'exercise_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the exercise', example=1),
            },
            required=['user_id', 'exercise_id']
        ),
        responses={201: openapi.Response("Workout plan deleted successfully")}
    )
    def delete(self, request):
        user_id = request.data["user_id"]
        exercise_id = request.data["exercise_id"]
        workout_plan = WorkoutPlan.objects.filter(user=user_id, exercise=exercise_id)

        if workout_plan:
            workout_plan.delete()
            return Response("Workout plan deleted successfully", status=200)
        return Response("Workout plan does not exist", status=404)


class WorkoutSessionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        workout_sessions = WorkoutSession.objects.all()
        serializer = WorkoutSessionSerializer(workout_sessions, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Add a new workout session",
        request_body=WorkoutSessionSerializer,
        responses={201: openapi.Response("Workout session added successfully")}
    )
    def post(self, request):
        serializer = WorkoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Workout session added successfully"}, status=201)
        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_description="Delete workout session",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the user', example=1),
                'workout_plan_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the workout plan',
                                                  example=1),
            },
            required=['user_id', 'workout_plan_id']
        ),
        responses={201: openapi.Response("Workout session deleted successfully")}
    )
    def delete(self, request):
        user_id = request.data["user_id"]
        workout_plan_id = request.data["workout_plan_id"]
        workout_session = WorkoutSession.objects.filter(user=user_id, workout_plan=workout_plan_id)
        if workout_session:
            workout_session.delete()
            return Response("Workout session deleted successfully", status=200)
        return Response("Workout session does not exist", status=404)


class FitnessGoalView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        goals = FitnessGoal.objects.all()
        serializer = WorkoutSessionSerializer(goals, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        operation_description="Add a new fitness goals",
        request_body=WorkoutSessionSerializer,
        responses={201: openapi.Response("Fitness goal added successfully")}
    )
    def post(self, request):
        serializer = WorkoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Fitness goal added successfully"}, status=201)
        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_description="Delete fitness goal",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the user', example=1),
            },
            required=['user_id']
        ),
        responses={201: openapi.Response("Fitness goal deleted successfully")}
    )
    def delete(self, request):
        user_id = request.data["user_id"]
        goal = FitnessGoal.objects.filter(user=user_id)
        if goal:
            goal.delete()
            return Response("Fitness goal deleted successfully", status=200)
        return Response("Fitness goal does not exist", status=404)


class StartWorkoutModeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Add a new fitness goals",
        request_body=WorkoutModeSessionSerializer,
        responses={201: openapi.Response("Fitness goal added successfully")}
    )
    def post(self, request):
        serializer = WorkoutModeSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"Something went wrong!"}, status=500)


class EndWorkoutModeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, session_id):
        try:
            session = WorkoutModeSession.objects.get(id=session_id)

            if session.status == 'completed':
                return Response({"message": "Workout already completed!"})

            session.status = 'completed'
            session.save()
            return Response({"message": "Workout completed!"}, status=200)
        except WorkoutModeSession.DoesNotExist:
            return Response({"error": "Session not found"}, status=404)
