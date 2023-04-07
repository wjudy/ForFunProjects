import pygame
import sys

class Bucket:

	def __init__(self, pos, count, col):
		self.pebbles = [Pebble(col)] * count
		print(self.pebbles)
		self.pos = pos
		self.col = col

	def add_pebble(self):
		self.count += 1

	def remove_pebble(self):
		self.count -= 1

class EndBucket(Bucket):

	def __init__(self, pos, count, col):
		super().__init__(pos, count, col)
	
	def get_score(self):
		return count

class Pebble():

	def __init__(self, color):
		self.c = color
	
class Buckets():

	def __init__(self):
		self.red1 = Bucket(1, 4, 'r')
		self.red2 = Bucket(2, 4, 'r')
		self.red3 = Bucket(3, 4, 'r')
		self.red4 = Bucket(4, 4, 'r')
		self.red5 = Bucket(5, 4, 'r')
		self.red6 = Bucket(6, 4, 'r')
		self.red_end = EndBucket(7, 0, 'r')
		self.blue1 = Bucket(1, 4, 'b')
		self.blue2 = Bucket(2, 4, 'b')
		self.blue3 = Bucket(3, 4, 'b')
		self.blue4 = Bucket(4, 4, 'b')
		self.blue5 = Bucket(5, 4, 'b')
		self.blue6 = Bucket(6, 4, 'b')
		self.blue_end = EndBucket(7, 0, 'b')

	def sow(bucket):
		pebbles = bucket.count
		pos = bucket.pos
		color = bucket.col
		while pebbles > 0:
			print('hello')
			pebbles -= 1
			
			
class Game():

	def __init__(self):
		self.buckets = Buckets()

	def is_finished(self):
		for bucket in self.buckets:
			if bucket.pos == 7:
				continue
			if bucket.count > 0:
				return False

		return True

def main():

	pygame.init()
	res = (1500,400)
	screen = pygame.display.set_mode(res)
	screen.fill((20,100,60))
	color = (255,255,255)
	color_light_red = (250,170,170)
	color_dark_red = (100,30,30)
	color_light_blue = (170,170,250)
	color_dark_blue = (30,30,100)
	smallfont = pygame.font.SysFont('Corbel',35)

	# DRAWING END BUCKETS
	pygame.draw.rect(screen, color_dark_blue, (50, 50, 100, 300))
	pygame.draw.rect(screen, color_dark_red, (1350, 50, 100, 300))

	# DRAWING LIGHT BLUE BUCKETS
	pygame.draw.circle(screen, color_light_blue, (250, 100), 75)
	pygame.draw.circle(screen, color_light_blue, (450, 100), 75)
	pygame.draw.circle(screen, color_light_blue, (650, 100), 75)
	pygame.draw.circle(screen, color_light_blue, (850, 100), 75)
	pygame.draw.circle(screen, color_light_blue, (1050, 100), 75)
	pygame.draw.circle(screen, color_light_blue, (1250, 100), 75)

	# DRAWING LIGHT BLUE BUCKETS
	pygame.draw.circle(screen, color_light_red, (250, 300), 75)
	pygame.draw.circle(screen, color_light_red, (450, 300), 75)
	pygame.draw.circle(screen, color_light_red, (650, 300), 75)
	pygame.draw.circle(screen, color_light_red, (850, 300), 75)
	pygame.draw.circle(screen, color_light_red, (1050, 300), 75)
	pygame.draw.circle(screen, color_light_red, (1250, 300), 75)

	pygame.display.update()

	game = Game()

	while not game.is_finished():
		moves

		

if __name__ == "__main__":
	main()