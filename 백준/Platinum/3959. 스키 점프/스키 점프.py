from math import sqrt, acos, pi, atan

g = 9.81

T = int(input())
for _ in range(T):
    j, p, H, L = map(int, input().split())
    v0 = sqrt(2 * g * j)
    try:
        x = sqrt(p / (g / (2 * v0 * v0) - 2 * H / L ** 2))
        hp = -4 * H * x / L ** 2
    except:
        x = -1
    if not (x >= 0 and x < L / 2):
        a = 2 * H / L ** 2 + g / (2 * v0 ** 2)
        b = -2 * H / L
        c = H - p
        try:
            x = (-b + sqrt(b ** 2 - a * c)) / a
            hp = 4 * H / L * (x / L - 1)
        except:
            x = -1
        if not (x >= 0.5 and x < L):
            x = sqrt(2 / g * (H + p)) * v0
            hp = 0
    f = -g / 2 * (x ** 2 / v0 ** 2) + H + p
    fp = -g * x / v0 ** 2
    velocity = sqrt(2 * g * (j + p + H - f))
    theta = abs(atan(fp) - atan(hp))
    print(x, velocity, theta * 180 / pi)
