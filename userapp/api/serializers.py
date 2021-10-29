from django.contrib.auth.models import User
from rest_framework import serializers

from userapp.models import Textsnippet,Tag


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2 :
            raise serializers.ValidationError({'error':'Password should be the same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email id already exists'})
        
        account = User(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            )
        account.set_password(password)
        account.save()

        return account

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TextsnippetSerializer(serializers.ModelSerializer):

    tag = TagSerializer
    class Meta:
        model = Textsnippet
        fields = '__all__'

    def save(self):
        user = self.request.user
        input_tag = self.validated_data['tag']
        title = self.validated_data['title']
        text = self.validated_data['text']
        if input_tag:

            try:
                tag = Tag.objects.get(title=input_tag)
            except:
                tag = Tag(title=input_tag)
                tag.save()
        if tag:

            textsnippet = Textsnippet(user=user,tag=tag,title=title, text=text)
        else:
            textsnippet = Textsnippet(user=user,title=title, text=text)
        textsnippet.save()
        return textsnippet
