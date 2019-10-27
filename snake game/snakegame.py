from york_graphics import *
from random import randint
import time
import sys

windowWidth = 400
windowHeight = 400
cellSize = 20
head = 0

# Design the interface when playing the game
def interface():
    setLineThickness('0.5')
    setLineColour('white')
    for m in range(0,400,20):
        moveTo(m,0)
        drawLine(0,400)
        updateCanvas()
    for z in range(0,400,20):
        moveTo(0,z)
        drawLine(400,0)
        updateCanvas()

# Print the dialogue box to ask whether to start
def dialogue_box():
    setLineColour("green")
    setTextProperties(face = "times roman", size = 18, style = "italic", align = "centre", anchor = "nw")
    moveTo(90,150)
    drawText("Start Snake Game?")
    moveTo(110,220)
    drawText("Yes")
    moveTo(180,220)
    drawText("Cancel")
    updateCanvas()


# Define different components of the game


# Define the snake
def drawSnake(snake):
    for cood in snake: # The array of snake is defined in main(). It is like any variable like 'i''j'
        # print(cood)
        # paint snake body in white
        setLineThickness("20")
        setLineColour("white")
        moveTo(cood['x'],cood['y'])
        drawLine(20,0)
    # paint snake head in yellow 
    setLineThickness("20")
    setLineColour("yellow")
    moveTo(snake[head]['x'],snake[head]['y'])
    drawLine(20,0)
    setCanvasColour('Black')
    setLineColour('white')
    setLineThickness('0.5')
    interface()
    updateCanvas()
    clearCanvas()

# Define different way of snake's move

# Define the move of snake when getting the keyPress
def turn(snake,event): # 'event' is the keyPress
    # turn up and turn down
    # snake[head]['y'] is the coordinate of the pink cellSize and snake[1]['y'] is the coordinate of the fist cellSize of white part
    # Confirm that the snake moves up or down because after the snake changes the direction, if y is equal, the snake is moving vertically
    # "snake[1]['y']" is the y coordinate of the first square of snake body
    if snake[head]['y'] == snake[1]['y']:
        # up
        if event == 'Up':
            # Delete the last cellSize of the previous snake body (white part)
            # 'snake[-1]' is the last squre of snake body
            del snake[-1]
            newHead = {'x':snake[head]['x'],'y':snake[head]['y'] - cellSize}
            # Insert a new cellSize because getKeyPress will delete last cellSize of previous snake body.
            # 'getKeyPress' changes the position of first cellSize so the coordinate is redefined.
            snake.insert(0,newHead)

        # down
        elif event == 'Down':
            del snake[-1]
            newHead = {'x':snake[head]['x'],'y':snake[head]['y'] + cellSize}
            snake.insert(0,newHead)

    # turn right and turn left
    # Confirm that the snake moves right or left because after the snake changes the direction, if x is equal, the snake is moving horizontally
    if snake[head]['x'] == snake[1]['x']:
        # right
        if event == 'Right':
            # Delete the last cellSize of the previous snake body (white part)
            del snake[-1]
            newHead = {'x':snake[head]['x'] + cellSize,'y':snake[head]['y']}
            # Insert a new cellSize because getKeyPress will delete last cellSize of previous snake body. getKeyPress changes the position of first cellSize so the coordinate is redefined previously
            snake.insert(0,newHead)

        # left
        elif event == 'Left':
            del snake[-1]
            newHead = {'x':snake[head]['x'] - cellSize,'y':snake[head]['y']}
            snake.insert(0,newHead)

    return snake

# Define the move of snake when there is no keyPress according to the previous direction
def move(snake):
    # Move left
    # Confirm that snake is moving towards left because when there is no keyPress, if the snake moves to left, the coordinate of head is bigger than the first cellSize of white part
    if snake[head]['x'] < snake[1]['x']:
        del snake[-1]
        newHead = {'x':snake[head]['x'] - cellSize,'y':snake[head]['y']}
        snake.insert(0,newHead)

    # Move right
    # Confirm that snake is moving towards right
    elif snake[head]['x'] > snake[1]['x']:
        del snake[-1]
        newHead = {'x':snake[head]['x'] + cellSize,'y':snake[head]['y']}
        snake.insert(0,newHead)

    # Move up
    # Confirm that snake is moving towards up
    elif snake[head]['y'] < snake[1]['y']:
        del snake[-1]
        newHead = {'x':snake[head]['x'],'y':snake[head]['y'] - cellSize}
        snake.insert(0,newHead)

    # Move down
    # Confirm that snake is moving towards down
    elif snake[head]['y'] > snake[1]['y']:
        del snake[-1]
        newHead = {'x':snake[head]['x'],'y':snake[head]['y'] + cellSize}
        snake.insert(0,newHead)

    return snake

