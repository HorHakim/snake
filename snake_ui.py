from config import *
import pygame

class SnakeUi:
	def __init__(self):
		pygame.init()
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption('Snake')

		self.font_style = pygame.font.SysFont(None, 50)
		self.score_font = pygame.font.SysFont(None, 20)


	def write_score(self, score):
		value = self.score_font.render(f"Votre score : {score}", True, BLUE)
		self.window.blit(value, [0, 0])


	def draw_snake(self, snake_list):
		for snake_block in snake_list:
			pygame.draw.rect(self.window, BLACK, [*snake_block, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])


	def draw_food(self, food_position):
		pygame.draw.rect(self.window, GREEN, [*food_position, SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE])

	
	def update_screen(self, score, snake_list, food_position):
		self.window.fill(WHITE)
		self.write_score(score)
		self.draw_snake(snake_list)
		self.draw_food(food_position)