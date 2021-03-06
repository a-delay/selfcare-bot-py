#!/usr/bin/env python
import pytumblr
import random
import os

def post_message(post=True):
    client = pytumblr.TumblrRestClient(
        os.environ['HKU_C_KEY'],
        os.environ['HKU_C_SEC'],
        os.environ['HKU_OAT'],
        os.environ['HKU_OAT_SEC']
    )

    message = generate_message();

    if post:
        client.create_text("selfcare-bot", state='published', tags=message['tags'], title=message['title'], body=message['body'])

def generate_message():

    pleases = ["please",
               "please",
               "please",
               "",
               ""]
    
    please = random.choice(pleases)

    prompts = ["remember",
              "take some time",
              "remember to take some time",
              "remember to take time",
              "remember to take some time right now",
              "remember to take some time rn",
              "take a break",
              "take a quick break",
              "remember to take a quick break",
              "don't forget",
              "take a moment",
              "take a moment right now",
              "take a moment rn",
              "take a little time today",
              "take a little time",
              "take a little time right now",
              "take a little time rn",
              "find some time",
              "find some time today",
              "find some time right now",
              "find some time rn",
              "take a little bit of time",
              "dont forget",
              "",
              "",
              ""]
    
    prompt = random.choice(prompts)

    transitions = ["to","and"]
    transition = random.choice(transitions)
    if prompt == "":
        transition = ""
    
    actiontags = {1: "water", 2: "food", 3 : "stretch", 4: "breathe", 5: "take a break", 6: "help"}

    actions = {"drink some water" : 1,
               "drink a cup of water": 1,
               "hydrate yourself": 1,
               "take a sip of water": 1,
               "pour yourself a glass of water": 1,
               "have some water": 1,
               "have a glass of water": 1,
               "have some water ": 1,
               "eat a snack": 2,
               "find a snack": 2,
               "eat something healthy": 2,
               "have some food if you haven't yet": 2,
               "eat some fruit": 2,
               "have some chips": 2,
               "eat a little something": 2,
               "eat": 2,
               "have some food": 2,
               "eat something": 2,
               "stand and stretch": 3,
               "check your posture": 3,
               "look up from your screen": 5,
               "stretch your back": 3,
               "look outside for a while": 3,
               "look at a bird or something": 3,
               "take a deep breath": 4,
               "take a deep breath and relax": 4,
               "sit up and stretch your shoulders": 3,
               "take a break": 5,
               "get some fresh air": 4,
               "stretch": 3,
               "adjust your posture": 3,
               "breathe": 4,
               "stretch your legs": 3,
               "take your meds": 5,
               "rest your eyes": 5,
               "flex your fingers": 3,
               "ask for help if you need it": 6,
               "ask for help if you need it ": 6,
               "laugh at something funny": 5,
               "watch a cat video": 5,
               "look away from your screen for a while": 5,
               "relax and find something calm to think about": 4}
    action = random.choice(list(actions))
    tag = actiontags[actions[action]]

    punctuations = ["",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "!",
                   "!",
                   "!",
                   "!!",
                   "!!!",
                   "!!!",
                   "!!!",
                   "!!!",
                   " !!",
                   " !!",
                   " !!!",
                   " !!!"]

    punctuation = random.choice(punctuations)

    titles = ["hey!!!",
             "frembly remembly",
             "frembly rememlby",
             "be kind to urself",
             "reminder:",
             "<3", 
             "ilu",
             "hello?",
             "pls listen",
             "are you doing ok",
             "u ok?",
             "hey!!",
             "hey",
             "<3 !!!!",
             "take a moment",
             "got a moment?",
             "please take a break!!!!",
             "please take a break!",
             "*with love and support*",
             "*a soft bird lands on your shoulder*",
             "times are rough but please take care of urself",
             "\U0001f3b6 *whistles a happy tune*",
             "a quick reminder!!!",
             "got a minute?",
             "welcome to the self-care zone"]
    title = random.choice(titles)
    
    emojis = ["\U0001f3b6",
              "\U0000270c",
              "\U0001f44c",
              "\U0001f44d",
              "\U0001f64c",
              "\U00002764",
              "\U0001f499",
              "\U0001f49a",
              "\U0001f49b",
              "\U0001f49c",
              "\U0001f5a4",
              "\U0001f338",
              "\U0001f3f5",
              "\U0001f339",
              "\U0001f33a",
              "\U0001f33b",
              "\U0001f33c",
              "\U0001f337",
              "\U0001f331",
              "\U00002b50",
              "\U0001f31f",
              "\U00002728",
              "\U0001f3b5",
              "\U0001f4af"]
    emoji = random.choice(emojis)    
    emoji = random.choice([ emoji, emoji+emoji, emoji+emoji+emoji])

    body = ' '.join([please, prompt, transition, action+punctuation, emoji])
    tags = ['selfcare', 'self care', 'selfcare bot', tag]

    message = {'tags': tags, 'title': title, 'body':body}
    return message

post_message()
