class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for ind, value in enumerate(s):
            if value == '(':
                stack.append(ind)
            else:
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(ind)
        print stack
        stack.insert(0,-1)
        stack.append(None)
        ans = max([len(s[stack[i]+1: stack[i+1]]) for i in xrange(len(stack)-1)])
        print ans
        return ans


s = Solution()
print s.longestValidParentheses('()(()')
