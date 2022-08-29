from rest_framework import serializers

from scspi_app_1.models import CustomUser, Question, Answer, Tag





class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id','user','question','description','image','tags']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','question','answer','image']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','tag_name','tag_description']


class RegisterAPIUsers(serializers.ModelSerializer):

    passsword_2 = serializers.CharField(style={'input_type':'password_2'}, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['email','username','password','password_2','user_type']
        extra_kwargs = {
            'password':{'write_only': True}
        }

        def save(self):
            api_user = CustomUser(
                email = self.validated_data['email'],
                username = self.validated_data['username'],
                user_type = 5
            )
            password = self.validated_data['password']
            password_2 = self.validated_data['password_2']

            if password != password_2:
                raise serializers.ValidationError({'password':'Password must match'})
            api_user.set_password(password)
            api_user.save()
            return api_user
























