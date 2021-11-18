import random
import copy

class Hat:
    def __init__(self, **kwargs):
        # we take the key and the value. Ex: {'blue': 4, 'red':2} => we take the key 'blue' and
        # the value 4. Then we go from 0 to 4 to append the key 'blue' to contents for 4 times. 
        # Same with red
        self.contents = []
        for key, value in kwargs.items(): 
            for i in range(value):        
                self.contents.append(key)
        print(self.contents)

    def draw(self, number):
        all_removed = []

        # if we draw more numbers from the hat the numbers of balls we have, we just return the contents of the hat
        if(number > len(self.contents)):
            return self.contents

        # if the above doesn't happend we go from i to number and remove balls
        # I used random to remove a random ball from the hat
        # I then appended the removed ball to a list named all_removed
        # I used the pop function to also remove the specified ball because it will not return in the hat
        for i in range(number):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed

    
    def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        count = 0
        
        for i in range(num_experiments):
            # copy the expected_balls and hat so next time we enter this for loop, we won't have different values
            # of expected_balls and hat 
            expected_copy = copy.deepcopy(expected_balls)
            hat_copy = copy.deepcopy(hat)
            colors_gotten = hat_copy.draw(num_balls_drawn)

            for color in colors_gotten:
                # if the color is in colors_gotten, we change the value of colors_gotten until we reach 0
                # if 0 is reached, then it means the ball was a successfully drawn
                if color in expected_copy:
                    expected_copy[color] -= 1

        # we check if a ball was successfully drawn once more and we count them
        if(all(x <= 0 for x in expected_copy.values())):
            count += 1

        return count / num_experiments
