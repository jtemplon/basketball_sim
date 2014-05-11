basketball_sim
==============

There is a models file that basically sets up everything, it also has a random player generator function, but that needs to be changed, because the players it generates aren't good enough to feed the game and get realistic results.

If you do want to feed it with realistic results you can run unc_clemson. It has 10 real players for both sides and does substitutions and plays relatively realistic college basketball games between the two teams.

To Dos: Make the random player generator work nicer, cleanup the game code (it is getting a little crazy), add game control layer (to select starting lineups potentially), think about other substitution patters besides fouls and "fatigue" (measured here by shots taken), add the ability to take a two-point shot right after pulling down an offensive rebound (it gives me a max recursion error when I tried it), add some additional gameplanning stuff (not sure what yet), add minutes played to players (would need to just update on flips, wouldn't be hard)
