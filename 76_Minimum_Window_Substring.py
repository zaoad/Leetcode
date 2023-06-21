class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = {}
        for v in t:
            if not dict_t.get(v):
                dict_t[v] = -1
            else:
                dict_t[v] -= 1
        len_t = len(t)
        count = 0
        ans = ''
        i = 0
        j = 0
        len_s = len(s)
        print(len_s)
        min_len = len_s + 5
        flag = False
        while j <= len_s and i < len_s:
            if count == len_t:
                size = j - i + 1
                if size < min_len:
                    min_len = size
                    ans = s[i:j]
                c = s[i]

                if dict_t.get(c) is not None:
                    dict_t[c] -= 1
                    if dict_t[c] < 0:
                        count -= 1
                flag = True
                i += 1
                continue
            if flag:
                c = s[i]
                if dict_t.get(c) is not None:
                    flag = False
                    continue
                i += 1

            else:
                if j >= len_s:
                    flag = True
                    i = i + 1
                    continue
                c = s[j]
                if dict_t.get(c) is not None:
                    dict_t[c] += 1
                    if dict_t[c] <= 0:
                        count += 1
                j += 1
        return ans
