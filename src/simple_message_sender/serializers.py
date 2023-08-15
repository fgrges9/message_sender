import uuid

from rest_framework import serializers

from bot.bot import Bot
from simple_message_sender.models import Message, ExtendedUser

bot = Bot.get_bot()


class MessageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["user"] = user
        message = Message.objects.create(**validated_data)
        if user.extendeduser.chat_id:
            bot.send_message(
                user.extendeduser.chat_id,
                f"{user.first_name}, я получил от тебя сообщение:\n" 
                f"{message.text}"
            )
        return message

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["user"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    uuid = serializers.CharField(read_only=True)

    def create(self, validated_data):

        user = ExtendedUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            uuid=uuid.uuid4(),
        )

        return user

    class Meta:
        model = ExtendedUser
        fields = ("id", "username", "password", "first_name", "uuid", )
