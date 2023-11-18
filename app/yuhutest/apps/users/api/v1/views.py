from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSeralizer


@extend_schema(description="Login", operation_id="Login", tags=["Access"])
class LoginView(TokenObtainPairView):
    pass


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny, ))
@extend_schema(description="Create User", operation_id="User.Create", tags=["Access"])
def create_user(request):
    request.data['email'] = request.data['username']
    serializer = UserCreateSeralizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        refresh = RefreshToken.for_user(serializer.instance)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
