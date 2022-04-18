from rekammedis.models import Pasien, RekamanMedis
from rekammedis.serializers import PasienSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PasienApi(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request: Request, format=None):
        serializer = PasienSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PasienDetailApi(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request: Request, nik: str, format=None):
        try:
            pasien = Pasien.objects.get(nik=nik)
            serializer = PasienSerializer(pasien)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Pasien.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class RekamMedisApi(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request: Request, format=None) -> Response:
        from pprint import pprint
        pprint(request.data)
        author = TenagaMedisProfile.objects.get(
            account__email=request.user)
        if author is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = RekamanMedisPostSerializer(data=request.data)
        nik = request.data.get("patient")
        pasien = Pasien.objects.get_or_create(nik=nik)
        if serializer.is_valid():
            serializer.save(author=author, pasien=pasien)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class RekamMedisDetilApi(APIView):
    pass
