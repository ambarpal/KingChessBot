#About
Here I will demonstrate the deficiencies in the a game-playing bot that won the first prize at grey-meter uni-commerce hackathon. They apparently did not lose even a single match in the contest.
The work is done in the ./break-bot subdirectory.

#Beating the Bot
##Method 1
The bot does not take into consideration the fact that after some moves the board graph may become disconnected and thus the player with the more choices at this time will win.
This possibility can be checked by a simple bfs of the board graph before making every move.
This is demonstrated in beaten-1-suffocate

##Method 2
The bot essentially makes a two-level bfs of the board graph, and decides greedily based on that. This can be beaten by doing a complete bfs over the board graph and ranking weighing every level a fraction that reduces with every level.
[Coming Soon]

#Note
The board that the referee passes in the current version is not according to the rank1bot's specifications, but nevertheless, it works accurately on beaten-1-suffocate.