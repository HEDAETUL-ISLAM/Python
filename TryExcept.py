try:
    result = 10/0

except ZeroDivisionError as ex:
    print(ex)
except:
    print("invalid input.")