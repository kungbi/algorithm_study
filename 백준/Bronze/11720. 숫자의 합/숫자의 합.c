#include <stdio.h>

int main() {
  int n;
  char arr[100];
  int result;

  scanf("%d", &n);
  scanf("%s", arr);

  result = 0;
  for (int i = 0; i < n; i++) {
    result += arr[i] - '0';
  }
  printf("%d", result);
  return 0;
}