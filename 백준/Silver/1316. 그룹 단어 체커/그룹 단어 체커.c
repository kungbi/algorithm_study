#include <stdio.h>
#include <string.h>

int main()
{
    int     n;
    int     arr_len;
    char    arr[100];
    char    visited[26];
    int     count = 0;
    char    tmp;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s", arr);
        arr_len = strlen(arr);
        memset(visited, 0, 26);
        for (int j = 0; j < arr_len; j++)
        {
            tmp = arr[j];
            if (visited[tmp - 'a'] == 0)
                visited[tmp - 'a'] = 1;
            else
            {
                if (arr[j-1] != arr[j])
                    break;
            }
            if (j == arr_len - 1)
                count++;
        }
    }
    printf("%d", count);
    return 0;
}
