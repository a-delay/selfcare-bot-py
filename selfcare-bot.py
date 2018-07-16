#!/usr/bin/env python
import pytumblr
import random
import pw

def post_message(post=True):
    client = pytumblr.TumblrRestClient(
        pw.C_KEY,
        pw.C_SEC,
        pw.OAT,
        pw.OAT_SEC
    )

    print(client.info())

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
             "\u1f3b6 *whistles a happy tune*",
             "a quick reminder!!!",
             "got a minute?",
             "welcome to the self-care zone"]
    title = random.choice(titles)
    
    emojis = ["\u1f3b6",
              "\u270c",
              "\u1f44c",
              "\u1f44d",
              "\u1f64c",
              "\u2764",
              "\u1f499",
              "\u1f49a",
              "\u1f49b",
              "\u1f49c",
              "\u1f5a4",
              "\u1f338",
              "\u1f3f5",
              "\u1f339",
              "\u1f33a",
              "\u1f33b",
              "\u1f33c",
              "\u1f337",
              "\u1f331",
              "\u2b50",
              "\u1f31f",
              "\u2728",
              "\u1f3b5",
              "\u1f4af"]
    emoji = random.choice(emojis)    
    emoji = random.choice([ emoji, emoji+emoji, emoji+emoji+emoji])

    body = ' '.join([please, prompt, transition, action+punctuation, emoji])

    message = {'tags': 'selfcare, self care, selfcare bot, '+tag, 'title': title, 'body':body}
    return message

post_message(False)
