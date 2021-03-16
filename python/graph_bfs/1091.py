from collections import deque

class Solution:

    def create_next(self, curs: str):
        chars = []
        for i in range(len(curs)):
            chars.append(curs[i])
        res = []
        for i in range(4):
            temp = chars[i]
            chars[i] = str((ord(chars[i]) - ord('0') + 1) % 10)
            res.append(''.join(chars))
            chars[i] = temp
            chars[i] = str((ord(chars[i]) - ord('0') + 9) % 10)
            res.append(''.join(chars))
            chars[i] = temp
        print(res)



        

    def openLock(self, deadends: List[str], target: str) -> int:

        start_word = "0000"
        self._deadends = set(deadends)
        if target in self._deadends or start_word in self._deadends:
            return -1

        if target == start_word:
            return 0

        q = deque()
        visited = dict()

        q.append(start_word)
        visited[start_word] = 1

        while q:
            curs = q.popleft()

            nexts = self.create_next(curs)

            for nxt in nexts:
                if nxt not in self._deadends and nxt not in visited:
                    q.append(nxt)
                    visited[nxt] = visited.get(curs) + 1

                    if nxt == target:
                        return visited[nxt]

        return -1


            

