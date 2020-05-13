def make(n):
    def milt(x):
        return n * x
    return milt

m3 = make(3)
m5 = make(5)

print(m3(6))
print(m3(m5(6)))
