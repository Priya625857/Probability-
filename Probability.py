# Probability-
# To calculate probability problem

#Total number of balls
total_balls=5+3+2

#Probability of drawing a red ball
red_balls=5
prob_red= red_balls/total_balls

#Probability of drawing a blue or green ball
blue_balls=3
green_balls=2
prob_blue_or_green = (blue_balls + green_balls)/ total_balls

#Probability of drawing two red balls consecutively wihout replacement
prob_two_reds=(red_balls/total_balls) + ((red_balls-1)/ (total_balls-1))

#Output results
print("Probability of drawing a red ball:",prob_red)
print("Probability of getting drawing a blue or green ball:",prob_blue_or_green)
print("Probability of drawing two red balls consecutively without replacement:",prob_two_reds)
