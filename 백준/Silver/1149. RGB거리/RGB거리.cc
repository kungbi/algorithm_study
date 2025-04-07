#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getNextIndex(int num, int plus){
	int sum = num + plus;
	if(2 < sum)
		sum -= 3;
	if(sum < 0)
		sum += 3;
	
	return sum;
}

int main(){
	int N, r, g, b;
	
	cin >> N;
	int arr[N][3];
	vector< vector<int> > dp(N, vector<int>(3, 1000000));
	for(int n = 0; n < N; n++){
		cin >> arr[n][0] >> arr[n][1] >> arr[n][2];
	}
	
	dp[0][0] = arr[0][0];
	dp[0][1] = arr[0][1];
	dp[0][2] = arr[0][2];
	int left, right;
	for(int n = 0; n < N-1; n++){
		for(int i = 0; i < 3; i++){
			left = getNextIndex(i, -1);
			right = getNextIndex(i, +1);
			
			dp[n+1][left] = min(dp[n+1][left], arr[n+1][left] + dp[n][i]);
			dp[n+1][right] = min(dp[n+1][right], arr[n+1][right] + dp[n][i]); 
		}
	}
	
	cout << *min_element(dp[N-1].begin(), dp[N-1].begin() + 3);
	return 0;
}