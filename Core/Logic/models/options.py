from pathlib import Path
import json

TAG_CHOICES = (
    ("TRI", "Triage"),
    ("BUG", "Bug"),
    ("DUP", "Duplicate"),
    ("INP", "In progress"),
    ("DEP", "Dependencies"),
)

PATH = Path(__file__).resolve().parent

with open(PATH/"fixtures/choices.json","w") as fileObj:
    json.dump((TAG_CHOICES), fileObj)


PRIORITY_CHOICES = (
    ("HIG", "High"),
    ("MOD", "Moderate"),
    ("SEV", "Severe"),
    ("LOW", "Low"),
    ("ML", "Moderately Low"),
    ("EMER", "Emergency"),
)

with open(PATH/"fixtures/priority.json", "w") as fileObj:
    json.dump(PRIORITY_CHOICES, fileObj)

REACTIONS = (
    ("👍", "👍"),
    ("🚀", "🚀"),
    ("☀️", "☀️"),
    ("📣", "📣"),
    ("👀", "👀"),
    ("👍", "👍"),
    ("👎", "👎"),
    ("🥳", "🥳"),
)

with open(PATH/"fixtures/rxn.json", "w") as fileObj:
    json.dump((REACTIONS), fileObj)

DEPARTMENTS = [
    (
    "ADM", "Administrator")
    ,
    ("MGM", "Management")
]

with open(PATH/"fixtures/dept.json", "w") as fileObj:
    json.dump((DEPARTMENTS), fileObj)


#Functions for read-objects

def read_file(file):
    with open(file) as fileObj:
        data = json.load(fileObj)
        return data

def write_file(file,data):
    with open(file, 'w') as fileObj:
        json.dump(data, fileObj)