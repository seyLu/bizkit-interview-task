from typing import Any

from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search() -> tuple[list[Any], int]:
    return search_users(request.args.to_dict()), 200


def search_users(args: dict[str, str]) -> list[Any]:
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            _id: string
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

    _id: str = args.get("id", "")
    name: str = args.get("name", "")
    age: int | None = try_int(args.get("age"))
    occupation: str = args.get("occupation", "")

    for user in USERS:
        user_id: str = user["id"]  # type: ignore[assignment]
        user_name: str = user["name"]  # type: ignore[assignment]
        user_age: int = user["age"]  # type: ignore[assignment]
        user_occupation: str = user["occupation"]  # type: ignore[assignment]

        if (
            (_id is not None and _id == user_id)
            or (name is not None and name.casefold() in user_name.casefold())
            or (age is not None and age in range(user_age - 1, user_age + 2))
            or (
                occupation is not None
                and occupation.casefold() in user_occupation.casefold()
            )
        ):
            matching_users.append(user)

    return matching_users


def try_int(num: str | None) -> int | None:
    _num: int | None = 0
    if num is not None:
        try:
            _num = int(num)
        except ValueError:
            _num = None
    return _num
