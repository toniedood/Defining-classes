class ForumPost():
    def __init__(self, author, text, upvotes):
        self.author = author 
        self.text = text
        self.upvotes = upvotes 

    def view(self):
        return f'{self.text}, by {self.author} with {self.upvotes} votes'

