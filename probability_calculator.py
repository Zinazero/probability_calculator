import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for colour, count in kwargs.items():
            self.contents.extend([colour] * count)

    def draw(self, amount):
        balls_to_draw = min(amount, len(self.contents))
        drawn_balls = random.sample(self.contents, balls_to_draw)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        drawn_dict = {x: drawn_balls.count(x) for x in drawn_balls}
        success = True
        for key, value in expected_balls.items():
            if drawn_dict.get(key, 0) < value:
                success = False
                break
        if success:
            count += 1
    return (count / num_experiments)

hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, expected_balls={"blue":2, "green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)