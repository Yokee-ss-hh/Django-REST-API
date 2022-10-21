from django.urls import path
from . views import StudentDataView, StudentDataViewDetail

urlpatterns = [
    path('get_students/', StudentDataView.as_view(), name="students data view"),
    path('get_student/<int:pk>/', StudentDataViewDetail.as_view(), name="students data view"),
]

