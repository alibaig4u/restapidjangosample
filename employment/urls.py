from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from employment import views

urlpatterns = [
    path('employees/', views.employee_list),
    path('employees/<int:pk>', views.employee_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)