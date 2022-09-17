from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view('Get')
def getData(request):
    person = {'name':'Haarry','age':22}

    return Response(person)