#include <stdio.h>
#include <string.h>

int main()
{
  char  arr[5][15];

  // bzero(arr, 5 * 15);
  memset(arr, 0, 5 * 15);
  for (int i = 0; i < 5; i++)
    scanf("%s", arr[i]);
  
  for (int col = 0; col < 15; col++){
    for (int row = 0; row < 5; row++){
      if (arr[row][col] != '\0')
        printf("%c", arr[row][col]);
    }
  }
  return (0);
}