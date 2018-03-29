#!/usr/bin/python3
import argparse
from wordlist import getWordList

def encode(message, key):
    ciphertext = str()
    for char in message.lower():
        if char != ' ':
            nc = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            nc = ' '
        ciphertext += nc
    return ciphertext

def decode(cyphertext, key):
    text = str()
    for char in cyphertext:
        if char != ' ':
            nc = chr((ord(char) - ord('a') - key + 26) % 26 + ord('a'))
        else:
            nc = ' '
        text += nc
    return text

def crack(cyphertext, wordList = getWordList()):
    decoded = list()
    solutions = list()
    for i in range(0, 26):
        text = decode(cyphertext, i)
        decoded.append((i, text))
        for word in wordList:
            if word in text:
                solutions.append((i, text))
                break
    if (len(solutions) != 0):
        return solutions
    else:
        return decoded

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Simple Ceasar Cypher")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encode', nargs=2, metavar=('message', 'key'))
    group.add_argument('-d', '--decode', nargs=2, metavar=('cyphertext', 'key'))
    group.add_argument('-c', '--crack', nargs=1, metavar='cyphertext')
    parser.add_argument('--min-word-size', type=int, default=4, metavar='num')
    parser.add_argument('--word-list', type=str, default='words.txt')
    args = parser.parse_args()
    if (args.encode is not None):
        print(encode(args.encode[0], int(args.encode[1])))
    elif (args.decode is not None):
        print(decode(args.decode[0], int(args.decode[1])))
    elif (args.crack is not None):
        print(crack(args.crack[0], getWordList(wordLen=args.min_word_size)))
