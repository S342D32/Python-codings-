from collections import deque
def wordLadder(beginWord, endWord, wordList):
  wordset = set(wordList)
  if endWord not in wordset:
    return 0
  queue = deque()
  queue.append((beginWord, 1))
  while queue:
    curr_word,level = queue.popleft()
    if curr_word == endWord:
      return level
    for i in range(len(curr_word)):
      for c in  "abcdefghijklmnopqrstuvwxyz":
         if c == curr_word[i]:
           continue 
         new_word = curr_word[:i]+c+curr_word[i+1:] 
         if new_word in wordset:
           queue.append((new_word,level+1))
           wordset.remove(new_word)
  return 0

wordList=["hot","dot","dog","lot","log","cog"]
beginWord="hot"
endWord="cog"
print(wordLadder(beginWord, endWord, wordList))
# TC = O(N*len(word)*26)
# SC =O(N)

         



   

  