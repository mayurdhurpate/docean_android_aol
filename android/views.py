from django.shortcuts import render
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
import json
from django.shortcuts import render
from android.models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import base64
import django.core.files
from PIL import Image
import cStringIO
import datetime
import dropbox
# Create your views here.

def home(title,text,sender,msg_id,topic,created):
    uids = []
    users = User.objects.all().order_by('-id')
    for user in users:
        uids.append(user.token)
    notis = Noti.objects.all().order_by('-id')
    noti = notis[0]
    timeshow = str(created.hour)+":"+str(created.minute)
    dateshow = str(created.day)+"-"+str(created.month)+"-"+str(created.year)
    
    url = 'https://gcm-http.googleapis.com/gcm/send'
    #payload = { "notification": {"title": title,"icon":"@drawable/myicon","text": text,"click_action":"MAIN"},"registration_ids" : uids}
    payload = {"data":{"message1":text,"title":title,"sender":sender,"id":msg_id,"topic":topic,"type":"message","time":timeshow,"date":dateshow},"registration_ids":uids}
    headers = {'content-type': 'application/json','Authorization':'key='+noti.api_key}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return json.loads(r.content)

@csrf_exempt
def register(request):
    if request.method == "POST" and request.POST['passkey'] == "hellolastry":
        try:
            u = User.objects.get(email=request.POST["email"])
        except:
            u = User()


        u.name = request.POST["name"]
        u.token = request.POST["token"]
        u.email = request.POST["email"]
        u.phone_no = request.POST["phone_no"]
        u.image_url = request.POST["image_url"]
        u.social_id = request.POST["social_id"]
        u.role = ""

        if(u.email=="null"):
            return HttpResponse(json.dumps({"message":"Null Data","success":"false"}),content_type="application/json") 
        
        u.save()
        return HttpResponse(json.dumps({"message":"User Registered","success":"true"}),content_type="application/json")
    else:
        return HttpResponse("Validation Failed")


@csrf_exempt
def message_receive(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        try:
            x = User.objects.get(email=request.POST["email"])
        except:
            data1 = {}
            data1["action"]="broadcast_msg"
            data1["error"]="true"
            return HttpResponse(json.dumps(data1), content_type='application/json')
        msg = Message()
        msg.sender = request.POST['username']
        msg.message = request.POST['bmsg']
        msg.token = request.POST["token"]
        msg.title = request.POST["bmsg_title"]
        msg.topic = request.POST['topic']
        msg.created = timezone.now()
        msg.save()
        data = home(msg.title,msg.message,msg.sender,msg.id,msg.topic,msg.created)
        msg.message_id = data['multicast_id']
        msg.save()
        data["action"]="broadcast_msg"
        data["error"]="false"
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data["action"]="broadcast_msg"
        data["error"]="true"
        return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def contacts_data(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        data = {"contacts":[],"action":"fetch_contacts"}
        users = User.objects.all().order_by('name')
        for user in users:
            user_dict = {}
            user_dict["name"] = user.name
            user_dict["email"] = user.email
            user_dict["phone_no"] = user.phone_no
            user_dict["image_url"] = user.image_url
            user_dict["role"] = user.role
            data["contacts"].append(user_dict)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Validation Failed")

@csrf_exempt
def message_data(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        data = {"messages":[],"action":"fetch_messages"}
        messages = Message.objects.all().order_by('-id')
        for message in messages:
            msg_dict = {}
            msg_dict["sender"] = message.sender
            msg_dict["message"] = message.message
            msg_dict["id"] = message.id
            msg_dict["topic"] = message.topic
            msg_dict["title"] = message.title
            msg_dict["time"] = str(message.created.hour)+":"+str(message.created.minute)
            msg_dict["date"] = str(message.created.day)+"-"+str(message.created.month)+"-"+str(message.created.year)
            data["messages"].append(msg_dict)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Validation Failed")

@csrf_exempt
def add_topic(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        topic = request.POST["topic"]

        uids = []
        users = User.objects.all().order_by('-id')
        for user in users:
            uids.append(user.token)
        notis = Noti.objects.all().order_by('-id')
        noti = notis[0]
        url = 'https://gcm-http.googleapis.com/gcm/send'
        payload = {"data":{"topic":topic,"type":"add_topic"},"registration_ids":uids}
        headers = {'content-type': 'application/json','Authorization':'key='+noti.api_key}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        data = json.loads(r.content)
        data["action"]="add_topic"
        data["error"]="false"
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Validation Failed") 

@csrf_exempt
def image_upload(request):
    if request.method == 'POST' and request.POST['passkey'] == "hellolastry":
        pic = cStringIO.StringIO()
        image_string = cStringIO.StringIO(base64.b64decode(request.POST['image']))
        image = Image.open(image_string)
        image.save(pic, image.format, quality = 100)
        pic.seek(0)
        x = datetime.datetime.now()
        ttt = x.strftime('%Y%m%d_%H%M%S')
        client = dropbox.client.DropboxClient('9ZP72jucDXQAAAAAAAABfWkVODGSeqPl0N2oPaiQpCuTHYh9JMyJfE5ZKXFvEy58')
        response = client.put_file("aol/" +ttt +"." +image.format,  pic)
        url = ''
        url = client.share(response['path'], short_url=False)['url'].replace('www.dropbox.com','dl.dropboxusercontent.com')
        print url
        return HttpResponse(json.dumps(url), content_type='application/json')
