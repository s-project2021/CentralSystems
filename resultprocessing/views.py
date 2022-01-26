from django.shortcuts import render
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from django.views.decorators.csrf import csrf_exempt
from .models import crowdmessage
from .models import syokudo_menu
# Create your views here.
@csrf_exempt
def xmltodb(request):
    xml_string = request.body.decode('utf-8')
    root = ET.fromstring(xml_string)

    for i in root.iter('xml'):
        p_id = i.find('place_id').text
        t_time = i.find('then_time').text
        cr = i.find('crowd').text
        writedb = crowdmessage(place_id=p_id,then_time=t_time,crowd=cr)
        writedb.save()

    return HttpResponse()

def message(request):

    message = crowdmessage.objects.order_by('-crowd')
    return render(request,'message.html', locals())

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
