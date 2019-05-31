from django.shortcuts import render
import pymysql
import uuid
from django.http import HttpResponse, JsonResponse
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
        print("--sql--",sql)
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
