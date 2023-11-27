import torch
import torch.nn as nn
import torch.optim as optim


with open('story.txt','r') as f:
    text = f.read()

char2index = {}
index2char = {}

char2index['#'] = 0
index2char[0] = '#'

all_chars = set(text)
for i,c in enumerate(all_chars):
    char2index[c] = i+1
    index2char[i+1] = c

vocab_size = len(char2index)
hidden_dim = 60


context_len = 10

all_data = []
for c in text:
    index = char2index[c]
    all_data.append(index)

all_data = torch.tensor(all_data)


def get_data(n):
    idxs = torch.randint(0,all_data.shape[0]-context_len-1,(n,))
    xx = [all_data[idx:idx+context_len] for idx in idxs]
    yy = [all_data[idx+1:idx+context_len+1] for idx in idxs]
    return torch.stack(xx),torch.stack(yy)


# print(get_data())