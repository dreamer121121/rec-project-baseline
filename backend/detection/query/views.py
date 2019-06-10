from django.shortcuts import render
import pymysql
import uuid
from django.http import JsonResponse
from PIL import Image
import numpy as np
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.

def send_message(request):
    try:
        id = uuid.uuid1()
        name = request.GET.get('nm')
        email = request.GET.get('email')
        message = request.GET.get('message')
        conn = pymysql.Connect(host= 'localhost',db='rec_project',password='123456',user='root')
        cursor = conn.cursor()
        fileds = ('id','fullname','email','message')
        sql = 'insert into detection'
        sql += str(tuple(fileds))
        sql = sql.replace('\'','')
        values = (str(id),name,email,message)
        sql_values = ' values'+str(tuple(values))
        sql += sql_values
        cursor.execute(sql)
        conn.commit()
        result = {}
        result['status'] = 'success'
        result['message'] = ['发送信息成功']
        return JsonResponse(result)
    except Exception as e:
        result = {}
        result['status'] = 'failed'
        result['message'] = ["发送信息失败"]
        return JsonResponse(result)

def postimg(request):
    result = {}
    try:
        img = request.FILES.get('img')
        default_storage.save('C:\\Users\\Tao xia\\Desktop\project\\rec\\backend\\detection\\images\\'+img.name,ContentFile(img.read()))
        detect(img.name)
        if img.name in os.listdir("../images/"):
            result['status'] = 'success'
            result['message'] = [img.name.split('.')[0]+'-result.jpg']
            return JsonResponse(result)
    except Exception as e:
        result['status'] = 'error'
        result['message'] = e
        return JsonResponse(result)


def detect(request):
    '''
    调用模型进行检测,将结果保存成图片
    :param request:
    :return:
    '''
    pass
