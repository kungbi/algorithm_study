#include <stdio.h>
#define NUM 9

int main(){
	int num;
    int max;
    int pos[2];

    max = -1;
    for (int y = 1; y <= NUM; y++)
    {
        for (int x = 1; x <= NUM; x++)
        {
            scanf("%d", &num);
            if (max < num)
            {
                max = num;
                pos[0] = y;
                pos[1] = x;
            }
        }
    }
    printf("%d\n", max);
    printf("%d %d\n", pos[0], pos[1]);
	return 0;
}
