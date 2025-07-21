from src.views.http_types.http_request import HttpRequest
from .person_creator_validator import person_creator_validator

def test_person_creator_validator():
    request = HttpRequest({
        "first_name": "fulano",
        "last_name": "detal",
        "age": 3,
        "pet_id": 7
    })

    person_creator_validator(request)
