from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_num = 0
        i = 0
        window = dict()
        for j, fruit in enumerate(fruits):
            window[fruit] = window.get(fruit, 0) + 1

            while len(window) > 2:
                window[fruits[i]] -= 1
                if window[fruits[i]] == 0:
                    del window[fruits[i]]
                i += 1

            max_num = max(max_num, j - i + 1)
        return max_num
