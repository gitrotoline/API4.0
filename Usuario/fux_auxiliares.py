import string
from random import choice
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives


def enviarCredentials(request):
    valores = string.ascii_lowercase + string.ascii_uppercase + string.digits

    senha = ''
    for i in range(8):
        senha += choice(valores)

    print(f"Senha: {senha}ROTO | User: {request.POST['email']}")

    User.objects.create_user('Supervisor', f"{request.POST['email']}", f'{senha}ROTO')

    subject, from_email, to = _(
        "Credencias Para Acesso da API4.0 - ROTOLINE"), 'support@rotoline.com', f"{request.POST['email']}"

    html_content = f"<h3>Segue abaixo os Usuários e as Senhas para acessar API da Rotoline</h3><br>" \
                   f"<b style='font-style: italic'>USUÁRIO</b>: supervisor <b style='font-style: italic'>SENHA</b>: {senha}ROTO"

    msg = EmailMultiAlternatives(subject=subject, body="", from_email=from_email, to=[to, "ti@rotoline.com"])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


# criptografia url------------------------------------------------------------------------------------------------------
def encrypt_name(encrypt_str):
    encrypted_str = ""
    for char in encrypt_str:
        encrypted_char = chr(ord(char) + 7)  # Shift characters in the ASCII table
        encrypted_str += encrypted_char
    return encrypted_str


# Função para descriptografar uma string
def decrypt_name(decrypt_str):
    decrypted_str = ""
    for char in decrypt_str:
        decrypted_char = chr(ord(char) - 7)  # Mudar para o caractere anterior na tabela ASCII
        decrypted_str += decrypted_char
    return decrypted_str
# ----------------------------------------------------------------------------------------------------------------------
