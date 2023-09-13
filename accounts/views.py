from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


class RegisterUserView(APIView):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = None
        password = None

        try:
            username = request.data['username']
            password = request.data['password']

        except Exception as e:
            return Response("User credentials cannot provided. Please fill the credentials", status=status.HTTP_400_BAD_REQUEST)

        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response(
                f"Successfully created user: {username}.", status=status.HTTP_201_CREATED)
        else:
            return Response(f"Failed to create user: {username}. Is the form sending a POST request that includes a username and password?", status=status.HTTP_403_FORBIDDEN)


class LoginUserView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = None
        password = None

        try:
            username = request.data['username']
            password = request.data['password']

        except Exception as e:
            return Response("User credentials cannot provided. Please fill the credentials",
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response("Login success!", status=status.HTTP_200_OK)
        else:
            return Response("Login failed! Maybe the user was not created properly? Edit this response in accounts/views.py")


@api_view(['POST'])
def logout_user_view(request):
    logout(request)
    return Response("Logged out")
