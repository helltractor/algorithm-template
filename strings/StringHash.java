package strings;

import java.util.Arrays;

class StringHash {
    
    private static final long BASE = 131313;
    private static final long MOD = 1_000_000_007L;
    
    private long[] h;
    private long[] p;
    private int n;
    
    public StringHash(String s) {
        this.n = s.length();
        this.h = new long[n + 1];
        this.p = new long[n + 1];
        p[0] = 1;
        for (int i = 1; i <= n; i++) {
            p[i] = (p[i - 1] * BASE) % MOD;
            h[i] = (h[i - 1] * BASE + s.charAt(i - 1)) % MOD;
        }
    }
    
    public StringHash(int[] s) {
        this.n = s.length;
        this.h = new long[n + 1];
        this.p = new long[n + 1];
        p[0] = 1;
        for (int i = 1; i <= n; i++) {
            p[i] = (p[i - 1] * BASE) % MOD;
            h[i] = (h[i - 1] * BASE + s[i - 1]) % MOD;
        }
    }
    
    public long getHash(int l, int r) {
        return (h[r + 1] - h[l] * p[r - l + 1] % MOD + MOD) % MOD;
    }
    
    public long getAddHash(int l1, int r1, int l2, int r2) {
        return (getHash(l1, r1) * p[r2 - l2 + 1] + getHash(l2, r2)) % MOD;
    }

}