```
  ____                            _   
 / ___|___  _ __  _   _  ___ __ _| |_ 
| |   / _ \| '_ \| | | |/ __/ _` | __|
| |__| (_) | |_) | |_| | (_| (_| | |_ 
 \____\___/| .__/ \__, |\___\__,_|\__|
           |_|    |___/               

Command-line based clipboard tool for every command-line Ninja
```

## Description
This is a clipboard tool for command-line heavy users, especially the users who are using only console mode in daily life. Traditional clipboard stores only 1 value at the same time, copycat doesn't but store as many as you could. (if you remember their name), you could store 1 value into your system clipboard(anonymously) or store many named records.

## System Requirement.
* Supported operating systems:
    * Mac OS X 10.6 or above version
    * Linux with `xclip` installed
    * Windows (testing, we're both not familiar with Windwos, if you would add some support to Windows part, we will appreciate that. :)
* Python 2.5 or above version

(P.S. This script will only work on Macintosh system for now, because the concept of it is using this command to operate clipboard: `pbcopy`.)


## Requirement
1. [pyclip](https://github.com/georgefs/pyclip) by @georgefs
2. [clime](https://github.com/moskytw/clime) by @moskytw


## Installation
1. Clone this project into your computer or download it directly.
`git clone https://github.com/georgefs/copycat.git`
2. `python install setup.py install`
3. Restart your terminal, and enjoy.


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

## Contributors

* @littleq0903
* @georgeli

Contributions are welcome, just send me your pull request and briefly describe what have you done!