import random
import re

def hi(username):
    response = "Hi " + username + "!"
    return response

def downvote(username):
    response = username + "--"
    return response

def sushi():
    responses = ["I hate sushi.", "Ew"]
    return random.choice(responses)

def compost():
    responses = ["Don't forget to compost!", "No paper towels in the recycling!"]
    return random.choice(responses)

def beep():
    responses = ["`beep boop`", "`initiating launch sequence..`", "`error`", "`I'm sorry, I can't do that, Dave.`"]
    return random.choice(responses)

def random_response():
    responses = ['ssanborn--', 'YAY', 'adorbs', 'omg', ':sumo:', ':heart:', ':smile:', 'gnats!', ':woop:', ':toot:', ':shoe:', 'Alana misses you.']
    return random.choice(responses)

def random_vote(username):
    vote = ['++', "--", "++", "++"]
    return username + random.choice(vote)

def random_favorite(username):
    return "You're my favorite " + username

def will():
    return "Will wasn't even born yet."

def flipflop(text):
    match = re.findall(r"\+\+", text)
    if match:
       return "flip.flopper--"
    return "flip.flopper++"

def luff(match):
    return "I luff " + match + "s!"

def feelings():
    responses = ["I don't know.", ":facepalm:", ":joy:", ":roflcopter:", ":sunglasses:", ":stuck_out_tongue:", ":neutral_face:", ":open_mouth:" ]
    return random.choice(responses)

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
    match = re.findall(r"\b(80s|90s|back when|long time|ago|the days|19\d{2}|20\d{2}\b)", text)
    if match:
       return will()
    match = re.findall(r"\b(activate|engage|dothething|initiate)(.*)?", text)
    if match:
       return beep()
    match = re.findall(r"(flip\.flopper)(--|\+\+)", text)
    if match:
       return flipflop(text)
    match = re.findall(r"\b(brussels sprout|rainbow|color|luff)", text)
    if match:
       return luff(match[0])
    match = re.findall(r"\b(how|what|why)\b(.*)?(alanabot)", text)
    if match:
       return feelings()
    match = re.findall(r"\b(too many|apple|watermelon|peach|pear|banana|strawberr(i|y)|cucumber|berr(i|y)|leftover|pie|pizza|carrot|bean|corn|pea|nectarine|grape|donut|trash|recycle|recycling|chip|cake|cookie)e*s*\b", text)
    if match:
       return compost()
    if (random.random() < 0.05):
       return random_response()
    if (random.random() < 0.01):
       return random_vote(username)
    if (random.random() < 0.01):
       return random_favorite(username)
    return
