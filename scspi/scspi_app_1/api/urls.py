# Api Urls
from django.urls import path

from . import views

app_name = 'scspi'


urlpatterns = [
    path('ask_question/', views.create_question_api, name='ask_question'),
    path('answer_question/',views.create_answer_api, name='answer_question'),
    path('create_tag/',views.create_tag_api, name='create_tag'),
    path('search_question/',views.QuestionListAPIView.as_view(), name='search_question'),
]
