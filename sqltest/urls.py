from django.urls import path, include
from rest_framework import routers
from . import views


# the django rest framework uses router to automatically provide the URL endpoints
router = routers.DefaultRouter()
router.register(r'myapi', views.DatabaseViewSet)

# this is our app specific url pattern to call particular views when loading particular URLs
urlpatterns = [
    # this pattern matches the base url (http://127.0.0.1:8000/) aka our homepage,
    # which is handled by the django rest framework
    path('', include(router.urls)),

    # this path is part of the rest framework and incorporates a "login" page
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # this path is a path to our original web form interface for manipulating our database
    path('webform/', views.showform, name='webform')
]
