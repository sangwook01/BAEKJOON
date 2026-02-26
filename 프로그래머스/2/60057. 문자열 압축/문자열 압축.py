'''
1.문자열을 확인하는 과정에서 같은 문자가 나오면 다음 문자 확인 
2.다른 문자열을 만나면 
2-a. 1개로 압축되는 경우
2-b. 기준을 i+1 해서 다음 것과 되는지 확인
2-b-1. 된다면 그 다음 문자열도 기준과 동일하게 해서 확인 즉, ababcdcd ->ab를 기준으로 하고 확인 2번째까지 가능
2-b-1-a. 된다면 cd를 기준으로 다음 것 확인
이과정이 멈출 시 2-b로 이동
2-b가 끝날 시 2-a로 이동
'''
def solution(s):

    n = len(s)
    answer = n    
    for step in range(1,n//2+1):
        result = ""
        prev = s[0:step] # 처음
        count = 1
        # step 단위로 순회
        for i in range(step, n, step):
            curr = s[i:i+step]
            # 같으면 count+1
            if prev == curr:
                count += 1
            # 다르면
            else:
                if count > 1:
                    result += str(count)
                result += prev
                prev = curr
                count = 1
        # 마지막 처리
        if count > 1:
            result += str(count)
        result += prev
        
        answer = min(answer, len(result))
    
    return answer
        
                
    