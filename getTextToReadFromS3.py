# coding=UTF-8
from random import randint
import boto3

text = """
#Harry fährt mit Taxi. Wort A.
WortB.

# Warum ist das so?

# wieso!

"""

a = text.split('#')
print "QWERT" + a[1]
print a
for i in a:
    print i


def getTextFromS3():
    s3 = boto3.resource('s3')

    obj = s3.Object("alexa-meine-affirmationen", "meine-affirmationen.txt")
    affirmationen_text = obj.get()['Body'].read().decode('utf-8')

    return affirmationen_text
