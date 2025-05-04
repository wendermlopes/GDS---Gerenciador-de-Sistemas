import sys
import os

# Adiciona o diretório onde este script está (a raiz do projeto) ao sys.path
# Isso simula a ação que manage.py faz para garantir que o projeto possa ser importado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
     sys.path.append(BASE_DIR)


print(f"Diretório base do projeto adicionado ao sys.path: {BASE_DIR}")

try:
    print("\nTentando importar cliente_web.settings...")
    # Esta importação só funcionará se a pasta 'cliente_web' existir dentro de BASE_DIR
    from cliente_web import settings
    print("Importação bem-sucedida!")
    print(f"DEBUG: Módulo de settings do Django carregado: {settings.SETTINGS_MODULE}")
except ModuleNotFoundError as e:
    print(f"\nErro de importação: {e}")
    print(f"Não foi possível encontrar o módulo 'cliente_web'.")
    print(f"Verifique se a pasta 'cliente_web' existe *exatamente* com este nome dentro de '{BASE_DIR}'.")
    print("Verifique a grafia e o uso de maiúsculas/minúsculas.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado durante a importação: {e}")

print(f"\nConteúdo atual de sys.path:")
for p in sys.path:
    print(p)