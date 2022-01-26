from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import base64
import os
import re
import cv2
import json
import numpy as np
from datetime import date,datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from resultprocessing.models import crowdmessage
from resultprocessing.models import syokudo_menu
from resultprocessing.models import place
from resultprocessing.models import rest_place
from resultprocessing.models import pc_classroom
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Max
from django.core.serializers import serialize
from django.http import JsonResponse

def index_view(request):

    html = 'suzukiproject'
    return HttpResponse(html)

@api_view(['POST',])
def photoin(request):
    data = request.body
    data = json.loads(data)
    ai_data_img = []
    for i in data['img']:
        image_b64 = i
        image_decode= base64.b64decode(image_b64)
        nparr = np.fromstring(image_decode,np.uint8)
        img_np = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
        dir_name = date.today().__str__().replace('_','_',2)
        dirs = os.path.join(settings.MEDIA_ROOT,dir_name)
        img_name = re.sub(r':|\.', '', datetime.now().__str__().split(' ')[1]) + '.png'

        if not os.path.isdir(dirs):
            os.makedirs(dirs)

        image = cv2.imwrite(os.path.join(dirs,img_name),img_np)

        #保存した画像を読み込み、AIチームへ送信
        f = open(os.path.join(dirs,img_name),'rb')
        base64_data = base64.b64encode(f.read())
        f.close()
        base64_data = base64_data.decode()

        ai_data_img.append(base64_data)

    ai_data = {'place_id':1,'then_time':data['then_time'],'img':ai_data_img}
    r = requests.post("http://127.0.0.1:8000/ai_test/", headers={'Content-Type': 'application/json', }, data=json.dumps(ai_data))
    #result = 'success'
    return Response()

#ダミーデータ送信
def dummy(request):
    #フォルダ指定
    path = "media/2021-10-07"
    files = os.listdir(path)
    ai_data_img = []
    for file in files:
        f = open(path+"/"+file,'rb')
        base64_data = base64.b64encode(f.read())
        f.close()
        base64_data = base64_data.decode()
        ai_data_img.append(base64_data)

    ai_data = {'place_id':1,'then_time':datetime.now().strftime("%Y%m%d_%H%M%S"),'img':ai_data_img}
    r = requests.post("http://127.0.0.1:8000/ai_test/", headers={'Content-Type': 'application/json', }, data=json.dumps(ai_data))

    html="<h1>sucess<h1>"
    return HttpResponse(html)

@api_view(['POST',])
@csrf_exempt
def ai_test(request):
    data = request.body.decode('utf-8')
    data = json.loads(data)
    for i in data['img']:
        image_b64 = i
        image_decode= base64.b64decode(image_b64)
        nparr = np.fromstring(image_decode,np.uint8)
        img_np = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
        dir_name = date.today().__str__().replace('_','_',2)
        dirs = os.path.join(settings.MEDIA_ROOT,dir_name)
        img_name = re.sub(r':|\.', '', datetime.now().__str__().split(' ')[1]) + '.png'

        if not os.path.isdir(dirs):
            os.makedirs(dirs)

        image = cv2.imwrite(os.path.join(dirs,img_name),img_np)

    result = 'success'
    return Response(result)



def photoout(request):

    html = "<h1>test2-photoout</h1>"
    return HttpResponse(html)

