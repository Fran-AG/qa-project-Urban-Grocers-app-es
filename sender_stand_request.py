import configuration
import requests
import data

def post_new_user(body): #Crea un nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def get_users_table(): #obtiene todos los usuarios de la base de datos
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

user_response = post_new_user(data.user_body)
print("Usuario:", user_response.status_code)
print(user_response.json())

auth_token = user_response.json()["authToken"]

def post_new_kit(body, auth_token):
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT,
                         json=body,
                         headers=headers_with_auth)

kit_response = post_new_kit(data.kit_body, auth_token)
print("Kit:", kit_response.status_code)
print(kit_response.json())