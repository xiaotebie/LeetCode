class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_dict将存储我们遇到的每个字符以及它们最后出现的位置
        char_dict = {}
        # left表示滑动窗口的左边界，res存储最长无重复字符子串的长度
        left, res = 0, 0
        # 我们从左到右扫描字符串，用right表示当前扫描到的字符的位置
        for right in range(len(s)):
            # 如果当前字符已经在char_dict中（即我们之前遇到过这个字符）
            if s[right] in char_dict:
                # 我们需要更新左边界，将其移动到重复字符上一次出现位置的右边一位
                # 这样我们可以保证滑动窗口内没有重复字符
                # 注意：这里我们使用max函数来更新left，是因为我们不希望left向左移动
                left = max(char_dict[s[right]] + 1, left)

            # 更新当前字符的最后出现位置
            char_dict[s[right]] = right

            # 更新最长无重复字符子串的长度
            # 因为right和left都是下标，所以长度需要加1
            res = max(res, right - left + 1)

        return res


teststr = "meroitu456756uyuo09pgreferg76iujtyhtyjyujmuik7455390tgmerpgk"
a = Solution()
print(a.lengthOfLongestSubstring(teststr))
