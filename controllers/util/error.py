import enum

class Error(enum.Enum):
    
    # Error Tokens
    TOKEN_INEXISTENTE = 'El Token no existe'
    TOKEN_INVALIDO = 'El token es invalido'
    
    # Error cuenta
    CUENTA_INEXISTENTE = 'La cuenta no existe'
    CUENTA_INVALIDA = 'La cuenta es invalida'
    EMAIL_EXISTENTE = 'El email ya existe'
    
    # Error persona
    DNI_EXISTENTE = 'El dni ya existe'

    # Error Producto
    PRODUCTO_EXISTENTE = 'El producto ya existe'
    PRODUCTO_INEXISTENTE = 'El producto no existe'


def json_error(error, status_code):
    return {'msg'  : 'Error',
            'code' : status_code,
            'info' : error,
    }