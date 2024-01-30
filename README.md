# Generating and Solving Mazes

## Generation Part

To generate a maze and make sure a solution exists. I choose a wall at random and compare the colour of each dimension of this wall for the x or y axis. If the colour is different then the wall takes the colour of one of the two colours and propagates that same colour.
I repeat this operation as many times as there are walls.

![maze gif](https://i.imgur.com/Ks3lnFe.gif)


## Solving Part

To resolve the maze as quickly as possible I used the A* algorithm. 
This algorithm consists of evaluating each neighbours of a position to determine the best direction to take

![Maze Solver Gif](https://i.imgur.com/4fcFyHN.gif)

![Big Maze](https://i.imgur.com/rhk85PK.gif)


