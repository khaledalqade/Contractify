from django.urls import path
from rest_framework import routers
from django.conf.urls import include
#from .views import MealViewSet, RatingViewSet, UserViewSet
from .views import UserViewSet, ContractViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
#router.register('meals', MealViewSet)
#router.register('ratings', RatingViewSet)
router.register('contracts', ContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
]