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
    responses = ['ssanborn--', 'YAY', 'adorbs', 'omg', ':sumo:', ':heart:', ':smile:', 'gnats!', ':woop:', ':toot:', ':shoe:']
    return random.choice(responses)

def random_vote(username):
    vote = ['++', "--", "++", "++"]
    return username + random.choice(vote)

def will():
    return "Will wasn't even born yet."

def maths():
    return "NO MATHS ALLOWED"

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
    match = re.findall(r"(sushi|sashimi|tuna|maguro)(.*)?", text)
    if match:
       return sushi()
    match = re.findall(r"(\d+)(.*)?(\+|\-|\*|\\)(.*)?(\d+)", text)
    if match:
       return maths()
    match = re.findall(r"\b(80s|90s|back when|long time|ago|the days|19\d{2}|20\d{2}\b)", text)
    if match:
       return will()
    match = re.findall(r"\b(activate|engage|dothething|initiate)(.*)?", text)
    if match:
       return beep()
    match = re.findall(r"\b(apple|watermelon|peach|pear|banana|strawberr(i|y)|cucumber|berr(i|y)|leftover|pie|pizza|carrot|bean|corn|pea|nectarine|grape|donut|trash|recycle|recycling|chip|cake|cookie)e*s*\b", text)
    if match:
       return compost()
    if (random.random() < 0.05):
       return random_response()
    if (random.random() < 0.01):
       return random_vote(username)
    return
