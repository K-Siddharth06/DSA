class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0

            if seat in [2, 3, 4, 5]:
                rows[row] |= 1

            if seat in [4, 5, 6, 7]:
                rows[row] |= 2

            if seat in [6, 7, 8, 9]:
                rows[row] |= 4

        ans = (n - len(rows)) * 2

        for mask in rows.values():
            if mask == 0:
                ans += 2

            elif (mask & 1) == 0 and (mask & 4) == 0:
                ans += 2

            elif (mask & 1) == 0 or (mask & 2) == 0 or (mask & 4) == 0:
                ans += 1

        return ans