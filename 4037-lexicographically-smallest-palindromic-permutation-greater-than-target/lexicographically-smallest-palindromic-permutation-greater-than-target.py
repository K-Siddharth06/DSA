class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)
        half = n // 2
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        odd = 0
        mid = -1

        for i in xrange(26):
            if cnt[i] % 2:
                odd += 1
                mid = i

        if odd != n % 2:
            return ""

        for i in xrange(26):
            cnt[i] //= 2

        t = target[:half]

        def build(h):
            if n % 2:
                return h + chr(mid + 97) + h[::-1]
            return h + h[::-1]

        c = cnt[:]
        possible = True

        for ch in t:
            x = ord(ch) - 97
            if c[x] == 0:
                possible = False
                break
            c[x] -= 1

        if possible:
            if n % 2:
                x = ord(target[half]) - 97

                if mid > x:
                    return build(t)

                if mid == x:
                    candidate = build(t)
                    if candidate > target:
                        return candidate
            else:
                candidate = build(t)
                if candidate > target:
                    return candidate

        c = cnt[:]
        prefix = []
        best_pos = -1
        best_char = -1
        i = 0

        while i < half:
            x = ord(t[i]) - 97

            j = x + 1
            while j < 26 and c[j] == 0:
                j += 1

            if j < 26:
                best_pos = i
                best_char = j
                best_prefix = prefix[:]

            if c[x] == 0:
                break

            c[x] -= 1
            prefix.append(x)
            i += 1

        if best_pos == -1:
            return ""

        c = cnt[:]

        for x in best_prefix:
            c[x] -= 1

        c[best_char] -= 1

        h = ""

        for x in best_prefix:
            h += chr(x + 97)

        h += chr(best_char + 97)

        for x in xrange(26):
            while c[x]:
                h += chr(x + 97)
                c[x] -= 1

        return build(h)