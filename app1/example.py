new_member = input("Type the name of the new member: ") + "\n"
file = open("members.txt", "r", encoding="utf-8")
existing_members = file.readlines()
file.close()

existing_members.append(new_member + "\n")

file = open("members.txt", "w", encoding="utf-8")
file.writelines(existing_members)
file.close()
