from rest_framework import generics
from .models import Messages
from .serializers import MessageSerializer
from .utils import send_telegram_message


class MessageView(generics.CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = request.data
        message_text = "Вопросы:\n"
        for key, value in data.items():
            if key in ["username", "phone"]:
                message_text += f"{key}: {value}\n"
        send_telegram_message(message_text)
        return response