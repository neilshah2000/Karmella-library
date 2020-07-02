from django.urls import path
from rest_framework import routers
from . import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('api/', include(router.urls)),
]