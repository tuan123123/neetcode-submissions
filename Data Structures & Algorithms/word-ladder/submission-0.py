class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        
        words = set(wordList)

        if endWord not in words:
            return 0
        
        q = deque([beginWord])

        words.discard(beginWord)
        moves = 2
        while q:
            for _  in range(len(q)):
                current = q.popleft()
                for i in range(len(current)):
                    for letter in "abcdefghijklmnopqrstuvwxyz":
                        if letter == current[i]:
                            continue
                        
                        next_word = (current[:i] + letter + current[i + 1:])

                        if next_word not in words:
                            continue
                        
                        if next_word == endWord:
                            return moves

                        words.remove(next_word)
                        q.append(next_word)
            moves += 1
        
        return 0

