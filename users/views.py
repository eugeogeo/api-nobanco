from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .api.serializers import UserSerializer, GeneralAccountSerializer, BalanceSerializer, PurchaseSerializer
from rest_framework import generics
from .models import User, GeneralAccount, Balance, Purchase

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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