from functools import partial
from urllib import request
from rest_framework.permissions import IsAuthenticated
from urllib.request import Request
from .serializers import KlinikSerializer, CabangSerializer
from .models import Cabang, Klinik, OwnerProfile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.views import APIView
from django.db import models


def get_object(klass: models.Model, pk: int):
    try:
        return klass.objects.get(pk=pk)
    except klass.DoesNotExist:
        return None


class KlinikAPI(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get_klinik(self, request: Request):
        owner = OwnerProfile.objects.get(account__email=request.user)
        try:
            klinik = Klinik.objects.get(owner=owner)
            return klinik
        except:
            return None

    def post(self, request):
        owner = OwnerProfile.objects.get(account__email=request.user)
        serializer = KlinikSerializer(data=request.data)
        klinik_exist = Klinik.objects.filter(owner=owner).count() > 0
        if serializer.is_valid() and owner is not None and not klinik_exist:
            serializer.save(owner=owner)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request, format=None):
        klinik = self.get_klinik(request)
        serializer = KlinikSerializer(klinik)
        if klinik is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request: Request, format=None):
        klinik = self.get_klinik(request)
        serializer = KlinikSerializer(klinik, data=request.data, partial=True)
        if serializer.is_valid() and klinik is not None:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, format=None):
        klinik = self.get_klinik(request)
        if klinik is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        klinik.delete()
        return Response(status=status.HTTP_200_OK)


class CabangListApi(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request: Request, format=None):
        owner = OwnerProfile.objects.get(account__email=request.user)
        klinik = Klinik.objects.get(owner=owner)
        branches = Cabang.objects.all()
        branches = branches.filter(klinik=klinik)
        serializer = CabangSerializer(branches, many=True)
        return Response(serializer.data)

    def post(self, request: Request, format=None):
        serializer = CabangSerializer(data=request.data)
        klinik_id = request.data.get("klinik")
        klinik = get_object(Klinik, klinik_id)
        if serializer.is_valid() and klinik is not None:
            serializer.save(klinik=klinik)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CabangDetailApi(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request: Request, pk: int, format=None):
        cabang = get_object(Cabang, pk)
        serializer = CabangSerializer(cabang)
        if cabang is not None:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request: Request, pk: int, format=None):
        cabang = get_object(Cabang, pk)
        serializer = CabangSerializer(cabang, data=request.data)
        if serializer.is_valid() and cabang is not None:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None):
        cabang = get_object(Cabang, pk)
        if cabang is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cabang.delete()
        return Response(status=status.HTTP_200_OK)
