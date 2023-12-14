from django.shortcuts import render

from twilio.rest import Client

#export OPENAI_API_KEY="Medicine"
import os


import google.generativeai as palm
from django.conf import settings
palm.configure(api_key=settings.PAML_API_KEY)


from .models import City,Hospitals

import pandas as pd
#from .forms import NameForm


def city_selection(request):
    if request.method == "POST":
        city_selected = request.POST.get('city_name_selected')
        hospital_detail = Hospitals.objects.filter(city_name=city_selected).values()
        city_names = City.objects.all()
        hospital_phone_number_store = []
        for item in hospital_detail:
            hospital_phone_number_store.append(item['hospital_number'])
        print(hospital_phone_number_store)
        data_frame1 = pd.DataFrame({'Phnumber': hospital_phone_number_store})
        with pd.ExcelWriter("pnumber.xlsx") as writer:
            data_frame1.to_excel(writer, sheet_name="Phno", index=False)

        return render(request, "index.html", {"hospital_detail": hospital_detail,"city_names_dict": city_names})


def get_name(request):
    city_names = City.objects.all()
    print(city_names)
    for item in city_names:
        print(item.city_name)

    return render(request, "index.html",{"city_names_dict": city_names})

def make_call_to_hospital(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        #form = NameForm1(request.POST)
        
        back_number = request.POST.get('callerbacknumber')
        print(back_number)
        print(type(back_number))
        if back_number != None:
            Message_On_Call ="Hi this is emergency looking for bed in Hospital please contact back on"+back_number
        else:
            Message_On_Call ="Hi this is emergency looking for bed in Hospital please contact back on 9467389160"    

        
        import pandas as pd
 
        # read by default 1st sheet of an excel file
        dataframe1 = pd.read_excel('pnumber1.xlsx')
        
        print(type(dataframe1))  
        li = dataframe1.values.tolist() 
        Num_list = []
        for i in li:
            for j in i:
                Num_list.append(j)
    
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        # account_sid = os.environ['TWILIO_ACCOUNT_SID']
        # auth_token = os.environ['TWILIO_AUTH_TOKEN']
        account_sid ="AC98822395e328672df7cdeb080d67bec3"
        auth_token ="82455b119a9a09c0e1ff73a9b7f0475c"
        client = Client(account_sid, auth_token)

        for Num in Num_list:
            print("....................................",Num)

            call = client.calls.create(
                                    twiml='<Response><Say>'+Message_On_Call+'</Say></Response>',
                                    to='+91'+str(Num),
                                    from_='+918708115075'
                                )

            print(call.sid
            ) 
            print(call.events)
            status=str(call.sid)
        if status:
            result = "Call been successfully made"
            return render(request, "index.html", {"form1": result})

    else:
       # form = NameForm1() 

       # return render(request, "call.html", {"form": form})
        return render(request, "index.html")



def Search_view(request):

    if request.method == "POST":
        message = request.POST.get('message')
        print(message)
        print(type(message))
        response = palm.chat(messages=message)
        message = response.messages[1]['content']
        return render(request, "search.html",{"message": message})
    else:
        return render(request, "search.html")








