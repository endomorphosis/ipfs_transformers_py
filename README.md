# Data Economy Hackathon
IPFS Huggingface Bridge

Author - Benjamin Barber @endomorphosis

QA / website - Kevin De Haan @coregod360

CLEANUP / Windows compatibility / Breakfix 03/31/2024 - 04/07/2024

# About

This is a model manager and wrapper for huggingface, looks up a index of models from an collection of models, and will download a model from either https/s3/ipfs, depending on which source is the fastest.

# How to use

setup.py

In your python script

from transformers import AutoModelForSeq2SeqLM

from ipfs_transformers import AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_auto_download("google/t5_11b_trueteacher_and_anli")

or 

from transformers import AutoModelForSeq2SeqLM

from ipfs_transformers import AutoModelForSeq2SeqLM

model = AutoModelForSeq2SeqLM.from_ipfs("QmWJr4M1VN5KpJjqCsJsJg7PDmFoqQYs1BKpYxcdMY1qkh")

To scrape huggingface

interactive prompt:

node scraper.js 

import a model:

node scraper.js hf "modelname" (as defined in your .json files)

import all models 

node scraper.js hf 