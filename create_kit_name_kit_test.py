import sender_stand_request
import data
#----------------------------------------------------------------------- Importa archivo data y sender
def get_user_body(first_name):
    current_body= data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body
#----------------------------------------------------------------------- Se crea usuario
def positive_assert_user(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1
#----------------------------------------------------------------------- Se verifica que el usuario se creo de forma exitosa
def get_new_user_token():
    user_body = get_user_body("firstName")
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token
#---------------------------------------------------------------------- Extrae token y lo almacena en la variable
def get_kit_body(name):
    current_body= data.kit_body.copy()
    current_body["name"] = name
    return current_body
#----------------------------------------------------------------------- Se crea kit
def positive_assert_kit(name):
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_response.status_code == 201
#-----------------------------------------------------------------------  optimiza pruebas positivas
def negative_assert_kit(kit_body):
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

def negative_assert_missing_name_kit(name):
    kit_body = data.kit_body.copy()
    kit_body.pop(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert kit_response.status_code == 400
#----------------------------------------------------------------------- optimiza pruebas negativas
def test_create_kit_1_letter_in_name_get_succes_response():
    positive_assert_kit("a")

def test_create_kit_511_letter_in_name_get_succes_response():
    positive_assert_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_special_character_in_name_get_succes_response():
    positive_assert_kit("#$%")

def test_create_kit_with_space_in_name_get_succes_response():
    positive_assert_kit("A AAA AAAAA")

def test_create_kit_with_numbers_in_name_get_succes_response():
    positive_assert_kit("1235")
#------------------------------------------------------------------------- pruebas positivas
def test_create_kit_with_special_characters_in_name_get_error_response():
    negative_assert_kit("")

def test_create_kit_with_512_characters_in_name_get_error_response():
    negative_assert_kit("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_with_numbers_in_name_get_error_response():
    negative_assert_kit(1523)

def test_create_kit_no_format_in_name_get_error_response():
    negative_assert_missing_name_kit("name")