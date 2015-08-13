import random
import re

def hi(username):
    response = "Hi " + username + "!"
    return response

def downvote(username):
    response = username + "--"
    return response

def sushi():
    response = "I hate sushi."
    return response

def compost():
    response = "Don't forget to compost!"
    return response

def beep():
    response = "`beep boop`"
    return response

def random_response():
    responses = ['ssanborn--', 'YAY', 'omg', ':heart:', ':smile:', 'gnats!', ':woop:', ':toot:']
    return random.choice(responses)

def random_vote(username):
    vote = ['--', '++', "++"]
    return username + random.choice(vote)

def on_message(msg, server):
    user = server.slack.server.users.find(msg["user"])
    username = user.name
    text = msg.get("text", "").lower()
    match = re.findall(r"^(hi|hello)\b", text)
    if match:
       return hi(username)
    match = re.findall(r"(terry gross)( .*)?", text)
    if match:
       return downvote(username)
    match = re.findall(r"(sushi)(.*)?", text)
    if match:
       return sushi()
    match = re.findall(r"\b(activate|engage|dothething|initiate)(.*)?", text)
    if match:
       return beep()
    match = re.findall(r"\b(apples|watermelon|pears|bananas|strawberries|cucumbers|berries|leftovers|pie|pizza|carrots|beans|corn|peas|nectarines|grapes|donuts|trash|recycle|recycling|chips|cake|cookies)\b", text)
    if match:
       return compost()
    if (random.random() < 0.01):
       return random_response()
    if (random.random() < 0.01):
       return random_vote(username)
    return
