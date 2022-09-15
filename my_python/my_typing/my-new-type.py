from typing import NewType

UserId = NewType('UserId', int)
id_1 = UserId(1234)
print(type(id_1))

def get_user_name(user_id: UserId) -> str:
    return str(user_id)

# typechecks
user_a = get_user_name(UserId(42351))

# does not typecheck; an int is not a UserId
user_b = get_user_name(-1)
print(user_b)

output = UserId(23413) + UserId(54341)

print(1 is UserId(1))