#webサイトのようにformで画像を受け取る
@csrf_exempt
def phototest(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    elif request.method == "POST":
        a_file = request.FILES['myfile']
        print("ファイル名は：",a_file.name)
        filename = os.path.join(settings.MEDIA_ROOT,a_file.name)
        with open(filename,'wb') as test:
            data = a_file.file.read()
            test.write(data)
        return HttpResponse(a_file.name + "送信成功")


def syokuji(request):
    if request.method == 'GET':
        n=0
        for b in range(5):
            dat=crowdmessage.objects.all()
            data1=dat.order_by('-then_time')
            crowd=data1[n].crowd
            then_time=data1[n].then_time
            place_id=data1[n].place_id
            id=data1[n].id
            id11list =data1.filter(place_id__exact=11) # idが11
            id11=id11list[0]
            id1list =data1.filter(place_id__exact=1) # idが11
            id1=id1list[0]

            if id1.crowd==0:
                id1data="空いています"
            elif id1.crowd==1:
                id1data="少し混んでいます"
            elif id1.crowd==2:
                id1data="混んでいます"
            elif id1.crowd==-1:
                id1data="エラー"

            if id11.crowd==0:
                id11data="空いています"
            elif id11.crowd==1:
                id11data="少し混んでいます"
            elif id11.crowd==2:
                id11data="混んでいます"
            elif id11.crowd==-1:
                id11data="エラー"

            context = {
                'text': '情報取得時間',
                "data1":data1,
                'then_time': then_time,
                "crowd":crowd,
                "place_id":place_id,
                "id":id,
                "id11":id11,
                "id1":id1,
                "id11data":id11data,
                "id1data":id1data,

            }


            return render(request,'syokuji.html',context)

            n=n+1


def pc(request):
    if request.method == 'GET':
        n=0
        for b in range(5):
            dat=crowdmessage.objects.all()
            data1=dat.order_by('-then_time')
            crowd=data1[n].crowd
            then_time=data1[n].then_time
            place_id=data1[n].place_id
            id=data1[n].id
            id33list =data1.filter(place_id__exact=33)
            id33=id33list[0]
            id3list =data1.filter(place_id__exact=3)
            id3=id3list[0]

            if id3.crowd==0:
                id3data="空いています"
            elif id3.crowd==1:
                id3data="少し混んでいます"
            elif id3.crowd==2:
                id3data="混んでいます"
            elif id3.crowd==-1:
                id3data="エラー"

            if id33.crowd==0:
                id33data="空いています"
            elif id33.crowd==1:
                id33data="少し混んでいます"
            elif id33.crowd==2:
                id33data="混んでいます"
            elif id33.crowd==-1:
                id1data="エラー"

            context = {
                'text': '情報取得時間',
                "data1":data1,
                'then_time': then_time,
                "crowd":crowd,
                "place_id":place_id,
                "id":id,
                "id33":id33,
                "id3":id3,
                "id3data":id3data,
                "id33data":id33data,
            }
            return render(request,'pc.html',context)
            n=n+1

def menu_green(request):

    menu_curry = syokudo_menu.objects.filter(place_id=1,kind="カレー")
    menu_noodles = syokudo_menu.objects.filter(place_id=1,kind="麺類")
    menu_donmono = syokudo_menu.objects.filter(place_id=1,kind="どんもの")
    menu_set = syokudo_menu.objects.filter(place_id=1,kind="セット")
    menu_others = syokudo_menu.objects.filter(place_id=1,kind="その他")
    name = menu_curry.get(id = 1)
    return render(request,'menu_green.html',locals())

def menu_ikuta(request):

    menu_noodles = syokudo_menu.objects.filter(place_id=11,kind="麺類")
    menu_donmono = syokudo_menu.objects.filter(place_id=11,kind="どんもの")
    menu_set = syokudo_menu.objects.filter(place_id=11,kind="セット")
    menu_others = syokudo_menu.objects.filter(place_id=11,kind="その他")
    name = menu_set.get(id = 39)
    return render(request,'menu_ikuta.html',locals())

def kyukei(request):
    if request.method == 'GET':
        n=0
        for b in range(5):
            dat=crowdmessage.objects.all()
            data1=dat.order_by('-then_time')
            crowd=data1[n].crowd
            then_time=data1[n].then_time
            place_id=data1[n].place_id
            id=data1[n].id

            id22list =data1.filter(place_id__exact=22) # idが11
            id22=id22list[0]
            id2list =data1.filter(place_id__exact=2) # idが11
            id2=id2list[0]

            if id2.crowd==0:
                id2data="空いています"
            elif id2.crowd==1:
                id2data="少し混んでいます"
            elif id2.crowd==2:
                id2data="混んでいます"
            elif id2.crowd==-1:
                id2data="エラー"

            if id22.crowd==0:
                id22data="空いています"
            elif id22.crowd==1:
                id22data="少し混んでいます"
            elif id22data.crowd==2:
                id22data="混んでいます"
            elif id22.crowd==-1:
                id22data="エラー"

            context = {
                'text': '情報取得時間',
                "data1":data1,
                'then_time': then_time,
                "crowd":crowd,
                "place_id":place_id,
                "id":id,
                "id22":id22,
                "id2":id2,
                "id22data":id22data,
                "id2data":id2data,

            }

            return render(request,'kyukei.html',context)
            n=n+1


def ikuta(request):
    if request.method == 'GET':
        return render(request,'menu_ikuta.html')

def green(request):
    if request.method == 'GET':
        return render(request,'menu_green.html')

#アプリ
def homepage(request):
    if request.method == 'GET':
        return render(request,'homepage.html')

#json形式をxmlに変換する
import xmltodict
@csrf_exempt
def ai(request):
    data = json.loads(request.body)
    new_data = {"xml":data}
    xml_data = xmltodict.unparse(new_data)

    print('DEBBUG:',xml_data)

    r = requests.post("http://127.0.0.1:8000/resultprocessing/xmltodb/",headers = {'Content-Type': 'application/xml'},data = xml_data)

    return HttpResponse()

def api(request):
    api = crowdmessage.objects.order_by('-crowd')
    api_json = json.loads(serialize("json",api,fields=('crowd','then_time','place_id')))
    result = {'api_json':api_json}
    return JsonResponse(result)
