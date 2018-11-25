class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_arr = s.split()
        print(s_arr)
        print(s_arr.reverse())
        s_arr_reversed = s_arr.reverse()
        return " ".join(s_arr_reversed)

sol = Solution()
print(sol.reverseWords("hello  world I'm    here lol ! yes"))
