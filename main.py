
import requests


def usuario_github(username):
    url = f'https://api.github.com/users/{username}'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            user_info = {
                'Nome de usuário': data['name'],
                'Localização': data.get('location', 'N/A'),
                'Bio': data.get('bio', 'N/A')
            }
            return user_info
        elif response.status_code == 404:
            return None  # Usuário não encontrado
        else:
            return {'Erro': f'Erro ao acessar a API do GitHub: {response.status_code}'}
    except requests.exceptions.RequestException as e:
        return {'Erro de Rede': f'Erro de rede ao acessar a API do GitHub: {e}'}


print("\nGitHub Users\n")

user = input("Informe o nome do usuário -> ")

user_info = usuario_github(user)

if user_info:
    print('\n')
    for key, value in user_info.items():
        print(f"{key}: {value}")
    print('\n')
else:
    print("\nNão foi possível encontrar o usuário\n")



