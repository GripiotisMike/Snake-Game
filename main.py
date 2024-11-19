from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates for smoother gameplay

# Create game components
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Listen for key presses to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # Update the screen after every movement
    time.sleep(0.2)  # Slow down the game loop to control the snake speed
    snake.move()

    # Check if the snake collides with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new location
        snake.extend()  # Add a segment to the snake's body
        scoreboard.score_increase()  # Increase the score

    # Check if the snake hits the wall or itself
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()  # Reset the scoreboard if snake hits the wall
        snake.snake_reset()  # Reset the snake

    # Check if the snake collides with its own body
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()  # Reset the scoreboard if snake hits itself
            snake.snake_reset()  # Reset the snake

# Exit the game when the user clicks on the screen
screen.exitonclick()
