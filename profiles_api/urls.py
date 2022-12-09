from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_viewset',views.HelloViewSet, basename='hello_viewset')


app_name = 'api'
urlpatterns = [
    path('hello/', views.HelloApiView.as_view(), name='hello'),
    path('', include(router.urls))
]