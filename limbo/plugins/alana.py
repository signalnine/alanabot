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

def on_message(msg, server):
    user = server.slack.server.users.find(msg["user"])
    username = user.name
    text = msg.get("text", "")
    match = re.findall(r"^(hi|hello|Hi)\b", text)
    if match:
       return hi(username)
    match = re.findall(r"(Terry Gross|terry gross)( .*)?", text)
    if match:
       return downvote(username)
    match = re.findall(r"(SUSHI|sushi)(.*)?", text)
    if match:
       return sushi()

    return
