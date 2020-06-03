teams_file = open("teams.txt", "w")

teamone = 'Chelsea' + "\n"
teamtwo = 'Arsenal' + '\n'
teamthree = 'Tottenham' + '\n'
teamfour = 'Liverpool' + '\n'
teamfive = 'Leicester' + '\n'

teams_file.write(teamone)
teams_file.write(teamtwo)
teams_file.write(teamthree)
teams_file.write(teamfour)
teams_file.write(teamfive)

teams_file.close()

read_teams = open("teams.txt", "r")
print(read_teams.readline())
read_teams.readline()
read_teams.readline()
print(read_teams.readline())
read_teams.readline()
read_teams.close()