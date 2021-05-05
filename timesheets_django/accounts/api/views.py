from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from accounts.models import User
from .serializers import RegistrationSerializer, loginSerializer, PasswordSerializer
from  timesheets_django.utils import generate_employee_id, generate_password,send_password_and_username

@swagger_auto_schema(method='post', request_body=RegistrationSerializer)
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    if request.method == 'POST':
        qs = User.objects.all()
        email = request.data.get('email')
        username = request.data.get('username')
        designation = request.data.get('designation')
        for i in qs:
            if username == i.username:
                return Response({'error': 'Employee already exists.'}, status=HTTP_400_BAD_REQUEST)
            if email == i.email:
                return Response({'error': 'Email already exists.'}, status=HTTP_400_BAD_REQUEST)
        serializer = RegistrationSerializer(data=request.data)
        employee = False
        management = False
        if designation == 'management':
            management = True
        else:
            employee = True
        if serializer.is_valid():
            user = serializer.save(is_management = management,is_employee = employee,username = generate_employee_id())
            password = generate_password()
            print(password)
            user.set_password(password)
            user.save()
            send_password_and_username(username, email, password)
            return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=loginSerializer)
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    try:
        qs = User.objects.get(pk=token.user_id)
    except User.DoesNotExist:
        return Response({'error': 'user id does not exist'}, status=HTTP_404_NOT_FOUND)
    return Response({'token': token.key, 'user_id': token.user_id,'role':qs.designation}, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def logout(request):
    print(request.user.auth_token)
    if not request.user.auth_token:
        return Response({'error': 'something went wrong'}, status=HTTP_404_NOT_FOUND)
    request.user.auth_token.delete()
    return Response({'success': 'successfully logout'}, status=HTTP_200_OK)

@swagger_auto_schema(method='put', request_body=PasswordSerializer)
@csrf_exempt
@api_view(['PUT'])
def change_password(request):
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    user = User.objects.get(id = request.user.id ) 
    if not user.check_password(old_password):
        return Response({'error':'Old password is not correct'})
    user.set_password(new_password)
    user.save()
    return Response({'success': 'successfully update'}, status=HTTP_200_OK)
    



