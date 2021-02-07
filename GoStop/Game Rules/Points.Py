points = []


# Basic point totals
if num_junk_cards >= 10:
    junk_points = num_junk_cards - 9
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

    if "SadMan" & num_brights == 3:
        bright_points = 2
    
    if num_brights == 5:
        bright_points = 15

else:
    bright_points= 0



# More advanced point calculations

points = points * 2^num_go

if Birds == 3:
    points += 5

if ribbons contain 3 of the same type:
    ribbon_points = 5
