# WikipediaGame

You can play with a live version of this at my blog at https://singlethreaded.me/wikipedia-game. It'll run your query on a server, so you don't need to download this repo at all.


This will try and find the shortest path between two wikipedia articles. 
The program can be run with: 

>> python parse.py

The program will then do this: 
Beginning Program....

Enter start point: 
Enter end point:

For these two, enter the start and end articles you would like to find a path between. In the wikipedia link for the article will
be formatted something like this: www.en.wikipedia.org/wiki/name_of_article (e.g www.en.wikipedia.org/wiki/North_Dakota). 
When entering the name of the article, you can use capitals or non-capital letters, use spaces instead of underscores (though 
underscores will still work). 

The program will run a heuristic-helped BFS starting from the start point. It will print out all the articles it is currently exploring. 
Then at the end, it will print a path from the start to the end. 

For example: 
Start Article: Palantir
End Article: Africa

Path: 
Palantir -> Magic (Middle-earth) -> J.R.R Tolkien -> Commander of the Order of the British Empire -> Orders, decorations, and medals of the United Kingdom -> United Kingdom -> Europe -> Africa


Enjoy!
