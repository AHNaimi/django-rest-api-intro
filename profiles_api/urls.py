from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_viewset',views.HelloViewSet, basename='hello_viewset')
router.register('profile', views.UserProfileViewSet)


app_name = 'api'
urlpatterns = [
    path('hello/', views.HelloApiView.as_view(), name='hello'),
    path('login/',views.UserLoginApi.as_view()),
    path('', include(router.urls))
]
""" for path(login/) you have to insert email instead of username in Username field """
