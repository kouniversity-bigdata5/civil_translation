# Requirements and Installation

* [PyTorch](http://pytorch.org/) version >= 1.0.0
* Python version >= 3.5

# How to run
### Data Preprocessing
Prepare the ko, th dataset by executing prepare_dataset.ipynb

### Prepare data for BERT and fine-tune BERT
Run the BERT_ko_th.ipynb

### Generate
Replace file paths as appropriate.
Using the `generate.py` to test model is the same as the Fairseq, but you should add `--bert-model-name` to indicate your BERT model name.

### Interactive
Using the `interactive.py` to test model.

Some of the code has been inspired/re-used from [this](https://github.com/bert-nmt/bert-nmt) implementation of BERT for NMT
