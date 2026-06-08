class ForumPost():
    def __init__(self, author, text, upvotes,):
        self.author = author 
        self.text = text
        self.upvotes = upvotes 
        self.replies = []


    def view(self):
        return f'{self.text}, by {self.author} with {self.upvotes} votes. Comments: {self.replies}'

    def add_replies(self, reply):
        self.replies.append(reply) 