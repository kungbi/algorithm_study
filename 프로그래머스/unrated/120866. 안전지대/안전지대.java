class Solution {
    public boolean is_frame(int x, int y, int n){
        return (0 <= x && x < n && 0 <= y && y < n);
    }
    
    public int solution(int[][] board) {
        int n = board.length;
        int answer = n * n;
        
        int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
        int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
        int x, y;
        
        
        for(int r = 0; r < n; r++){
            for(int c = 0; c < n; c++){
                if (board[r][c] == 1){
                    answer--;
                    for(int i = 0; i < 8; i++){
                        x = c + dx[i];
                        y = r + dy[i];
                        if (is_frame(x, y, n) && board[y][x] == 0){
                            board[y][x] = 2;
                            answer--;
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}