#主要使用rfind跟strip函數
#一個去掉首尾空格 => strip()
#一個找最後出現的指定字元(空格) => rfind(" ")

s = "Hello World "
def lengthOfLastWord(s):
    s = s.strip()
    rfind = s.rfind(" ")
    ans = len(s) - (rfind+1)
    return ans
print(lengthOfLastWord(s))

#不使用rfind跟strip函數的解答
def lengthOfLastWord_nofunction(s):
    # 先去除末尾的空格
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1

    # 从末尾向前找到最后一个单词的结束位置
    start = end
    while start >= 0 and s[start] != ' ':
        start -= 1

    # 计算最后一个单词的长度
    return end - start