from django.urls import path

from question.views import ListQuestion, RetrieveQuestion

urlpatterns = [
    path('', ListQuestion.as_view(), name='question'),
    path('<int:pk>', RetrieveQuestion.as_view(), name='question')
]