# Define the 'eat' function to let the snake be longer when the coordinates are equal to the foods' coordinates
# If snake eats food, the length is increasing so there is no need to delete the last cellSize of white part
def eat(snake):
    # left
    if snake[head]['x'] < snake[1]['x']:
        newHead = {'x':snake[head]['x'] - cellSize,'y':snake[head]['y']}
        snake.insert(0,newHead)

    # right
    elif snake[head]['x'] > snake[1]['x']:
        newHead = {'x':snake[head]['x'] + cellSize,'y':snake[head]['y']}
        snake.insert(0,newHead)

    # up
    elif snake[head]['y'] < snake[1]['y']:
        newHead = {'x':snake[head]['x'],'y':snake[head]['y'] - cellSize}
        snake.insert(0,newHead)

    # down
    elif snake[head]['y'] > snake[1]['y']:
        newHead = {'x':snake[head]['x'],'y':snake[head]['y'] + cellSize}
        snake.insert(0,newHead)

    return snake

# Print out 'game over' when crash happens
def check_game_over(score):

    # Define the score that the user gets
    clearCanvas()
    setCanvasColour('Black')
    setLineColour('white')
    setTextProperties(face='times roman', size = 18, style='bold italic', align='centre',anchor='centre')
    moveTo(170,100)
    drawText('GAME OVER')
    moveTo(170,180)
    drawText("Score:" + str(score))
    setTextProperties(face='times roman', size = 10, style='bold italic', align='centre',anchor='centre')
    moveTo(160,250)
    drawText("Press                  to exit")
    setTextProperties(face='times roman', size = 20, style='bold italic', align='centre',anchor='centre')
    moveTo(160,250)
    drawText("ESC")
    setTextProperties(face='times roman', size = 10, style='bold italic', align='centre',anchor='centre')
    moveTo(160,300)
    drawText("Press anywhere to continue")
    updateCanvas()

    while(True):
        x,y = waitForMouseClick()
        if x > 100 and x < 250 and y > 200 and y < 300: # Exit the window
            closeWindow()
        else:
            clearCanvas()
            updateCanvas()
            main()

# Define main functin of snake_game

def main():
    # Open a new window
    # openWindow()
    dialogue_box()

    # Different situation when pressing different buttons
    x,y = waitForMouseClick()
    if x > 180 and x < 270 and y < 300  and y > 170: #Cancel
        closeWindow()
        
    elif x < 150 and x > 110 and y < 300 and y > 170: #Yes
        clearCanvas()
        interface()
        updateCanvas()
        score = 0
        
         # Set the initial point of snakes and draw it
        startX = cellSize * randint(5,windowWidth/cellSize - 1)
        # The reason why it is an '10'or '30' is that the intial point is at middle of left line of the cellSize
        startY = cellSize * randint(1,windowHeight/cellSize -1) - 10
        

        # Due to the stable startY and '+''-' symbol after startX the initial direction has been confirmed
        snake = [{'x':startX,'y':startY},
                 {'x':startX - 1 * cellSize,'y':startY},
                 {'x':startX - 2 * cellSize,'y':startY},
                 {'x':startX - 3 * cellSize,'y':startY}]

        # Set the initial point of food
        foodX = cellSize * randint(2,windowWidth/cellSize - 2) 
        foodY = cellSize * randint(2,windowHeight/cellSize - 2) - 10

        time.sleep(3)
        while True: # 'while True' means there is no end of the loop except seeing 'break' and 'sys.exit()
            time.sleep(0.1)
            i = getKeyPress()
            # print(i)
            if i == 'Escape':
                sys.exit()
                closeWindow()

            # When pressing the direction button, the snake will turn to specific direction
            if i in ['Left','Right','Up','Down']:
                turn(snake,i)

            # If there is no specific instruction, the snake will just move in terms of the initial direction
            else:
                move(snake)
                
            print(i)

             # When the coordinates of snakes are eauqal to the coordinates of food, the length of sanke will increase one cellSize and the score will be added one
            if snake[head]['x'] == foodX and snake[head]['y'] == foodY:
                foodX = cellSize * randint(2,windowWidth/cellSize - 1)
                foodY = cellSize * randint(2,windowHeight/cellSize - 1) - 10
                eat(snake)
                score = score + 1

            # Define the time when the game is over
            elif snake[head]['x'] < 0 or snake[head]['x'] >= windowWidth or snake[head]['y'] <= 0 or snake[head]['y'] >= windowHeight:
                check_game_over(score)
            for body in snake[1:]: # 'snake[1:]' means in the array of the snake,  
                if body == snake[head]:
                    check_game_over(score)

            print(foodX,foodY)

            # Define what will happen after 3 seconds after pressing 'Yes'
            # Defination of the food
            setLineColour("pink")
            setLineThickness("20")
            moveTo(foodX,foodY)
            drawLine(20,0)
            # At the same time, we draw the snake
            drawSnake(snake)

            
            print(snake)

        else:
            dialogue_box() # Other place

            
# Print the main function out
if __name__ == '__main__':
    openWindow()
    main()

# Bugs: when the snake is a little bit long, the food will appear in the snake
        # viewing previous scores 
        # everytime the player play the game, the snakegame should store the highest score for this time playing the game
