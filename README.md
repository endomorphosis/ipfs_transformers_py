# Data Economy Hackathon
IPFS Huggingface Bridge

for transformers.js visit:
https://github.com/endomorphosis/ipfs_transformers_js

for huggingface datasets python library visit
https://github.com/endomorphosis/ipfs_datasets

for orbitdbkit nodejs library visit
https://github.com/endomorphosis/orbitdb-benchmark/

Author - Benjamin Barber
QA - Kevin De Haan

# About

This is a model manager and wrapper for huggingface, looks up a index of models from an collection of models, and will download a model from either https/s3/ipfs, depending on which source is the fastest.

# How to use
~~~shell
pip install .
~~~

look run ``python3 example.py`` for examples of usage.

this is designed to be a drop in replacement, which requires only 2 lines to be changed

In your python script
~~~shell
from transformers import AutoModel
from ipfs_transformers import AutoModel
model = AutoModel.from_auto_download("bge-small-en-v1.5")  
~~~

or 

~~~shell
from transformers import AutoModel
from ipfs_transformers import AutoModel
model = AutoModel.from_ipfs("QmccfbkWLYs9K3yucc6b3eSt8s8fKcyRRt24e3CDaeRhM1")
~~~

or to use with with s3 caching 
~~~shell
from transformers import AutoModel
from ipfs_transformers import AutoModel
model = T5Model.from_auto_download(
    model_name="google-bert/t5_11b_trueteacher_and_anli",
    s3cfg={
        "bucket": "cloud",
        "endpoint": "https://storage.googleapis.com",
        "secret_key": "",
        "access_key": ""
    }
)
~~~

# To scrape huggingface

with interactive prompt:

~~~shell
node scraper.js [source] [model name]
~~~

~~~shell
node scraper.js 
~~~

import a model already defined:

~~~shell
node scraper.js hf "modelname" (as defined in your .json files)
~~~

import all models previously defined:

~~~shell
node scraper.js hf 
~~~

## TODO integrate orbitDB

## TODO finish translating model manager to node.js and replace existing ipfs-cluster wrapper

## TODO finish finish translating model manager to browser js and replace existing ipfs-cluster wrapper

## TODO integrate transformers.js (browser implementation)

## TODO integrate bacalhau dockerfile