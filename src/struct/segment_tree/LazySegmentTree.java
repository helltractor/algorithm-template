
/**
 * @Link: https://github.com/NASU41/AtCoderLibraryForJava/master/LazyySegTree/LazyySegTree.java
 */
class LazySegmentTree<S, F> {

    final int MAX;

    final int N;
    final int Log;
    final java.util.function.BinaryOperator<S> Op;
    final S E;
    final java.util.function.BiFunction<F, S, S> Mapping;
    final java.util.function.BinaryOperator<F> Composition;
    final F Id;

    final S[] Data;
    final F[] Lazy;

    @SuppressWarnings("unchecked")
    public LazySegmentTree(int n, java.util.function.BinaryOperator<S> op, S e, java.util.function.BiFunction<F, S, S> mapping, java.util.function.BinaryOperator<F> composition, F id) {
        this.MAX = n;
        int k = 1;
        while (k < n) {
            k <<= 1;
        }
        this.N = k;
        this.Log = Integer.numberOfTrailingZeros(N);
        this.Op = op;
        this.E = e;
        this.Mapping = mapping;
        this.Composition = composition;
        this.Id = id;
        this.Data = (S[]) new Object[N << 1];
        this.Lazy = (F[]) new Object[N];
        java.util.Arrays.fill(Data, E);
        java.util.Arrays.fill(Lazy, Id);
    }

    public LazySegmentTree(S[] dat, java.util.function.BinaryOperator<S> op, S e, java.util.function.BiFunction<F, S, S> mapping, java.util.function.BinaryOperator<F> composition, F id) {
        this(dat.length, op, e, mapping, composition, id);
        build(dat);
    }

    private void build(S[] dat) {
        int l = dat.length;
        System.arraycopy(dat, 0, Data, N, l);
        for (int i = N - 1; i > 0; i--) {
            Data[i] = Op.apply(Data[i << 1 | 0], Data[i << 1 | 1]);
        }
    }

    private void push(int k) {
        if (Lazy[k] == Id) {
            return;
        }
        int lk = k << 1 | 0, rk = k << 1 | 1;
        Data[lk] = Mapping.apply(Lazy[k], Data[lk]);
        Data[rk] = Mapping.apply(Lazy[k], Data[rk]);
        if (lk < N) {
            Lazy[lk] = Composition.apply(Lazy[k], Lazy[lk]);
        }
        if (rk < N) {
            Lazy[rk] = Composition.apply(Lazy[k], Lazy[rk]);
        }
        Lazy[k] = Id;
    }

    private void pushTo(int k) {
        for (int i = Log; i > 0; i--) {
            push(k >> i);
        }
    }

    private void pushTo(int lk, int rk) {
        for (int i = Log; i > 0; i--) {
            if (((lk >> i) << i) != lk) {
                push(lk >> i);
            }
            if (((rk >> i) << i) != rk) {
                push(rk >> i);
            }
        }
    }

    private void updateFrom(int k) {
        k >>= 1;
        while (k > 0) {
            Data[k] = Op.apply(Data[k << 1 | 0], Data[k << 1 | 1]);
            k >>= 1;
        }
    }

    private void updateFrom(int lk, int rk) {
        for (int i = 1; i <= Log; i++) {
            if (((lk >> i) << i) != lk) {
                int lki = lk >> i;
                Data[lki] = Op.apply(Data[lki << 1 | 0], Data[lki << 1 | 1]);
            }
            if (((rk >> i) << i) != rk) {
                int rki = (rk - 1) >> i;
                Data[rki] = Op.apply(Data[rki << 1 | 0], Data[rki << 1 | 1]);
            }
        }
    }

    public void set(int p, S x) {
        exclusiveRangeCheck(p);
        p += N;
        pushTo(p);
        Data[p] = x;
        updateFrom(p);
    }

    public S get(int p) {
        exclusiveRangeCheck(p);
        p += N;
        pushTo(p);
        return Data[p];
    }

