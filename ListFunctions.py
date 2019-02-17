lucky_numbers = [47,56,6,70,81,9]
friends = ["ninad","bulbul","bulbul","faisal","fokrul","rahman"]
friends.extend(lucky_numbers)
friends.append("tommy")
friends.insert(1,"esha") #1 is the position 
friends.remove("tommy")
friends.pop() #delete last element

print(friends)
print(friends.count("bulbul"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 =friends.copy()
print(friends2)
