class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        ans = []
        pos = -1
        larger = -1

        for i in xrange(n):
            x = ord(target[i]) - 97

            j = x + 1
            while j < 26 and cnt[j] == 0:
                j += 1

            if j < 26:
                pos = i
                larger = j

            if cnt[x] == 0:
                break

            cnt[x] -= 1
            ans.append(target[i])
        else:
            i = n

        if pos == -1:
            return ""

        for k in xrange(pos, len(ans)):
            cnt[ord(ans[k]) - 97] += 1

        ans = ans[:pos]
        ans.append(chr(larger + 97))
        cnt[larger] -= 1

        for k in xrange(26):
            while cnt[k]:
                ans.append(chr(k + 97))
                cnt[k] -= 1

        return ''.join(ans)