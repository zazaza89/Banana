r = praw.Reddit('just having fun learning with /u/IBotaBanana')
r.login('IBotABanana', 'Jackieaa1')
submission = r.get_submission(submission_id='1rehmx')
flat_comments = praw.helpers.flatten_tree(submission.comments)
already_done = set()
for comment in flat_comments:
  if comment.body == "I'm not worried" and comment.id not in already_done:
    comment.reply('How can you not be worried?')
    already_done.add(comment.id)
