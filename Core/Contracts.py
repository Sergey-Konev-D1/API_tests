USER_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

LIST_RESOURSE_DATA_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"},
    },
    "required": ["id", "name", "year", "color", "pantone_value"]
}

LIST_RESOURSE_DATA_SCHEMA_BLOCK_SUPPORT = {
    "type": "object",
    "properties": {
        "url": {"type": "string"},
        "text": {"type": "string"}
    },
    "required": ["url", "text"]
}

USER_DATA_SCHEMA_CREATE_PERSON = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

USER_DATA_SCHEMA_UPDATE_PERSON = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["name", "job", "updatedAt"]
}

REGISTRATION_DATA_SCHEMA = {
    "type": "object",
    "properties":{
        "id": {"type": "number"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

LOGIN_DATA_SCHEMA = {
    "type": "object",
    "properties":{
        "token": {"type": "string"}
    },
    "required": ["token"]
}