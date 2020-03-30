from rest_framework import serializers
from MySer.models import *

# 此文件用来存放序列化器


# class StudentSerializer(serializers.Serializer):
class StudentSerializer(serializers.ModelSerializer):
    '''
    里面写的是每一个需要序ser列化/反序列化的字段
    跟定义模型基本一致
    '''
    # name = serializers.CharField(label='姓名', max_length=20)
    # age = serializers.IntegerField()
    # score = serializers.IntegerField()

    class Meta:
        # 告诉序列花旗，对应哪个模型
        model = Student
        # fields = ('name', 'age', 'score')
        fields = '__all__'
