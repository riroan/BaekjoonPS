#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define endl '\n'
const int oOvOo = 0;
using ll = long long;
using namespace std;
typedef complex<double> base;
#include <smmintrin.h>
#include <immintrin.h>
#pragma GCC target("avx2")
#pragma GCC target("fma")
__m256d mult(__m256d a, __m256d b)
{
    __m256d c = _mm256_movedup_pd(a);
    __m256d d = _mm256_shuffle_pd(a, a, 15);
    __m256d cb = _mm256_mul_pd(c, b);
    __m256d db = _mm256_mul_pd(d, b);
    __m256d e = _mm256_shuffle_pd(db, db, 5);
    __m256d r = _mm256_addsub_pd(cb, e);
    return r;
}
void fft(int n, __m128d a[], bool invert)
{
    for (int i = 1, j = 0; i < n; ++i)
    {
        int bit = n >> 1;
        for (; j >= bit; bit >>= 1)
            j -= bit;
        j += bit;
        if (i < j)
            swap(a[i], a[j]);
    }
    for (int len = 2; len <= n; len <<= 1)
    {
        double ang = 2 * 3.14159265358979 / len * (invert ? -1 : 1);
        __m256d wlen;
        wlen[0] = cos(ang), wlen[1] = sin(ang);
        for (int i = 0; i < n; i += len)
        {
            __m256d w;
            w[0] = 1;
            w[1] = 0;
            for (int j = 0; j < len / 2; ++j)
            {
                w = _mm256_permute2f128_pd(w, w, 0);
                wlen = _mm256_insertf128_pd(wlen, a[i + j + len / 2], 1);
                w = mult(w, wlen);
                __m128d vw = _mm256_extractf128_pd(w, 1);
                __m128d u = a[i + j];
                a[i + j] = _mm_add_pd(u, vw);
                a[i + j + len / 2] = _mm_sub_pd(u, vw);
            }
        }
    }
    if (invert)
    {
        __m128d inv;
        inv[0] = inv[1] = 1.0 / n;
        for (int i = 0; i < n; ++i)
            a[i] = _mm_mul_pd(a[i], inv);
    }
}
vector<int64_t> multiply(vector<int64_t> &v, vector<int64_t> &w)
{
    int n = 2;
    while (n < v.size() + w.size())
        n <<= 1;
    __m128d *fv = new __m128d[n];
    for (int i = 0; i < n; ++i)
        fv[i][0] = fv[i][1] = 0;
    for (int i = 0; i < v.size(); ++i)
        fv[i][0] = v[i];
    for (int i = 0; i < w.size(); ++i)
        fv[i][1] = w[i];
    fft(n, fv, 0); // (a+bi) is stored in FFT
    for (int i = 0; i < n; i += 2)
    {
        __m256d a;
        a = _mm256_insertf128_pd(a, fv[i], 0);
        a = _mm256_insertf128_pd(a, fv[i + 1], 1);
        a = mult(a, a);
        fv[i] = _mm256_extractf128_pd(a, 0);
        fv[i + 1] = _mm256_extractf128_pd(a, 1);
    }
    fft(n, fv, 1);
    vector<int64_t> ret(n);
    for (int i = 0; i < n; ++i)
        ret[i] = (int64_t)round(fv[i][1] / 2);
    delete[] fv;
    return ret;
}
int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    string a, b;
    cin >> a;
    cin >> b;
    int n = a.size();
    vector<int64_t> arr(n), brr(n);
    for (int i = 0; i < n; i++)
    {
        arr[i] = a[i]-'0';
        brr[i] = b[i]-'0';
    }
    reverse(brr.begin(), brr.end());
    for (int i = 0; i < n;i++)
        arr.push_back(arr[i]);
    // int k = 2;
    // while (k<arr.size()+brr.size())
    //     k <<= 1;
    // for (int i = 0; i < k - arr.size();i++)
    //     arr.push_back(0);
    // for (int i = 0; i < k - brr.size(); i++)
    //     brr.push_back(0);
    auto ret = multiply(arr, brr);
    int64_t ans = 0;
    for(auto i : ret){
        ans = max(ans, i);
    }
    cout << ans << endl;
    return oOvOo;
}