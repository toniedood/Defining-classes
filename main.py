from forum_post import ForumPost

post1 = ForumPost( "Steven", "How to add text in CLasses", 4)
post1.add_replies("Great work!")
post1.add_replies("Love, it!")

post2 = ForumPost( "Anderson", "Have you mannaged?", 3000)
#post2.add_replies("it was verry helpfull.")

print(post1.view()) 
print(post2.view())
