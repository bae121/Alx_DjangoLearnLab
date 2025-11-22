from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    path ('books-list/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('token/', obtain_auth_token, name='api-token'),
    # token/ lets users get a token via POST with username and password

]