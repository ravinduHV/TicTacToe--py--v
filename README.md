   # TicTacToe - The Dino Adventure 
    #### Video Demo:  <URL HERE>
    #### Description:
    
   > TicTacToe is a childhood game we all played. Here is a python implementation of the game. Without using OOp and AI, this is just created
     using functional programing with simple algorithem.

> User can simple run the program by calling *python TicTacToe.py*
>> There are two backdrops you can use. one is 'X' and other one is 'O'. 

>> Program promt for move, after that user can given comma seperated co-ordinate value as cell address. And press ***Enter***.
>   <html>
>      <img src='images/image1.png'>
>   </html>

> program will auto exit when after final result given.

# Algorithem.


#### + Prompt user for backdrop. 
#### + Repeat
   
   + If first move and computer's turn
       - Make a random move
          - Display grid.
   + Else
        - Display grid.
   + Check whether computer wins
        - if wins
            + Display *Lose* 
            + program exit
   + User's Turn
        - Prompt for a move. 
   + for filled cells around new move.
        - if filled cells filled by user
            + for every major axis
                - if filled cell and new move in axis
                    + Get other cell 
                    + If it is not empty and already filled by user 
                        - User win the game.
                        - Exit program

   + for filled cells around new move.
        - if filled cells filled by user
            + for every major axis
                - if filled cell and new move in axis
                    + Get other cell 
                    + If it is empty and there are no winning moves for computer.
                        - Block axis.
                        - break
   + if not maked a move yet and there is no winning move.
        - for empty cells around new move
            + for every major axis
                - If new moved cell and empty cell both in same axis
                    + check if other cell filled by user
                        - Block axis
   + else if computer has winning move.
        - Make the winning move
    
   + if yet computer does not perform any move and it is computer's first move
        - Make a secret move
   + if computer not yet make any move 
        - Make a random move
   + if no more cells and no one wins 
        - Display *Draw*
        - Exit program


> ## Requirements
> ### + dinosay
>   + *pip install dinosay*


> ***LET'S PLAY! CHEERS!!***