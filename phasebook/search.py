from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search() -> tuple[dict | str | list, int]:
    return search_users(request.args.to_dict()), 200


def search_users(args: dict) -> list:
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    if not args:
        return USERS

    matching_users = []

    id: str = args.get("id")
    name: str = args.get("name")
    age: int = try_int(args.get("age"))
    occupation: str = args.get("occupation")

    for user in USERS:
        user_id: str = user["id"]
        user_name: str = user["name"]
        user_age: int = user["age"]
        user_occupation: str = user["occupation"]

        print(id, user_id)
        print(name, user_name)
        print(age, user_age)
        print(occupation, user_occupation)

        if (id is not None and id == user_id) \
            or (name is not None and name.casefold() in user_name.casefold()) \
            or (age is not None and age in range(user_age - 1, user_age + 2)) \
            or (occupation is not None and occupation.casefold() in user_occupation.casefold()) \
        :
            matching_users.append(user)

    return matching_users


def try_int(num: str|None):
    if num is not None:
        try:
            num = int(num)
        except ValueError:
            num = None
        return num
