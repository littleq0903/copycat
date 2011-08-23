## System Requirement.
* Mac OS X 10.6 or above (Maybe not, but I don't know, it is welcome to give me feedbacks if you tested this stuff on your old Mac. :D
* Python2.5 or above

(P.S. This script will only work on Macintosh system now, because the concept of it is using this command to operate clipboard: `pbcopy`.)


## Installation
1. Clone this project into your computer or download it directly.
`git clone git@github.com:littleq0903/copycat.git`
2. Move it into `~/bin/`, if it doesn't exist, create it.
3. Add the following command in your ~/.profile
`export PATH=$PATH:$HOME/bin`
4. Restart your terminal, and enjoy.


## Description
This is a tool for management of your own clipboard under the command-line environment on a Max, you can store some strings as "name=value" pair, and copy it into your clipboard with the name very fast!


## Usage
`./copycat -s "home address xxxx" eng-addr`

`./copycat eng-addr`
result:
"home address xxx" -> clipboard

`./copycat --list`
result:
list all variables with its name and value

`./copycat -d eng-addr`
result:
deleted the variable which has the name as you gave.

`./copycat -D`
result:
clean the all copy table.
