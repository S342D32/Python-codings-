
from collections import deque

def wordLadder(wordList, beginWord, endWord):

    wordSet = set(wordList)

    if endWord not in wordSet:
        return []

    result = []
    queue = deque()

    queue.append([beginWord])

    while queue:

        level_size = len(queue)
        chosen_word = set()

        for _ in range(level_size):

            sequence = queue.popleft()
            last_word = sequence[-1]

            if last_word == endWord:
                result.append(sequence)
                continue

            for i in range(len(last_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    if ch == last_word[i]:
                        continue

                    new_word = last_word[:i] + ch + last_word[i+1:]

                    if new_word in wordSet:
                        chosen_word.add(new_word)
                        queue.append(sequence + [new_word])

        # Remove words only after processing the entire level
        for word in chosen_word:
            wordSet.remove(word)

        # Once the shortest paths are found, stop
        if result:
            break

    return result


wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "hot"
endWord = "cog"

print(wordLadder(wordList, beginWord, endWord))

wordList=["hot","dot","dog","lot","log","cog"]
beginWord="hot"
endWord="cog"
print(wordLadder(wordList,beginWord, endWord ))

# Complexity
# Let:
# - N = number of words.
# - L = length of each word.
# - 26 = alphabet size.
# - P = number of shortest paths.
# Complexity	Value
# Neighbor generation	O(N × L × 26 × L)
# Path storage	O(P × N × L) upper bound