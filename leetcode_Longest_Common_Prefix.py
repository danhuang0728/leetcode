#求全部前公共詞綴
#用sorted函數將字串字母依照A~Z依序排好
#判斷排完後的頭尾有沒有不一樣 (如果有前公共詞綴排完後前會第一個字母會一致)
#迴圈一個一個字母對
v = ["abe","abd","abg","abz"]
ans=""
v=sorted(v) 
print(v)
first=v[0]
last=v[-1]

for i in range(min(len(first),len(last))):
    if(first[i]!=last[i]):
        print(ans)
        break
    ans+=first[i]
print(ans)
