from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import IHASerializer, UserActionsSerializer
from .models import IHA, UserActions
from .signals import iha_created_handler, iha_updated_handler


class ListIHAView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login-user')
        return render(request, 'iha-table.html')

    def post(self, request):
        return redirect('add-iha')


class AddIHAView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login-user')

        return render(request, 'add-iha.html')

    def post(self, request):
        data = request.data
        brand = None
        model_name = None

        try:
            brand = data['iha_brand']
            model_name = data['iha_name']

            serializer = IHASerializer(data={'brand': brand, 'model_name': model_name})

            if serializer.is_valid():
                created_iha = serializer.save()
                #iha_created_handler(sender=IHA, instance=created_iha, request=request)
                return Response({'message': 'IHA created!'})

            return Response({'error': 'Something went wrong!asdsad'})

        except Exception as e:
            print('Exceptionn')
            print(str(e))
            return Response({'message': 'Something went wrong!'})

class UpdateIHAView(APIView):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('login-user')

        iha = IHA.objects.get(id=id)

        return render(request, 'update-iha.html', {'iha': iha})

    def post(self, request, id):
        data = request.data

        try:
            brand = data['iha_brand']
            model_name = data['iha_name']

        except Exception as e:
            print(str(e))
            return Response({'error': 'Something went wrong!'})

        try:
            iha = IHA.objects.get(id=id)
            iha.brand = brand
            iha.model_name = model_name
            iha.save()
            #iha_updated_handler(sender=IHA, instance=iha, request=request)
            return Response({'message': 'IHA updated!'})
        except Exception as e:
            print(str(e))
            return Response({'error': 'IHA updated!'})


class DeleteIHAView(APIView):
    def post(self, request, id):
        iha = IHA.objects.get(id=id).delete()
        #iha_deleted_handler(sender=IHA, instance=iha, request=request)
        return Response({'message': 'Silme işlemi başarılı'})


class IHADataView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication credentials are required!'})

        all_iha = IHA.objects.all()
        serializer = IHASerializer(all_iha, many=True)
        all_iha_data = serializer.data

        return Response(all_iha_data)


class UserActionsListView(APIView):
    def get(self, request):
        return render(request, 'user-actions-table.html')


class UserActionsDataView(APIView):
    def get(self, request):
        actions = UserActions.objects.all()

        data = []

        for action in actions:
            user_info = {
                'username': action.user.username,
                'iha': f"{action.iha.brand} - {action.iha.model_name}",
                'action': action.action_type,
                'time': action.timestamp,
            }
            print("al")
            data.append(user_info)

        return Response(data)
