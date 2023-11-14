#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int N, M;
    cin >> N;
    cin >> M;

    int arr[N];
    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }

    int result = 0;
    int temp;
    for(int i = 0; i < N-2; i++){
        for(int j = i+1; j < N-1; j++){
            for(int k = j+1; k < N; k++){
                temp = arr[i]+arr[j]+arr[k];
                if(temp <= M)
                    result = max(result, temp);
            }
        }
    }

    cout << result;
    return 0;
}