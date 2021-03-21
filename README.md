# Simple Similarity Matching
This module supports calculating matching score between two strings with two methods
* TfIdf to convert two strings base on vocabulary which built from these strings, and then get cosine matching score
* Use word2vec to get vector from sentences, and then get cosine matching score


## Download data here:
- https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?usp=sharing
- https://thiaisotajppub.s3-ap-northeast-1.amazonaws.com/publicfiles/wiki.vi.model.bin.gz

## Put data to target directory
```bash
mv  ~/Downloads/GoogleNews-vectors-negative300.bin ./data/models/similarity/
mv  ~/Downloads/wiki.vi.model.bin ./data/models/similarity/
```

## Install requirement packages
```bash
python3 -m pip install -r requirements.txt
```
