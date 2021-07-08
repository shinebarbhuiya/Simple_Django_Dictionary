from django.shortcuts import render
import requests


# Create your views here.



def Home(request):

    word = request.GET.get('word', 'shine')
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"


    data = requests.get(url).json()

    payload = {
        'word' : data[0]['word'].title() ,
        'definition' : data[0]['meanings'][0]['definitions'][0]["definition"],
        # 'error_title' : data['title'],
        # 'error_msg' : "No Definitions Found"
        # 'daata' : data
    }

    context = { 'data' : payload}

    return render(request, 'home.html', context)

