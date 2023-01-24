from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView

from .serializers import UrlSerializer
from .models import Requests, Url


class CreateUrlAPIView(CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def get_serializer_context(self):
        # if self.request.user.is_anonymous :
        #     raise AuthenticationFailed('your not logged in as user')    
        return {'user_id': self.request.user.id}