from core.entity import User
from core.entity import Post


def main() -> int:
    user = User(
        name="John Doe",
        email="johndoe@gmail.com",
        password="hello123456",
        is_admin=True,
        is_active=True,
    )

    post = Post(
        title="Hello World",
        content="This is the first post",
        url="hello-world",
        user_id=user.id,
    )

    user.post = [post]

    print(user)
    return 0


if __name__ == "__main__":
    main()
