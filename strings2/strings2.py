# slice string into sentences of maximum length K, return number of sentences, if not possible return -1

import sys

entry_string = sys.argv[1]
max_sentence_length = int(sys.argv[2])

entry_string=list(entry_string)
sentences = []


def slicing(string, length):
    sentence_count = 0
    if len(string) < length:
        return "-1"
    while sentence_count < len(string)/length:
        sentences.append(string[sentence_count*max_sentence_length:(sentence_count*max_sentence_length)+max_sentence_length])
        sentence_count = sentence_count+1


slicing(entry_string, max_sentence_length)
print(entry_string)
print(max_sentence_length)
print(len(sentences))