import snake_ui
import snake_logic
from config import *
import pygame

class SnakeController:
	def __init__(self):
		self.snake_ui_object = snake_ui.SnakeUi()
		self.snake_logic_object = snake_logic.SnakeLogic()
		self.run_game()


	def get_player_input(self, event):
		if event.key == pygame.K_LEFT:
			self.snake_logic_object.set_snake_movement("left")
		elif event.key == pygame.K_RIGHT:
			self.snake_logic_object.set_snake_movement("right")
		elif event.key == pygame.K_UP:
			self.snake_logic_object.set_snake_movement("up")
		elif event.key == pygame.K_DOWN:
			self.snake_logic_object.set_snake_movement("down")



	def run_game(self):
		run = True
		clock = pygame.time.Clock()

		while run :
			clock.tick(SNAKE_SPEED)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				
				if event.type == pygame.KEYDOWN:
					self.get_player_input(event)


			self.snake_logic_object.move_snake()

			score = self.snake_logic_object.get_score()
			snake_list = self.snake_logic_object.snake_list
			food_position = self.snake_logic_object.food_position

			run = self.snake_logic_object.game_in_progress()
			
			self.snake_ui_object.update_screen(score, snake_list, food_position)
			pygame.display.update()

		pygame.quit()