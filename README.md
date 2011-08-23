## Description
每次都會有這樣的需求我要輸入英文地址，或是輸入一個常常用的domain name，比如說AWS的public dns，我寫了一個工具可以把一些妳常常用的內容存在一個像是hash一樣的表單，只要透過像這樣的command就可以快速複製到clipboard:


## Usage
./copycat -s "home address xxxx" eng-addr

./copycat eng-addr
result: "home address xxx" -> clipboard

./copycat --list
result:
list all variables with its name and value

./copycat -d eng-addr
result:
deleted the variable which has the name as you gave.

./copycat -D
result:
cleanup the all copy table.
