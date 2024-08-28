
task_list = []

while True:
    command = input("Input a task (add [task]/remove [task]/clear/exit/sort/remove/print [the task list]): ")
    if command == "exit":
        print("exiting the program")
        break
    if command == "clear":
        task_list.clear()
        print("task list cleared")
    if command == "print":
        index = 0
        print("---------------------------------------")
        index += 1
        print("TASK LIST:")
        for item in task_list:
            print(index, item)
        print("---------------------------------------")
    if command.startswith("add "):
        print(f"adding '{command[4:]}' to the task list")
        task_list.append(command[4:])
    if command.startswith("sort"):
        print("sorting the list by the alphabet")
        task_list.sort()
    if command.startswith("remove "):
        print(f'removing')
        task_list.remove(command[7:])
    else:
        print("error")