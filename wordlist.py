def getWordList(wordLen = 4, wordFile="words.txt"):
    wordList = list()
    with open(wordFile) as f:
        for line in f.readlines():
            if (len(line) > wordLen+1):
                wordList.append(line[:-1])
    return wordList 
