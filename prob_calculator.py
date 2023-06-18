import copy
import random


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for color, count in balls.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls):
    drawn_balls = []
    if num_balls >= len(self.contents):
      drawn_balls = self.contents
      self.contents = []
    else:
      indices = random.sample(range(len(self.contents)), num_balls)
      drawn_balls = [self.contents[i] for i in indices]
      self.contents = [
        ball for i, ball in enumerate(self.contents) if i not in indices
      ]
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0

  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    drawn_balls_dict = {}
    for ball in drawn_balls:
      drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1

    success_flag = True
    for color, count in expected_balls.items():
      if drawn_balls_dict.get(color, 0) < count:
        success_flag = False
        break

    if success_flag:
      success += 1

  return success / num_experiments
