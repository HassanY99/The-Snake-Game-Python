# The-Snake-Game-Python

## Recreation of Nokia's popular Snake game using Python Turtle module.
I made this app using python OOP and turtle module that uses tkinter. This game only has one level as it is the first working version but keeps track of users high score.

## CLASSES
### Main: Contains all the computation and runs the program.
### Food: Defines the attributes of a "food" and its random position.
### Snake: Defines the attributes used to create the snake. This class defines the list of segments that add up to build the snake and defines snake movement.
### Scoreboard: Defines attributes of a scoreboard and its functionality of updating the highest score in the scoreboard.txt file.

## LOGIC
### The snake is made using a list of segments. As the snake eats more food, segments get added and length increases.
### The Food is generated randomly.
### Collisions are detected when the head of the snake interacts with the Food, itself, or with the boundaries.

## INSTRUCTIONS
### Run the program in your IDE, a seperate window will open where the snake automatically starts moving. Take control by using your keyboard arrows.
### Avoid collision with walls and yourself and try to eat as much food as possible for a higher score.
