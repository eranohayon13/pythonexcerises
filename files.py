file = open("teams.txt", "w")

team1 = "Manchetser United"
team2 = "New York Knicks"
team3 = "Boston Red Sox"
team4 = "Oakland Raiders"
team5 = "Beitar Jerusalem"

team = team1 + "\n" + team2 + "\n" + team3 + "\n" + team4 + "\n" + team5

file.write(team)

file = open("teams.txt", "r")
outfile = ""
for line in range(5):
    if line == 0:
        file.readline()
        outfile += "This is a new line \n"
    outfile += file.readline()
#Opens the team file, and creates a new variuable for us to store old file contents.
# For loop to go through thte 5 lines and when at line 0, skip a line and add new message.
# loop starts from the top and goesto the next line and adds that line to the file, does this until all lines are done that are within the range.

file.close()

file = open("teamsedit", "w")
file.write(outfile)
#creates a new file and adds the code from the previous edit to ensure teh original list and updated line is included.