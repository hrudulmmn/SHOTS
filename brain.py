import yaml
import random
import memory

with open("personality.yaml","r") as per:
    personality = yaml.safe_load(per)

def greet_user(user):
    if user.lower()=="hello" or user.lower()=="hi":
        return random.choice(personality['greet'])

def ask_question(user):
    if user.lower()=="how" or user.lower()=="what" or user.lower()=="why":
        return random.choice(personality['ask'])
    else:
        return greet_user(user)
