import time
from turtle import Screen
from  snake import Snake
from  food import Food
from scoreboard import  Scoreboard
scoreboard = Scoreboard()
snake = Snake()
screen = Screen()
food = Food()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake game')
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

#detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


#detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 299 or snake.head.ycor() < -280:

        scoreboard.reset()
        snake.reset()

    #detect collision with body
    for segment in snake.all_turtle[1:]:
        if snake.head.distance(segment) < 9:

            scoreboard.reset()
            snake.reset()

screen.exitonclick()
