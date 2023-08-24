For this game I will be creating 4 componets to have a better understanding about the OOP(object oriented programming)
Key Highlights
1. Learning how to  import python file(.py) in another file and use its modules
2. Using super class
3. logic of movement for direction change
4. Interaction with food and wall for Game Over
4. maintaing a score board

Future features
1.Adding HIGH SCORE: having a highscore bar inside it, which will not update at start so that people can see the reference for the high score to beat
	Using the concept of file handling
2. Adding an score highligh feature whenever scored it will change color sort of a blinking 


Main logic of the code:

main.py =
 here allthe interactions of different classes will happen
food capture method 
score update 
screen method is used to update the screen whenever the turtle move and interacte with food or its tell
game over when snake.head move to a positon of current segment of its body
game over when it reaches the boundaries of the screen size we demarcated
scoreboard class is called upon to have a score feature during run time 
which due to screen.update will show correctly in real time
snake movement will be controlled by screen. tracer method to have a fluid motion of snake
 
food.py 
= here food will randomly appear on the screen with move method created in this class
also inheriting the turtle class
snake.py 
1. Here , creating a snake with default segment of 3 block
2. adding the segment as which will interact with food.py in main.py
3. adding the snake movement methods which will be called in main.py using screen .listen() and screen.onkey method

score.py
here scoreboard class is created using turtle as a superclass
score update 
here i will add a highscore feature
along with the score blinking when snake eats a food pallete