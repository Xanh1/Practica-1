schema_crear_persona = {
    "type": "object",
    "required": ["dni", "nombre", "apellido", "email", "clave"],
    "properties": {
        "dni": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10
        },
        "nombre": {
            "type": "string"
        },
        "apellido": {
            "type": "string"
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "clave": {
            "type": "string"
        }
    }
}


schema_login = {
    "type": "object",
    "required" : ["email", "clave"],
    "properties": {
        "email" : {
            "type" : "string"
        },
        "clave" : {
            "type" : "string"
        }
    }
}


schema_crear_producto = {
    "type": "object",
    "required" : ["nombre", "descripcion"],
    "properties": {
        "nombre" : {
            "type" : "string"
        },
        "descripcion" : {
            "type" : "string"
        }
    }
}

schema_agregar_lote = {
    "type": "object",
    "required" : ["producto", "precio", "cantidad", "fecha_exp"],
    "properties": {
        "producto" : {
            "type" : "string"
        },
        "precio" : {
            "type" : "number",
            "format" : "double"
        },
        "cantidad" : {
            "type" : "integer"
        },
        "fecha_exp" : {
            "type" : "string"
        }
    }
}