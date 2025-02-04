# write a python program using function to convert celsius to fahrenheit
#   c/5=(f-32)/9

def temperature(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in f: "))
c=temperature(f)
print(f"{round(c,2)}°C")