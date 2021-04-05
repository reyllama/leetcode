"""
763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""

class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        from collections import defaultdict
        ref = defaultdict(list)

        for idx, letter in enumerate(S):
            ref[letter].append(idx)

        out = [0] * len(S)
        cur = 1

        for letter in ref:
            if len(ref[letter])>1:
                k = ref[letter][-1]-ref[letter][0]+1
                if out[ref[letter][0]] + out[ref[letter][-1]]==0:
                    out[ref[letter][0]:ref[letter][-1]+1]=[cur]*k
                    cur += 1
                elif out[ref[letter][0]]==0:
                    out[ref[letter][0]:ref[letter][-1]+1]=[out[ref[letter][-1]]]*k
                elif out[ref[letter][-1]]==0:
                    out[ref[letter][0]:ref[letter][-1]+1]=[out[ref[letter][0]]]*k
                elif out[ref[letter][0]] != out[ref[letter][-1]]:
                    out[out.index(out[ref[letter][0]]):len(S)-out.index(out[::-1][ref[letter][-1]])] = [out[ref[letter][0]]]*(len(S)-out.index(out[::-1][ref[letter][-1]])-out.index(out[ref[letter][0]]))


        cnt = 0
        ans = []
        done = set()

        for item in out:
            if item == 0:
                ans.append(1)
                continue
            elif item in done:
                continue
            else:
                ans.append(out.count(item))
                done.add(item)

        return ans

"""
Runtime: 40 ms, faster than 64.29% of Python3 online submissions for Partition Labels.
Memory Usage: 14.3 MB, less than 58.60% of Python3 online submissions for Partition Labels.
"""
