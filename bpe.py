from collections import defaultdict
from collections import Counter


dataset = [
    "this is a sentence",
    "another sentence here",
    "this is repeated"
]

def train_tokenizer(dataset, vocab_size):
    word_count = word_freq(dataset)
    vocab = init_vocab(word_count)
    word_splits = word_split(word_count) 
    merge_rules = defaultdict(str)
    

    while len(vocab) <= vocab_size:       
        pair_frequency = pair_freq(word_splits, word_count) 
        prominent_pair, appeared = dominant_pair(pair_frequency)  
        word_splits = merge_pair(prominent_pair, word_splits)
        merge_rules[prominent_pair] = "".join(prominent_pair)  
        vocab.append(''.join(prominent_pair)) 
    
    return merge_rules, vocab


def tokenizer(merge_rules, dataset):
    tokenized_data = list()
    for paragraph in dataset:
        tokenized_data.append( tokenize(merge_rules, paragraph) ) 

def tokenize(rules, paragraph):
    splits = list(paragraph.replace(' ','$')) 
    for pair, token in rules.items():
        idx = 0
        while idx < len(splits)-1 :
            if splits[idx] == pair[0] and splits[idx+1] == pair[1]:
                splits = splits[:idx] + token + splits[idx+2:]
    return splits


def word_freq(dataset):
    return Counter(word for line in dataset for word in line.replace(' ', ' $').split()) 

def word_split(unique_words):
    return defaultdict(list, {word: list(word) for word in unique_words}) 

def init_vocab(unique_words):
   return list(dict.fromkeys(i for word in unique_words for i in word)) + ['$'] 
                                                                           
def pair_freq(splits, word_count):
    pair_dict = defaultdict(int) 
    for word, count in word_count.items():
        split = splits[word] 
        if len(word) == 1:
            continue
        for a, b in zip(split, split[1:]):
            pair_dict[(a, b)] += count
    return pair_dict

def dominant_pair(pairs):
    return max(pairs.items(), key=lambda x: x[1]) 


def merge(rules, pair): 
    rules[pair] = "".join(pair)
    return rules 

def merge_pair(pair, word_splits):
    merged_splits = defaultdict(list) 
    for word, split in word_split.items():
        for idx in range(len(split)-1):
            if split[idx] == pair[0] and split[idx+1] == pair[1]:
                split = split[:idx] + "".join(pair) + split[idx+2:]
        merged_splits[word] = split
    return merged_splits




            
             


