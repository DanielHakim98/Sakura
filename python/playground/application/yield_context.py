class MyContext:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit', exc_type)

def stream():
    with MyContext():
        yield 1
        yield 2

for x in stream():
    assert x == 1
    break
print("after")

word = "python"
res = ""
for i in range(len(word)-1, -1, -1):
    res += word[i]
print(res)
