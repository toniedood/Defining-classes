from forum_post import ForumPost

post1 = ForumPost( "Steven", "How to add text in CLasses", 4)
post2 = ForumPost( "Anderson", "Have you mannaged?", 3000)

print(f'{post1.text}, by {post1.author} with {post1.upvotes} votes')
print(f'{post2.text}, by {post2.author} with {post2.upvotes} votes')

