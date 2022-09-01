from django.urls import path
from .views import HouseList, HouseDetail, HouseCreate, HouseUpdate

urlpatterns = [
    path("", HouseList.as_view(), name="house_list"),
    path("<int:pk>", HouseDetail.as_view(), name="house_detail"),
    path("create/", HouseCreate.as_view(), name="house_create"),
    path("update/<int:pk>", HouseUpdate.as_view(), name="house_update")
]
