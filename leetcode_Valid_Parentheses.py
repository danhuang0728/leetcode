#建立一個空的推疊用陣列
#如果為左邊類型的括號就會push進空堆疊裡
#如果為右邊類型的括號就會進去另一邊配對
#配對成功正確的就會從堆疊裡pop出來 不正確就直接return False
#如果所有括號都是正確格式 最後堆疊裡會因為都配對完成所以呈現空的狀態 
#如果不是空的直接return False
#條建都達成return True

s = "([)]"
def isValid(s):
    stack = []
    for i in s:
        if i in '{[(':
            stack.append(i)
        else:
            if not stack or i == ")" and stack[-1] != "(" or\
                i == "]" and stack[-1] != "[" or\
                i == "}" and stack[-1] != "{" :
                return False
            stack.pop()
    if not stack:
        return True
    else:
        return False
      
print(isValid(s))
