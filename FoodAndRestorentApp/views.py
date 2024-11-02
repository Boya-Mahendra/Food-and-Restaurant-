from django.shortcuts import render,redirect
from .models import Food
from .models import Restorent
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import FoodSerilaizer
from .serializer import RestorentSerializer
from django.http import HttpResponse
# from rest_framework import JSONrensderer
# Create your views here.



def homePage(request):
    return render(request,'homepage.html')


def restahome(request):
    return render (request,'restHome.html')


def registerFoodNormal(request):
    return render(request,'foodregister.html')

def insertFooddataNormal(request):
    foodid=request.POST.get('fid')
    foodName=request.POST.get('fname')
    foodPrice=request.POST.get('fprice')
    fdata=Food(Fid=foodid,FoodName=foodName,FoodPrice=foodPrice)
    fdata.save()
    return render (request,'foodmessage.html')


def diaplyaFoodForm(request):
    return render(request,'getFoodForm.html')
def displayFoodRecord(request):
    # foodId=request.POST.get('fid')
    record=Food.objects.all()
    return render(request,'foodRecordDisplay.html',{'records':record})

def updateFoodrecordForm(request):
    return render(request,'updatefood.html')
def updateFoodRecords(request):
    foodId=request.POST.get('foodid')
    foodName=request.POST.get('foodname')
    foodprice=request.POST.get('foodprice')
    uodate=Food.objects.filter(Fid=foodId).update(FoodName=foodName,FoodPrice=foodprice)
    return redirect('displayFoodRecord')

def deletFormForFood(request):
    return render(request,'deleteFoodData.html')
def deletFoodrecord(request):
    foodid=request.POST['foodrecord']
    data=Food.objects.filter(Fid=foodid)
    data.delete()
    return redirect('displayFoodRecord')


def deletallFoodRecord(request):
    alldatd=Food.objects.all().delete()
    return redirect(displayFoodRecord)
# ---------------------------restorent-------------------------------------------------




def registerRestorentnormal(request):
    return render(request,'registerRestorent.html')

def restorentData(request):
    restorentId=request.POST.get('rid')
    restorentName=request.POST.get('rname')
    restorentlocation=request.POST.get('rlocation')
    restorent=Restorent(RId=restorentId,RName=restorentName,RLocation=restorentlocation)
    restorent.save()
    return render(request,'restorentMessage.html')


def displaybaseOnlocation(request):
    return render(request,'restlocation.html')
def restdatalocation(request):
    location=request.POST.get('rloc')
    locdata=Restorent.objects.filter(RLocation=location)
    return render(request,'locationdetails.html',{'locdata':locdata})


def restorentDataDisplay(request):
    all=Restorent.objects.all()
    return render(request,'restorecords.html',{'data':all})

def deletrestoRecordform(request):
    return render(request,'deletrestorentrecodForm.html')
def deletrestorentrecod(request):
    restId=request.POST.get('rid')
    restorentid=Restorent.objects.filter(RId=restId)
    restorentid.delete()
    return redirect('restorecords')

def updaterestForm(request):
    return render(request,'updaterestorentForm.html')
def updatedataRestorent(request):
    restorentId=request.POST.get('rid')
    restorentName=request.POST.get('rname')
    restorentlocation=request.POST.get('rlocation')
    restorent=Restorent.objects.filter(RId=restorentId).update(RName=restorentName,RLocation=restorentlocation)
    return redirect('restorecords')

def restorentDataDeletall(request):
    all=Restorent.objects.all()
    all.delete()
    return redirect('restorecords')
# ---------------------------food-rest-------------------------------------------------
@api_view(['POST'])
def insertFoodRest(request):
    food=FoodSerilaizer(data=request.data)
    if food .is_valid():
        food.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GEt'])
def displayFoodREST(request):
    food=Food.objects.filter(Fid=101).get()
    return Response(FoodSerilaizer(food).data)


@api_view(['GET'])
def deletFoodREST(rquest):
    food=Food.objects.filter(Fid=105).get()
    food.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GEt'])
def updateFoodREST(request):
    food=Food.objects.filter(Fid=101).update(FoodName='idli')
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def getAllFoodData(request):
    food=FoodSerilaizer(Food.objects.all(),many=True)
    return Response(food.data)

# ---------------------------food-Restorent-------------------------------------------------
@api_view(['POST'])
def insertRestorentREST(request):
    restorent=RestorentSerializer(data=request.data)
    if restorent.is_valid():
        restorent.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def displayRestorentREST(request):
    restorent=Restorent.objects.filter(RId=101).get()
    return Response(RestorentSerializer(restorent).data)

@api_view(['GET'])
def displayRestorenByLoctREST(request):
    restorent=Restorent.objects.filter(RLocation='vistrun business hotel').get()
    return Response(RestorentSerializer(restorent).data)


@api_view(['GET'])
def UpdateRestorentREST(request):
    restorent=Restorent.objects.filter(RId=101).update(RLocation='national college')
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def deleteRestorentREST(request):
    restorent=Restorent.objects.filter(RId=101)
    restorent.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getAllRestorentData(request):
    serializ=RestorentSerializer(Restorent.objects.all() ,many=True)
    return Response(serializ.data)





# ----------------------------------------------------------------------------------

