from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .api.serializers import UserSerializer, GeneralAccountSerializer, BalanceSerializer, PurchaseSerializer
from rest_framework import generics
from users.models import User, GeneralAccount, Balance, Purchase
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            cpf = serializer.validated_data.get('cpf')
            if User.objects.filter(cpf=cpf).exists():
                response_data = {
                    "message": "Usuario já cadastrado",
                    "ok": False
                }
                return Response(response_data, status=status.HTTP_409_CONFLICT)
            serializer.save()
            response_data = {
                    "message": "Usuario cadastrado com sucesso.",
                    "ok": True
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        response_data = {
            "message": "Não foi possivel criar o usuario.",
            "user_created": False,
            "errors": serializer.errors
        }
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            
            # Lógica para excluir o usuário
            
            # Exemplo: excluindo o usuário definindo o campo "deleted" como True
            instance.deleted = True
            instance.save()
            
            response_data = {
                "message": "Usuário deletado com sucesso.",
                "ok": True
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# GeneralAccount
class GeneralAccountCreateView(APIView):
    def post(self, request):
        serializer = GeneralAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeneralAccountList(generics.ListAPIView):
    queryset = GeneralAccount.objects.all()
    serializer_class = GeneralAccountSerializer


class GeneralAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralAccount.objects.all()
    serializer_class = GeneralAccountSerializer


class GeneralAccountUpdateView(UpdateAPIView):
    serializer_class = GeneralAccountSerializer
    queryset = GeneralAccount.objects.all()


class BalanceCreateView(APIView):
    def post(self, request):
        serializer = BalanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Balance

class BalanceList(generics.ListAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class BalanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class BalanceUpdateView(UpdateAPIView):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()


# Purchase
class PurchaseCreateView(APIView):
    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseList(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class PurchaseUpdateView(UpdateAPIView):
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()