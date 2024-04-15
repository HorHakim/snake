from config import *
import random

class SnakeLogic:
	def __init__(self):

		self.snake_list = [(WIDTH // 2, HEIGHT // 2)]
		self.movement = [0, SNAKE_BLOCK_SIZE]
		self.snake_length = 1

		self.food_position = (random.randint(0, WIDTH) // SNAKE_BLOCK_SIZE * SNAKE_BLOCK_SIZE,\
							  random.randint(0, HEIGHT) // SNAKE_BLOCK_SIZE * SNAKE_BLOCK_SIZE)



	def set_snake_movement(self, new_movement):

		if new_movement == "left":
			if self.movement == [0, SNAKE_BLOCK_SIZE] or self.movement ==[0, -SNAKE_BLOCK_SIZE]:
				self.movement = [-SNAKE_BLOCK_SIZE, 0]

		elif new_movement == "right":
			if self.movement == [0, SNAKE_BLOCK_SIZE] or self.movement == [0, -SNAKE_BLOCK_SIZE]:
				self.movement = [SNAKE_BLOCK_SIZE, 0]

		if new_movement == "up":
			if self.movement == [-SNAKE_BLOCK_SIZE, 0] or self.movement ==[SNAKE_BLOCK_SIZE, 0]:
				self.movement = [0, -SNAKE_BLOCK_SIZE]

		elif new_movement == "down":
			if self.movement == [-SNAKE_BLOCK_SIZE, 0] or self.movement ==[SNAKE_BLOCK_SIZE, 0]:
				self.movement = [0, SNAKE_BLOCK_SIZE]



	def move_snake(self):
		new_head_position = (self.snake_list[-1][0] + self.movement[0], self.snake_list[-1][1] + self.movement[1])
		self.snake_list.append(new_head_position)
		
		if new_head_position == self.food_position:
			self.food_position = (random.randint(0, WIDTH) // SNAKE_BLOCK_SIZE * SNAKE_BLOCK_SIZE,\
					 			  random.randint(0, HEIGHT) // SNAKE_BLOCK_SIZE * SNAKE_BLOCK_SIZE)
		
		else:
			del self.snake_list[0]



	def get_score(self):
		return len(self.snake_list)



	def game_in_progress(self):
		eat_itself = not len(set(self.snake_list)) == len(self.snake_list)
		out_of_bound = self.snake_list[-1][0] < 0 or self.snake_list[-1][0] > WIDTH or self.snake_list[-1][1] < 0 or self.snake_list[-1][1] > HEIGHT
		return not (eat_itself or out_of_bound)