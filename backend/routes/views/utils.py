import httpx
from fastapi import HTTPException
import config
from fastapi import Request
from jose import jwt, JWTError

def get_current_user(request: Request):
    token = request.session.get("access_token")
    if not token:
        return None
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

async def from_api(ruta: str , metodo: str = "GET", data: dict = None, headers: dict = None):
    """
    Realiza una solicitud HTTP a la API interna de la aplicación para cualquier método HTTP.

    Args:
    - ruta (str): Ruta del endpoint al que se desea hacer la solicitud.
    - metodo (str): Método HTTP (por defecto 'GET', puede ser 'POST', 'PUT', 'DELETE', 'PATCH', etc.).
    - data (dict, opcional): Datos a enviar en el cuerpo de la solicitud (solo para 'POST', 'PUT', 'PATCH', etc.).
    - headers (dict, opcional): Encabezados HTTP (por ejemplo, para pasar tokens de autenticación).

    Returns:
    - dict: Respuesta en formato JSON de la API.

    Raises:
    - HTTPException: Si la solicitud no fue exitosa, se lanza una excepción con el código de error.
    """
    url_completa = f"{config.API_BACKEND}{ruta}"

    async with httpx.AsyncClient() as client:
        try:
            # Escoge el método según el parámetro "metodo"
            if metodo.upper() == "POST":
                response = await client.post(url_completa, data=data, headers=headers)
            elif metodo.upper() == "PUT":
                response = await client.put(url_completa, data=data, headers=headers)
            elif metodo.upper() == "DELETE":
                response = await client.delete(url_completa, data=data, headers=headers)
            elif metodo.upper() == "PATCH":
                response = await client.patch(url_completa, data=data, headers=headers)
            else:  # Por defecto, si no se especifica un método válido, es un GET
                response = await client.get(url_completa, headers=headers)
            
            # Verificamos si la respuesta fue exitosa (status 200)
            response.raise_for_status()
            
            # Devolvemos la respuesta en formato JSON
            return response.json()
        
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error en la solicitud: {e}")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"Error en la API: {e.response.text}")