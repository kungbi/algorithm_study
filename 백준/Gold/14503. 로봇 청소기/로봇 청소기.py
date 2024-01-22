
# 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 현재 칸의 주변 
# $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
# 반시계 방향으로 
# $90^\circ$ 회전한다.
# 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 1번으로 돌아간다.

dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

def to_back(r, c, d):
  dx, dy = list(zip(dxs, dys))[(d - 2) % 4]
  return r + dy, c + dx

def to_front(r, c, d):
  dx, dy = list(zip(dxs, dys))[d]
  return r + dy, c + dx

def is_frame(x, y, n, m):
  return 0 <= x < m and 0 <= y < n

def is_dirty_space(arr, r, c):
  N = len(arr)
  M = len(arr[0])
  for dx, dy in zip(dxs, dys):
    nx = c + dx
    ny = r + dy
    if is_frame(nx, ny, N, M) and arr[ny][nx] == 0:
      return True
  return False

def solution():
  N, M = tuple(map(int, input().split()))
  r, c, d = tuple(map(int, input().split()))
  arr = [list(map(int, input().split())) for _ in range(N)]
  clean_count = 0

  while True:
    if arr[r][c] == 0:
      arr[r][c] = 2
      clean_count += 1
    
    if not is_dirty_space(arr, r, c):
      back_r, back_c = to_back(r, c, d)
      if not is_frame(back_c, back_r, N, M) or arr[back_r][back_c] == 1:
        return clean_count
      r = back_r
      c = back_c
    
    if is_dirty_space(arr, r, c):
      d = (d - 1) % 4
      front_r, front_c = to_front(r, c, d)
      if is_frame(front_c, front_r, N, M) and arr[front_r][front_c] == 0:
        r = front_r
        c = front_c

print(solution())