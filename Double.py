'''this might do something'''

try:
    x = float(input())
    print(x*2)
except ValueError:
    print("number please")
