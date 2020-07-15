from django.shortcuts import render
import json

from json import dumps
from django.http import JsonResponse
from .models import PersonalDetails
# Create your views here.


def home(request):
    personalDetails = PersonalDetails.objects.all()
    finalData = {}
    for data in personalDetails:
        finalData[data.roll_no] = {'first_name': data.first_name,
                          'last_name': data.last_name, 'email': data.email, 'date_of_birth': str(data.date_of_birth), 'hobbies': data.hobbies}

    finalData = dumps(finalData)
    context = {'pd': personalDetails, 'finalData': finalData}
    return render(request, 'mysite/base.html', context)


def saveDetails(request):
    data = json.loads(request.body)
    print(data['date_of_birth'][:10])
    PersonalDetails.objects.create(
        roll_no=data['roll_no'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        date_of_birth=data['date_of_birth'][:10],
        hobbies=data['hobbies']

    )

    return JsonResponse('Data Transferes', safe=False)
