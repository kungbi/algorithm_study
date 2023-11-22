class Solution {
    int dfs(int num, int subCnt){
        int cnt = 0;
        
        if(num == 3){
            if(subCnt == 2)
                return 1;
            return 0;
        }else if(num < 3 || Math.log(num) / Math.log(3) * 2 < subCnt){
            return 0;
        }

        if(num % 3 == 0 && 2 <= subCnt){
            cnt += dfs(num / 3, subCnt - 2);
        }
        cnt += dfs(num - 1, subCnt + 1);
        return cnt;
    }
    
    public int solution(int n) {
        int answer = 0;
        answer = dfs(n - 2, 2);
        return answer;
    }
}