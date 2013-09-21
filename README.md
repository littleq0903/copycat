## System Requirement.
* Mac OS X 10.6 or above or Linux or Windows (Maybe not, but I don't know, it is welcome to give me feedbacks if you tested this stuff on your old Mac. :D
* Python2.5 or above

(P.S. This script will only work on Macintosh system now, because the concept of it is using this command to operate clipboard: `pbcopy`.)


## Requirement
1. https://github.com/georgefs/pyclip
2. https://github.com/moskytw/clime



## Installation
1. Clone this project into your computer or download it directly.
`git clone https://github.com/georgefs/copycat.git`
2. `python install setup.py install`
3. Restart your terminal, and enjoy.


## Description
This is a tool for management of your own clipboard under the command-line environment on a Max, you can store some strings as "name=value" pair, and copy it into your clipboard with the name very fast!


## Usage

###command line support 
1. copy into clipboard `copycat "some thing"`
2. past from clipboard `copycat --paste` or `copycat -p`
3. named clipboard `copycat --name=name "some thing"` or `copycat -n name "some thing"` and `copycat --paste --name=name` or `copycat -pn name`
4. support stdin `echo test|copycat` or `cat file|copycat -n name`..
5. list `copycat --list` or `copycat -l`
6. remove `copycat --delete --name name` or `copycat -dn name`

###python method
```python
import copycat
copycat.copy(value='value', name='name')
copycat.paste(name='name')
```
