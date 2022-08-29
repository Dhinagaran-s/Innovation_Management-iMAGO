# Api Views
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


from .serializers import AnswerSerializer, QuestionSerializer, TagSerializer
from scspi_app_1.models import Question



@api_view(['POST',])
# @permission_classes((IsAuthenticated,))
def create_question_api(request):
    if request.method != 'POST':
        return Response({'request':'Request must be POST'})
    try:
        serializer = QuestionSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            question_obj = serializer.save()
            data['response'] = 'Successfully posted a Question'
            data['question'] = question_obj.question
        else:
            data = serializer.errors
        return Response(data)
    except Exception as exp:
        print(exp)
        return Response({'response':'Some error occurred, please contact admin'})



@api_view(['POST',])
def create_answer_api(request):
    if request.method != 'POST':
        return Response({'request':'Request must be POST'})
    try:
        serializer = AnswerSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            answer_obj = serializer.save()
            data['response'] = 'Successfully answered a question'
            data['question'] = str(Question.objects.get(id=answer_obj.question).question)
            data['answer'] = answer_obj.answer
        else:
            data = serializer.errors
        return Response(data)
    except Exception as exp:
        print(exp)
        return Response({'response':'Some error occurred, please contact admin'})



@api_view(['POST',])
def create_tag_api(request):
    if request.method != 'POST':
        return Response({'request':'Request must be POST'})
    try:
        serializer = TagSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            tag_obj = serializer.save()
            data['response'] = 'Successfully created a tag'
            data['tag'] = tag_obj.tag_name
            data['description'] = tag_obj.tag_description
        else:
            data = serializer.errors
        return Response(data)
    except Exception as exp:
        print(exp)
        return Response({'response':'Some error occurred, please contact admin'})



class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('question', 'description')









