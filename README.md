# 🔤 Byte Pair Encoding (BPE) Tokenizer in Python

This repository contains a minimal and readable implementation of the **Byte Pair Encoding (BPE)** tokenization algorithm, widely used in natural language processing (NLP) tasks such as GPT, RoBERTa, and SentencePiece.

---

## 🚀 What is BPE Tokenization?

**Byte Pair Encoding** is a data compression and tokenization technique that iteratively merges the most frequent pairs of bytes or characters in a dataset. It helps:
- Reduce vocabulary size
- Handle unknown or rare words
- Improve generalization in language models

---

## 📁 Dataset

The tokenizer operates on a sample `dataset`, defined as a list of text strings:

```python
dataset = [
    "this is a sentence",
    "another sentence here",
    "this is repeated"
]
