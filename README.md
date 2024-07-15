# IPFS Huggingface Transformers

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


# IPFS Huggingface Bridge

for transformers.js visit:                          
https://github.com/endomorphosis/ipfs_transformers_js

for huggingface datasets python library visit:
https://github.com/endomorphosis/ipfs_datasets

for faiss KNN index python library visit:
https://github.com/endomorphosis/ipfs_faiss

for orbitdb_kit nodejs library visit:
https://github.com/endomorphosis/orbitdb_kit/

for fireproof_kit nodejs library visit:
https://github.com/endomorphosis/fireproof-kit

for python model manager library visit: 
https://github.com/endomorphosis/ipfs_model_manager/

for nodejs model manager library visit: 
https://github.com/endomorphosis/ipfs_model_manager_js/

for nodejs ipfs huggingface scraper with pinning services visit:
https://github.com/endomorphosis/ipfs_huggingface_scraper/

for ipfs huggingface agents visit:
https://github.com/endomorphosis/ipfs_agents

for ipfs huggingface accelerate visit:
https://github.com/endomorphosis/ipfs_accelerate

for ipfs_kit visit:
https://github.com/endomorphosis/ipfs_kit

for ipfs_kit_js visit:
https://github.com/endomorphosis/ipfs_kit_js

Author - Benjamin Barber
QA - Kevin De Haan
