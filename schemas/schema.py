schema_create_person = {
    "type": "object",
    "required": ["dni", "name", "last-name", "username", "password"],
    "properties": {
        "dni": {
            "type": "string",
            "minLength": 10,
            "maxLength": 10
        },
        "name": {
            "type": "string"
        },
        "last-name": {
            "type": "string"
        },
        "username": {
            "type": "string",
            "format": "email"
        },
        "password": {
            "type": "string"
        }
    }
}


schema_login = {
    "type": "object",
    "required" : ["username", "password"],
    "properties": {
        "username" : {
            "type" : "string"
        },
        "password" : {
            "type" : "string"
        }
    }
}


schema_create_product = {
    "type": "object",
    "required" : ["name", "description"],
    "properties": {
        "name" : {
            "type" : "string"
        },
        "description" : {
            "type" : "string"
        }
    }
}

schema_update_product = {
    "type": "object",
    "required" : ["uid", "name", "description"],
    "properties": {
        "uid": {
            "type" : "string"
        },
        "name" : {
            "type" : "string"
        },
        "description" : {
            "type" : "string"
        }
    }
}

schema_create_batch = {
    "type": "object",
    "required" : ["product", "price", "stock", "exp_date"],
    "properties": {
        "product" : {
            "type" : "string"
        },
        "price" : {
            "type" : "number",
            "format" : "double"
        },
        "stock" : {
            "type" : "integer"
        },
        "exp_date" : {
            "type" : "string"
        }
    }
}

schema_update_batch = {
    "type": "object",
    "required" : ["batch", "product", "price", "stock", "exp_date"],
    "properties": {
        "batch": {
          "type" : "string"  
        },
        "product" : {
            "type" : "string"
        },
        "price" : {
            "type" : "number",
            "format" : "double"
        },
        "stock" : {
            "type" : "integer"
        },
        "exp_date" : {
            "type" : "string"
        }
    }
}
