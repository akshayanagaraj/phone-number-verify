
from django.shortcuts import render 
from .forms import InputForm 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import requests
#accesskey is the pyhton script used to save the api keys. Please dont hardcode your api keys, especially if your code is opensource.
from . import accesskey
import ipstack
import json
# Create your views here. 
def front(request): 
    context ={} 
    context['form']= InputForm()
    context['reply']=''
    
    if request.method == 'POST':
        #print(context['form']['phone']['value'])
        print('done')
        reply = ''
        form = InputForm(request.POST)
        print(form.data['phone'])
        phone_number = str(form.data['phone'])
        phone_number = "+91"+phone_number
        url = 'http://apilayer.net/api/validate?access_key=' + accesskey.access_key_num + '&number=' + phone_number
        response = requests.get(url)
        print (response.content)

        resp = json.loads(response.content)
        print(resp['valid'],type(resp['valid']))
        if resp['valid']==True:
            print('true')
            context['reply'] = 'the number is valid'
        else:
            print('false')
            context['reply'] = 'the number is invalid'
        print(context['reply'])
      
    return render(request, "verify/front.html", context) 




