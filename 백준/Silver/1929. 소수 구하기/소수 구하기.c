#include <stdio.h>

int is_prime(int num)
{
  int i;

  if (num == 1)
    return (0);
  i = 2;
  while (i*i <= num)
  {
    if (num % i == 0)
      return (0);
    i++;
  }
  return (1);
}

int main()
{
  int M, N;

  scanf("%d %d", &M, &N);
  for(int i = M; i <= N; i++)
  {
    if (is_prime(i) == 1)
      printf("%d\n", i);
  }
  return (0);
}