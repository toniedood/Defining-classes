from forum_post import ForumPost

post1 = ForumPost()
post1.author = 'Steven'
post1.text = 'How to find use for every Microsoft product.'
post1.upvotes = 2

post2 = ForumPost()
post2.author = 'Gay'
post2.text = 'Lord of the prayers'
post2.upvotes = 300

print(f'{post1.text} / {post1.author}, {post1.upvotes} votes')
print(f'{post2.text} / {post2.author}, {post2.upvotes} votes')

