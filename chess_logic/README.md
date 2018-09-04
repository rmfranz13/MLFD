# Chess Logic
This directory aims to produce an algorithm capable of initializing an interactive virtual chess board which allows the play of legal moves and determines when the game is over and what the result is. This is essentially just a real-life chess board except the chess board itself knows the rules and enforces them. This goal is entirely unrelated to the goal of creating an intelligent chess player, though it is an essential step if legal games are to be played between two entities.

This setup will also allow the play of illegal moves (does not explicitly forbid them) though playing an illegal move will immediately result in a loss, which I hope will be an incentive to the neural networks to learn the rules just like any new chess player will make mistakes at first. I'm also doing this because this is the only way I can force every neural network to have the same number of inputs and outputs (64 in, 128 out... I think).

Anyways, presented below is an asm diagram for how I'm planning on building this interactive chess board. 

## ASM for Interactive chess board
![](https://github.com/rmfranz13/MLFD/blob/master/chess_logic/interactive_chess_board.png)
