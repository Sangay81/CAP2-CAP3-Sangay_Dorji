import unittest
from unittest.mock import Mock
import pygame
pygame.init()

from main import SNAKE, Vector2

class TestSnakeGame(unittest.TestCase): #This test is all about checking if the snake can move in the game.  
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1, 1))

    def tearDown(self):
        pygame.quit()

    def test_move_snake(self):
        snake = SNAKE()
        snake.direction = Vector2(1, 0)
        snake.move_snake()
        self.assertEqual(snake.body[0], Vector2(6, 10))

    def test_add_block(self): #test_add_block: This test is about checking if a new block can be added to the game. 
                               
        snake = SNAKE()
        snake = SNAKE()
        snake.add_block()
        self.assertTrue(snake.new_block)

    def test_update_head_graphics(self):##test_update_head_graphics: This test is about checking if the graphics of the snake's head can be updated.
                                        
        snake = SNAKE()
        snake.update_head_graphics()
        self.assertEqual(snake.head, snake.head_left)
       

    def test_update_tail_graphics(self):#test_update_tail_graphics: This test is about checking if the graphics of the snake's tail can be updated.
                                  
        snake = SNAKE()
        snake.update_tail_graphics()
        self.assertEqual(snake.tail, snake.tail_left)

    def test_reset(self):#test_reset: This test is about checking if the game can be reset. 
                       
        snake = SNAKE()
        snake.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        snake.direction = Vector2(1, 0)
        snake.reset()
        self.assertEqual(snake.body, [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)])
        self.assertEqual(snake.direction, Vector2(0, 0))

    def test_play_crunch_sound(self):#test_play_crunch_sound: This test is about checking if the crunch sound can be played when the snake eats a block.


        snake = SNAKE()
        snake.crunch_sound = Mock()
        snake.play_crunch_sound()
        snake.crunch_sound.play.assert_called_once()

if __name__ == '__main__':
    unittest.main()


