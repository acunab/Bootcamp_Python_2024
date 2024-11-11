from django.shortcuts import render

# Create your views here.
# palindrome/views.py

from django.http import JsonResponse

def es_palindromo(request, palabra):
    # Elimina espacios y convierte a minúsculas
    palabra_sin_espacios = palabra.replace(" ", "").lower()
    
    # Verifica si la palabra es igual a su reversa
    es_palindromo = palabra_sin_espacios == palabra_sin_espacios[::-1]
    
    # Devuelve una respuesta en formato JSON con el resultado
    return JsonResponse({
        'palabra': palabra,
        'es_palindromo': es_palindromo,
        'mensaje': 'Es un palíndromo' if es_palindromo else 'No es un palíndromo'
    })