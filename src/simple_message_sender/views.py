from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import mixins, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from simple_message_sender.models import Message, ExtendedUser
from simple_message_sender.serializers import MessageSerializer, UserSerializer


class MessageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        return Message.objects.filter(user=self.request.user)


class CreateUserView(CreateAPIView):

    model = ExtendedUser
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer

# Create your views here.
