#This kind of problem require making adj list of possible edge 
#Then bfs result in minimum path between nodes
#Problem name Word Ladder / Similiar Problem Minimum genetic mutation

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        
        N = len(beginWord)
        
        for word in wordList:
            for i in range(N):
                patt = word[:i]+"*"+word[i+1:]
                adj[patt].append(word)
        q = deque()
        q.append([beginWord , 1])
        visited = set()
    
        while q:
            word , level = q.popleft()
            for i in range(N):
                cur_pat = word[:i] + "*" + word[i+1:]
                for v in adj[cur_pat]:
                    if v == endWord:
                        return level+1
                    if v not in visited:
                        visited.add(v)
                        q.append([v , level+1])
        return 0