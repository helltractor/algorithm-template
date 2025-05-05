import os
import random
import sys
from io import IOBase, BytesIO


class FastIO(IOBase):
    newlines = 0
    
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b: break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


BUFSIZE = 1 << 12
sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
MOD1, MOD9 = 10 ** 9 + 7, 998244353
RD = random.randint(MOD1, MOD1 << 1)
D4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
D8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
Y, N, A, B = "Yes", "No", "Alice", "Bob"


def D():
    n, m = MII()
    ans = 0
    for i in range(64):
        if m >> i & 1:
            mod = 1 << i
            q, r = divmod(n + 1, mod * 2)
            ans += q * mod
            if r > mod:
                ans += r - mod
    print(ans % MOD1)


if __name__ == '__main__':
    D()
