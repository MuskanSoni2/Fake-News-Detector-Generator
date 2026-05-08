import random

subjects = [
"Government",
"NASA",
"Scientists",
"Police",
"Prime Minister",
"WHO"
]

verbs = [
"announces",
"reveals",
"discovers",
"launches",
"confirms"
]

objects = [
"secret alien mission",
"new virus outbreak",
"free electricity for all citizens",
"hidden gold mine discovery",
"AI robot army project"
]

def generate_fake_news():
    headline = random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(objects)
    return headline