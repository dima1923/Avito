from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import UserSerializer, ChatSerializer, MessageSerializer, ChatShowSerializer, MessageShowSerializer
from django.db.models import Max
from .models import User,Chat,Message


class UserView(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id":serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class ChatView(viewsets.ViewSet):
    def create(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id":serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset=Chat.objects.all()
        serializer=ChatSerializer(queryset, many=True)
        return Response(serializer.data)

    def show_chats(self, request):
        serializer: ChatShowSerializer = ChatShowSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data.get('user')
            queryset = Chat.objects.annotate(max_date=Max('message__created_at')).order_by('-max_date').filter(users=user,max_date__isnull=False)
            chat_serializer = ChatSerializer(queryset, many=True)
            return Response(chat_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MessageView(viewsets.ViewSet):
    def create(self, request):
        serializer=MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"id":serializer.data.get("id")}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset=Message.objects.all()
        serializer=MessageSerializer(queryset,many=True)
        return Response(serializer.data)

    def show_message(self, request):
        serializer = MessageShowSerializer(data=request.data)
        if serializer.is_valid():
            chat = serializer.data.get('chat')
            queryset = Message.objects.filter(chat=chat).order_by('created_at')
            message_serializer = MessageSerializer(queryset, many=True)
            return Response(message_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
