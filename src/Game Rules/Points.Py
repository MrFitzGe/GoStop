
scoreboard_crosstab = self.scoreboard['Group'].value_counts()

num_junks = scoreboard_crosstab.iloc['junk'] + self.scoreboard['Special'].value_counts().iloc['DoubleJunk']
num_animals = scoreboard_crosstab.iloc['animal']
num_ribbons = scoreboard_crosstab.iloc['ribbon']
num_brights = scoreboard_crosstab.iloc['junk']
# Basic point totals


if num_junks >= 10:
    junk_points = num_junks - 9
else:
    junk_points = 0
       
if num_animals >= 5:
    animal_points = num_animals - 4
else:
    animal_points= 0

if num_ribbons >= 5:
    ribbon_points = num_animals - 4
else:
    ribbon_points= 0

if num_brights >= 3:
    
    bright_points = num_brights

    if self.scoreboard.Special.isin(["SadMan"]) & num_brights == 3:
        bright_points = 2
    
    if num_brights == 5:
        bright_points = 15

else:
    bright_points= 0

points = bright_points + animal_points + ribbon_points + junk_points

# More advanced point calculations

if self.scoreboard['Special'].value_counts().iloc['Bird'] == 3:
    points += 5

if self.scoreboard['Special'].value_counts().iloc['Red_Writing'] == 3:
    points += 3
    
if self.scoreboard['Special'].value_counts().iloc['Blue_Writing'] == 3:
    points += 3
    
if self.scoreboard['Special'].value_counts().iloc['Red_Blank'] == 3:
    points += 3

points = points * 2^self.num_go