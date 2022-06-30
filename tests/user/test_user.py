from src.baseclasses.response import Response
from src.schema.user import User


def test_getiing_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200)
    Response(get_users).validate(User)
    print(make_number)