    public S prod(int l, int r) {
        if (l > r) {
            throw new IllegalArgumentException(
                    String.format("Invalid range: [%d, %d)", l, r)
            );
        }
        inclusiveRangeCheck(l);
        inclusiveRangeCheck(r);
        if (l == r) {
            return E;
        }
        l += N;
        r += N;
        pushTo(l, r);
        S sumLeft = E, sumRight = E;
        while (l < r) {
            if ((l & 1) == 1) {
                sumLeft = Op.apply(sumLeft, Data[l++]);
            }
            if ((r & 1) == 1) {
                sumRight = Op.apply(Data[--r], sumRight);
            }
            l >>= 1;
            r >>= 1;
        }
        return Op.apply(sumLeft, sumRight);
    }

    public S allProd() {
        return Data[1];
    }

    public void apply(int p, F f) {
        exclusiveRangeCheck(p);
        p += N;
        pushTo(p);
        Data[p] = Mapping.apply(f, Data[p]);
        updateFrom(p);
    }

    public void apply(int l, int r, F f) {
        if (l > r) {
            throw new IllegalArgumentException(
                    String.format("Invalid range: [%d, %d)", l, r)
            );
        }
        inclusiveRangeCheck(l);
        inclusiveRangeCheck(r);
        if (l == r) {
            return;
        }
        l += N;
        r += N;
        pushTo(l, r);
        for (int l2 = l, r2 = r; l2 < r2;) {
            if ((l2 & 1) == 1) {
                Data[l2] = Mapping.apply(f, Data[l2]);
                if (l2 < N) {
                    Lazy[l2] = Composition.apply(f, Lazy[l2]);
                }
                l2++;
            }
            if ((r2 & 1) == 1) {
                r2--;
                Data[r2] = Mapping.apply(f, Data[r2]);
                if (r2 < N) {
                    Lazy[r2] = Composition.apply(f, Lazy[r2]);
                }
            }
            l2 >>= 1;
            r2 >>= 1;
        }
        updateFrom(l, r);
    }

    public int maxRight(int l, java.util.function.Predicate<S> g) {
        inclusiveRangeCheck(l);
        if (!g.test(E)) {
            throw new IllegalArgumentException("Identity element must satisfy the condition.");
        }
        if (l == MAX) {
            return MAX;
        }
        l += N;
        pushTo(l);
        S sum = E;
        do {
            l >>= Integer.numberOfTrailingZeros(l);
            if (!g.test(Op.apply(sum, Data[l]))) {
                while (l < N) {
                    push(l);
                    l = l << 1;
                    if (g.test(Op.apply(sum, Data[l]))) {
                        sum = Op.apply(sum, Data[l]);
                        l++;
                    }
                }
                return l - N;
            }
            sum = Op.apply(sum, Data[l]);
            l++;
        } while ((l & -l) != l);
        return MAX;
    }

    public int minLeft(int r, java.util.function.Predicate<S> g) {
        inclusiveRangeCheck(r);
        if (!g.test(E)) {
            throw new IllegalArgumentException("Identity element must satisfy the condition.");
        }
        if (r == 0) {
            return 0;
        }
        r += N;
        pushTo(r - 1);
        S sum = E;
        do {
            r--;
            while (r > 1 && (r & 1) == 1) {
                r >>= 1;
            }
            if (!g.test(Op.apply(Data[r], sum))) {
                while (r < N) {
                    push(r);
                    r = r << 1 | 1;
                    if (g.test(Op.apply(Data[r], sum))) {
                        sum = Op.apply(Data[r], sum);
                        r--;
                    }
                }
                return r + 1 - N;
            }
            sum = Op.apply(Data[r], sum);
        } while ((r & -r) != r);
        return 0;
    }

    private void exclusiveRangeCheck(int p) {
        if (p < 0 || p >= MAX) {
            throw new IndexOutOfBoundsException(
                    String.format("Index %d is not in [%d, %d).", p, 0, MAX)
            );
        }
    }

    private void inclusiveRangeCheck(int p) {
        if (p < 0 || p > MAX) {
            throw new IndexOutOfBoundsException(
                    String.format("Index %d is not in [%d, %d].", p, 0, MAX)
            );
        }
    }
}
