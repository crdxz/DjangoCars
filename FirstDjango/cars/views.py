from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import cars

# Create your views here
@api_view(["POST", "GET"])
def getCars(request,*args,**kwarfs):
    
    if request.method == "POST":
        
        carname = request.data.get("carname")
        model = request.data.get("model")
        year = request.data.get("year")
        hp = request.data.get("hp")
        new = request.data.get("new")
        
        car = cars(carname=carname, model=model, year=year, hp=hp, new=new)
        car.save()
        
        return Response({"data" : {
            "carname" : car.carname,
            "model" : car.model,
            "year" : car.year,
            "hp" : car.hp,
            "new" : car.new
        }})
    
    if request.method == "GET":
        _cars = cars.objects.all()
        return Response({"data" : [{
            "carname" : car.carname,
            "model" : car.model,
            "year" : car.year,
            "hp" : car.hp,
            "new" : car.new
            }for car in _cars]})