class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                nums.append(int(token))
            else:
                tmp_res = 0
                if token == "+":
                    tmp = nums.pop()
                    tmp_res = nums.pop() + tmp
                elif token == "-":
                    tmp_res = 0
                    tmp = nums.pop()
                    tmp_res = nums.pop() - tmp
                elif token == '*':
                    tmp = nums.pop()
                    tmp_res = nums.pop() * tmp
                else:
                    tmp = nums.pop()
                    tmp_res = int(nums.pop() / tmp)
                nums.append(tmp_res)
        return nums[-1]