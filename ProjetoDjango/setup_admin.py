import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetoDjango.settings')
django.setup()

from django.contrib.auth.models import User

# Cria o superusuário se ele não existir
username = 'admin'
email = 'admin@email.com'
password = 'sua_senha_secreta' # <--- MUDE ISSO DEPOIS!

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Usuário {username} criado com sucesso!")
else:
    print(f"Usuário {username} já existe.")