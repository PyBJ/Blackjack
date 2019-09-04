# Python Blackjack Game

## TODO:
- Possible Features:
1.      Refactor so that ControllerTick(): # Handle input events, ViewTick(): # Draw everything
        - https://www.pygame.org/wiki/tut_design
          
2.      Balance needs to be subtracted whenever the hand begins, then
        if the player loses, nothing happens. If they win, they get ante + winnings.
        In it's current state, a player could continue spamming new game to never
        lose money. 

3.      Move the player hand up so options can be center formatted for them?

4.      Possibly add player "short hints" to the menu/game? 
   
## Note:
test.txt contains specific packages used to test the project
dev.txt contains packages used during the development process
prod.txt contains packages for production environment?

To run application go to linux terminal.
cd into /Blackjack-Project folder

Enter this command in /Blackjack-Project directory

$source venv/bin/activate

Enter this command in the Blackjack-Project/src directory

$python __main__.py

## UML Diagram Images:
![Image of Call Diagram](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/UML_Call_Diagram.png)
![Image of Class Diagram](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/Blackjack_Classes.png)

## Project Execution Images:
#### Start Menu
![Image of Starting Menu](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/execution_images/Starting_menu.PNG)
#### Starting a New Game
![Image of Starting Game](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/execution_images/Start_game.PNG)
#### Hitting and Staying Under 21
![Image of Hitting and Drawing](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/execution_images/Hit_and_draw.PNG)
#### Hitting and Winning
![Image of Hitting and Winning](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/execution_images/Hit_and_win.PNG)
#### Hitting and Going Over 21
![Image of Hitting and Losing](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/execution_images/Hit_and_lose.PNG)
#### Getting Blackjack
![Image of Getting Blackjack](https://github.com/CS4398-SM-Group2/Blackjack-Project/blob/feature/doc/execution_images/Blackjack.PNG)
