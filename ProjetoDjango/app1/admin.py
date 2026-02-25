from django.contrib import admin
from .models import Produto # Importa seu modelo
from .models import Marca
from .models import Categoria

admin.site.register(Produto) # Avisa ao Django para mostrar esse modelo no Admin
admin.site.register(Categoria)
admin.site.register(Marca)