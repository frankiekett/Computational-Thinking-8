# Begining: create variables 
summer_points = 0 
winter_points = 0

# Middle: ask questions 
answer = input("Would you rather A) play on the ocean , or B) play in the snow?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1


answer = input("Would you rather drink A) hot chocolate , or B) lemonade?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1 


answer = input("Would you rather wear A) pants , or B) shorts?")
if answer == "A":
    winter_points += 1
elif answer == "B":
    summer_points += 1  


answer = input("Would you rather vacation to A) Hawaii , or B) Canada?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1 


answer = input("Would you rather A) lay in the sun , or B) sit by a fire?")
if answer == "A":
    summer_points += 1
elif answer == "B":
    winter_points += 1 


# end of quiz 
if summer_points > winter_points : 
    print("you are a summer person")
elif winter_points > summer_points :
    print("you are a winter person")
 