# CYOA Game Engine
This will make it easy to create your own choose
your own adventure game.

## Instructions

- Type anything without a line break to have it printed typewriter-style.

- Type 'chunk [anything unique]' to make a new chunk of text. 
	- Example: 'chunk bathroom scene' would help me know when your scene starts and stops so I can properly add everything together.

- TIP: You must start a chunk before using any keywords below

- Type 'pause' to make user press ENTER to continue.

- Type 'choose' and then comma-separated items to list a menu to choose from.
	- Example: "choose A, B, C"
	- Returns string i.e. 'A'

- Type 'blank' to insert a blank line

- Type 'wait [seconds]' to pause for a designated amount of seconds. Default is 1 second.

	- Make comments by starting with #
	- Example: '# this is a comment.'

## Example use case
- Create a script, separating all important sections with `chunk` keywords.
- Edit the python file to order the scenes and add logic with user input and "if" statements.
- Run the main python file after importing the engine package to play the game in the terminal
