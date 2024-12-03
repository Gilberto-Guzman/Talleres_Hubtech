class Post:
    def __init__(self, post_id, title, body, user_id):
        self.post_id = post_id
        self.title = title
        self.body = body
        self.user_id = user_id

    @classmethod
    def from_dict(cls,data):
        return cls(
            post_id=data.get("id"),
            title=data.get("title"),
            body=data.get("body"),
            user_id=data.get("userId")
        )

    def __str__(self):
        return f"Post(ID: {self.post_id}, Title: {self.title}, Body: {self.body}, UserID: {self.user_id})"

data = [

]

post = Post.from_dict(data)
print(post)

# post = Post(
#     post_id=1,
#     title="Loop",
#     body="Lorem Ipsum",
#     user_id=30
# )

# print(post)