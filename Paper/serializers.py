from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import BlogModel, DocxModel, CatModel, FAQModel, ListModel


class RegSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, validators=[validate_password], write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, passwd):
        if passwd['password'] != passwd['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords didn't match. Please Retry"})

        return passwd

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], username=validated_data['username'] )
        user.set_password(validated_data['password'])
        user.save()

        return user


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatModel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class DocxSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocxModel
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')


class ListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    status = serializers.ReadOnlyField(source='status.status')
    title = serializers.ReadOnlyField(source='title.title')

    class Meta:
        model = ListModel
        fields = ('user', 'title', 'status', 'expected_EndDate')

