from django.urls import path
from . import views


urlpatterns = (
    path('books/', views.ListBooksView.as_view(), name='books'),
    path('books/<int:id>', views.DetailBookView.as_view(), name='details')
)