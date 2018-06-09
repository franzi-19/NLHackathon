#!/usr/bin/python
import json
import quickstart
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
import Features, EntitiesOptions, KeywordsOptions
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, CategoriesOptions
import re

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='253b4aa9-26ee-4caf-b919-f5533dd61ad6',
  password='vfQVBiOl0fV8',
  url = 'https://gateway-fra.watsonplatform.net/natural-language-understanding/api',
  version='2018-03-16')

def analyseVideo(text):
    response = natural_language_understanding.analyze(
        text = text,
        features=Features(
            categories=CategoriesOptions(),
            entities=EntitiesOptions(
            emotion=True,
            sentiment=True,
            limit=3),
            keywords=KeywordsOptions(
            emotion=True,
            sentiment=True,
            limit=3)))

    #json.dumps(response, indent=2)
    print("Classification: ")
    for cat in response["categories"]:
        print(str(cat["label"]) + "(" + str(round(cat["score"]*100)) + "%)")
    print("\n")
