import requests
from django.conf import settings

def get_api(endpoint, params=None):
    """
    Función para hacer una solicitud GET a la API.
    
    :param endpoint: El endpoint específico de la API.
    :param params: Parámetros de consulta (query parameters) que se enviarán en la URL (por defecto None).
    :return: La respuesta de la API.
    """
    url = f"{settings.API_URL}{endpoint}"
    
    try:
        respuesta = requests.get(url, params=params)  # Si hay parámetros, los agregamos a la URL
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición GET: {e}")
        return None


def post_api(endpoint, datos):
    """
    Función para hacer una solicitud POST a la API.
    
    :param endpoint: El endpoint específico de la API.
    :param datos: Los datos a enviar en la solicitud POST.
    :return: La respuesta de la API.
    """
    url = f"{settings.API_URL}{endpoint}"
    
    try:
        # Usamos json para enviar datos de forma adecuada en POST
        respuesta = requests.post(url, json=datos)  # Se pasan los datos como JSON
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición POST: {e}")
        return None


def put_api(endpoint, datos):
    """
    Función para hacer una solicitud PUT a la API.
    
    :param endpoint: El endpoint específico de la API.
    :param datos: Los datos a enviar en la solicitud PUT.
    :return: La respuesta de la API.
    """
    url = f"{settings.API_URL}{endpoint}"
    
    try:
        # Usamos json para enviar datos de forma adecuada en PUT
        respuesta = requests.put(url, json=datos)  # Se pasan los datos como JSON
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición PUT: {e}")
        return None


def delete_api(endpoint, params=None):
    """
    Función para hacer una solicitud DELETE a la API.
    
    :param endpoint: El endpoint específico de la API.
    :param params: Parámetros de consulta (query parameters) que se enviarán en la URL (por defecto None).
    :return: La respuesta de la API.
    """
    url = f"{settings.API_URL}{endpoint}"
    
    try:
        # Si hay parámetros, se agregan a la URL
        respuesta = requests.delete(url, params=params)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            respuesta.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la petición DELETE: {e}")
        return None
