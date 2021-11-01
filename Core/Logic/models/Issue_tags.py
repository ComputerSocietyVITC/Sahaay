from os import read
from Logic.models.options import read_file
from pathlib import Path
DIR = str(Path(__file__).resolve().parent.parent) + r"/models/fixtures"

TAG_CHOICES = read_file(DIR + '/choices.json')
PRIORITY_CHOICES = read_file(DIR + '/priority.json')
REACTIONS = read_file(DIR + './rxn.json')
DEPARTMENTS = read_file(DIR + './dept.json')