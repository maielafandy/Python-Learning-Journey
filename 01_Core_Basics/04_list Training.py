task = []

task.append("study")
task.append("Gym")
task.append("Read")

for index, name in enumerate(task):
    print(f"{index+1}-{name}")

print(f"the length of the list is {len(task)}")
task_num = int(input("Enter task to delet"))
index = task_num-1
task.pop(index)

task_name = str(input("Enter task to search"))
num = task.count(task_name)
if num >= 1:
    print("task found")
else:
    print("task not found")


for index, name in enumerate(task):
    print(f"{index+1}-{name}")
print(f"the length of the list is {len(task)}")
