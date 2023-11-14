#include <stdio.h>

int main()
{
  int map[100][100] = {0};
  int n, input_x, input_y;
  int i, j, x, y;
  int count;

  scanf("%d", &n);
  for (i = 0; i < n; i++)
  {
    scanf("%d %d", &input_x, &input_y);
    for (j = 0; j < 100; j++)
      map[input_y + j / 10][input_x + j % 10]++;
  }

  count = 0;
  for (y = 0; y < 100; y++)
  {
    for (x = 0; x < 100; x++)
    {
      if (map[y][x] != 0)
        count++;
    }
  }
  printf("%d", count);
  return (0);
}