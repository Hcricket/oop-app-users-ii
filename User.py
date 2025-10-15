class User:
    all_posts = []  

    def __init__(self, username):
        self.username = username
        self.posts = []  

    def create_post(self, content):
        post = {"author": self.username, "content": content}
        self.posts.append(post)
        User.all_posts.append(post)