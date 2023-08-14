from django.shortcuts import render
from rest_framework.views import APIView
from App.models import React
from rest_framework.response import Response
from App.serializers import Reactserializers
# Create your views here.

class Reactview (APIView):
    def get(self, request):
        output = [{"Employee": output.Employee,
                   "Department": output.Department}
                  for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = Reactserializers(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

