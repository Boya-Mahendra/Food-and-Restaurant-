"""
URL configuration for FoodAndRestorent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.homePage,name='Homepage'),
    path('restHome/',views.restahome,name='restHome'),
    path('registerFoodNormal/',views.registerFoodNormal,name='registerFoodNormal'),
    path('foodInsertMessage/',views.insertFooddataNormal,name='foodInsertMessage'),
    path('insertFoodREST/',views.insertFoodRest,name='insetFoodREST'),
    path('registerRestorentnormal/',views.registerRestorentnormal,name='registerRestorentnormal'),
    path('restorentmessage/',views.restorentData,name='restorentmessage'),
    path('insertRestorentREST/',views.insertRestorentREST,name='insertREstorentRESt/'),
    path('displayFoodREST/',views.displayFoodREST,name='displayFoodREST'),
    path('displayRestorentREST/',views.displayRestorentREST,name='displayRestorentREST'),
    path('deletFoodRESt/',views.deletFoodREST,name='deletFoodrest'),
    path('updateFopdREST/',views.updateFoodREST,name='updateFoodREST'),
    path('displayrestorentByLocRESt',views.displayRestorenByLoctREST,name='displayrestorentByLocREST'),
    path('updateRestorentREST/',views.UpdateRestorentREST,name='updateRestorentREST'),
    path('deleteRestorentREST/',views.deleteRestorentREST,name='deleteRestorentREST'),
    path('getAllRestorentData/',views.getAllRestorentData,name='getAllRestorentData'),
    path('getAllFoodData/',views.getAllFoodData,name='getAllFoodData'),
    path('displayFoodForm/',views.diaplyaFoodForm,name='displayFoodForm'),
    path('displayFoodRecord/',views.displayFoodRecord,name='displayFoodRecord'),
    path('restorecords/',views.restorentDataDisplay,name='restorecords'),
    path('updateFoodrecordform/',views.updateFoodrecordForm,name='updateFoodrecordform'),
    path('updateFoodRecords/',views.updateFoodRecords,name='updateFoodRecords'),
    path('deletFoodrecord/',views.deletFoodrecord,name='deletFoodrecord'),
    path('deletFormForFood/',views.deletFormForFood,name='deletFormForFood'),
    path('deletallFoodrecords/',views.deletallFoodRecord,name='deletallFoodrecords'),
    path('displayBasedOnlocatio/',views.displaybaseOnlocation,name='displayBasedOnlocatio'),
    path('displayBasedOnlocation/',views.restdatalocation,name='displayBasedOnlocation'),
    path('deletrestorentForem/',views.deletrestoRecordform,name='deletrestorentForem'),
    path('deletRestorentrecord/',views.deletrestorentrecod,name='deletRestorentrecord'),
    path('updaterestForm/',views.updaterestForm,name='updaterestForm'),
    path('updateDatarestaurent/',views.updatedataRestorent,name='updateDataresyaurent'),
    path('restorenrdeletAll/',views.restorentDataDeletall,name='restorentdeletAll'),
    
]
