# 2 => 3
# 3 => 3+1 = 4, 3 - 1 = 2, 2=> 3, 3+4 =7
# 4 => 4+1 = 5, 4 - 1 = 3, 3=> 7, 5+7 = 12 => 14
# 5 => 5+1 = 6, 5 - 1 = 4, 4=> 13, 6+13 = 19 => 25
# 6 => 6+1 = 7, 6 - 1 = 5, 5=> 25, 7+25 = 32 => 57

# 3,7,14,25,57,120,247,502,1013,2035,4080,8169,16349,32712,65439,130994,262105,524327,1048572,2097141,4194293,8388598,16777207,33554426,67108865,134217745,268435508,536870935,1073741990,2147483999,4294968019,8589936062,17179872151,34359744731,68719489594,137438790021,274877580073,549755160178,1099513220387,2199026440609,4398052881054,8796105761943,17592111523823,35184223047676,70368446095383,140736892190793,281473784381616,562947568763263,1125895137526653,2251790275053276,4503580550106523,9007161100213029,18014322200426040,36028644400852057,72057288801704087,144114577603408150,288229155206816279,576458310413632539,1152916620827265062,2305833241654530111,4611666483309060211,9223332966618120420,18446665933236240839,36893331866472481769,73786663732944963532,147573327465889927159,295146654931779854309,590293309863559708610,1180586619727119417221,2361173239454238834443,4722346478908477668888,9444692957816955337777,18889385915633910675557,37778771831267821351110,75557543662535642702217,151115087325071285404433,302230174650142570808866,604460349300285141617733,1208920698600570283235467,2417841397201140566470934,4835682794402281132941879,9671365588804562265883769,19342731177609124531767542,38685462355218249063535191,77370924710436498127070391,154741


# def worst_case_button_presses(n):
#     return (2 ** n) - 1

# # Read input
# n = int(input())

# # Output the result
# print(worst_case_button_presses(n))

# def min_presses(n):
#     # Base case
#     if n == 1:
#         return 1
#     # Initialize the value for the first button press case
#     presses = 1
#     for i in range(2, n+1):
#         presses = 2 * presses + 1
#     return presses

# # Input
# n = int(input())
# print(min_presses(n))

# def calculate_worst_case_presses(n):
#     # Calculate total presses using the formula
#     total_presses = (n * (n + 1)) // 2
#     return total_presses

# # Input reading
# n = int(input().strip())
# result = calculate_worst_case_presses(n)
# print(result)

# def calculate_button_presses(n, sequence):
#     pressed_buttons = set()  # To track which buttons have been pressed
#     total_presses = 0
    
#     for button in sequence:
#         if button not in pressed_buttons:
#             total_presses += 1  # Count this button press
#             pressed_buttons.add(button)  # Mark this button as pressed
            
#         # Each time we press a new button, we also need to account for previous presses
#         total_presses += len(pressed_buttons)  # Add the number of unique presses
    
#     return total_presses

# # Input reading
# n = int(input().strip())
# sequence = list(map(int, input().strip().split()))

# result = calculate_button_presses(n, sequence)
# print(result)



# def calculate_button_presses(n):
#     total_presses = 0
#     for i in range(1, n + 1):
#         total_presses += i * (n - i + 1)
#     return total_presses

# # Input reading
# n = int(input().strip())
# result = calculate_button_presses(n)
# print(result)

