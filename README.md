# Simple Similarity Matching
This module support calculating matching score between two strings with two method
* TfIdf to convert two string base on vocabulary which built from these strings, and then get cosine matching score
* Use word2vec to get vector from sentences, and then get cosine matching score


## Download data here:
- https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
- https://thiaisotajppub.s3-ap-northeast-1.amazonaws.com/publicfiles/wiki.vi.model.bin.gz

## Put data to target directory
* put data on directory: ./data/models/similarity/

## Install requirement packages
```bash
python3 -m pip install -r requirements.txt
```