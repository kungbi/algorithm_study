#include <stdio.h>

int main(){
    int N, M, flag;
    int sum = 0;
    int first = 0;
    scanf("%d %d", &M, &N);

    for(int i = M; i <= N; i++){
        flag = 0;
        if (i == 1)
            flag = 1;
        for(int j = 2; j < i; j++){
            if(i % j == 0){
                flag = 1;
                break;
            }
        }

        if(flag == 0){
            sum += i;
            if(first == 0)
                first = i;
        }
    }

    if(sum != 0){
        printf("%d\n", sum);
        printf("%d\n", first);
    }
    else
        printf("-1\n");
    return 0;
}