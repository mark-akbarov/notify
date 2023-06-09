from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView

from user.serializers.login import LoginSerializer
from user.services.login import login


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return login(**serializer.validated_data)