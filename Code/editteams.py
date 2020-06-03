lines = []
printlines = []
save_teams = open("teams.txt", "r")
lines = save_teams.readlines()
save_teams.close()

edit_teams = open("teams.txt", "w")
edit_teams.write("This is a new line" + '\n')
for ele in lines:
    edit_teams.write(ele)
edit_teams.close()

print_teams = open("teams.txt", "r")
printlines = print_teams.readlines()
print(printlines)
print_teams.close()