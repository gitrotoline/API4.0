from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import AccessToken

from Usuario.models import Token_user


class CustomTokenObtainSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        try:
            # Verifica se o token já existe para o usuário
            user_token = Token_user.objects.get(user=user)
            access_token = user_token.token
        except Token_user.DoesNotExist:
            # Gera um novo token de acesso
            access_token = str(AccessToken.for_user(user))
            # Armazena o token no banco de dados
            Token_user.objects.create(user=user, token=access_token)

        return access_token

    def validate(self, attrs):
        # Valida as credenciais do usuário
        data = super().validate(attrs)
        # Retorna apenas o token de acesso
        return {'access': self.get_token(self.user)}
