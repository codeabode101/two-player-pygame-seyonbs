import sys
print("write your robot's name below")
robot_nameeee = input()
robot_name = robot_nameeee
print("please write down your robot's role below")
robot_roleee = input()
robot_role = robot_roleee
robot_battery_percentege = 100
print(F"greetings, my name is {robot_name},my role is to {robot_role} you,my battery percentage is {robot_battery_percentege}")
print("please write down task name below")
task_namee = input()
task_name = task_namee
print("please write down how much battery you are going to use below")
battery_costtt = int(input())
battery_cost = battery_costtt
robot_battery_percentege -= battery_cost
current_battery_level = robot_battery_percentege
print(task_name, battery_cost, current_battery_level, robot_name)