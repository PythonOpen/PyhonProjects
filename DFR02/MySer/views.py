from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
# Create your views here.
from MySer.models import Student
from MySer.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet


class StudentViewSet(ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGenAPIView(GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        '''
        处理业务
        跟数据库交互
        :param request:
        :return:
        '''
        ser = self.get_serializer(self.queryset.all(), many=True)
        return Response(data=ser.data)
        # return Response(data=None)

    # def get(self, request):
    #     '''
    #     处理业务
    #     跟数据库交互
    #     :param request:
    #     :return:
    #     '''
    #     print("hahaha")
    #     stus = Student.objects.all()
    #     ser = StudentSerializer(stus, many=True)
    #     return Response(data=ser.data)
    #     # return Response(data=None)


class StudentVS(viewsets.ModelViewSet):
    pass


class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self, request):
        '''
        处理业务
        跟数据库交互
        :param request:
        :return:
        '''
        print("In APIView get")
        stus = Student.objects.all()
        ser = StudentSerializer(stus, many=True)
        return Response(data=ser.data)

