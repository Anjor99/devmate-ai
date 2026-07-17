from app.models.message import Message, Role

msg = Message(
    role=Role.USER,
    content="Hello DevMate!"
)

print(msg)