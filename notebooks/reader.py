import pathlib

import nltk

# set directories
DATA_DIR = pathlib.Path().cwd().parent.joinpath("data")
CORPUS_DIR = DATA_DIR.joinpath("02_corpus").joinpath("grimm")

# Prepare corpus reader
GERMAN_TOKENIZER = nltk.data.load("tokenizers/punkt/german.pickle")
fairytale_corpus_reader = nltk.corpus.PlaintextCorpusReader(
    root=str(CORPUS_DIR),
    fileids="[\w+-]*\.txt",
    sent_tokenizer=GERMAN_TOKENIZER,
    encoding="utf-8",
)
