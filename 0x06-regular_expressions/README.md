# Project: 0x06. Regular expression
<img src="./extra/regex_now_2_problems.jpg" alt="Regex_2_problems" width=75%>

## Background Context
* For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.
* Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:
```sh
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```
* Install with ruby with: `sudo apt install ruby-full`

## Resources

#### Read or watch:

* [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
* [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
* [Rubular is your best friend](https://rubular.com/)
* [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
* [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Description of what each file shows (Tasks):
* extra	--- folder that contains concept to better understand the project and JPEGs for README.
* Files that start with:
0. [Simply matching School](./0-simply_match_school.rb):
<img src="./extra/regex-task0.png" alt="Task-0" width=100%>

* Requirements:
	- The regular expression must match `School`
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
- Example:
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb School | cat -e
	School$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb "Best School" | cat -e
	School$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb "School Best School" | cat -e
	SchoolSchool$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
	$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ 
	```
1. [Repetition Token #0](./1-repetition_token_0.rb) :
<img src="./extra/regex-task1.png" alt="Task-1" width=100%>

* Requirements:
	- Find the regular expression that will match the above cases
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* The [website](regex101.com) is awesome to test out how exactly it works. So we just insert the test string from the image above (left part) and then put in the regular expression `hbt{2,5}n` and see how it matches.
2. [Repetition Token #1](./2-repetition_token_1.rb) :
<img src="./extra/regex-task2.png" alt="Task-2" width=100%>

* Requirements:
	- Find the regular expression that will match the above cases
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
3. [Repetition Token #2](./3-repetition_token_2.rb) :
<img src="./extra/regex-task3.png" alt="Task-3" width=100%>

* Requirements:
	- Find the regular expression that will match the above cases
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
4. [Repetition Token #3](./4-repetition_token_3.rb) :
<img src="./extra/regex-task4.png" alt="Task-4" width=100%>

* Requirements:
	- Find the regular expression that will match the above cases
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
	- Your regex should not contain square brackets
5. [Not quite HBTN yet](./5-beginning_and_end.rb) :
* Requirements:
	- The regular expression must be exactly matching a string that starts with `h` ends with `n` and can have any single character in between
	- Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./5-beginning_and_end.rb 'hn' | cat -e
	$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./5-beginning_and_end.rb 'hbn' | cat -e
	hbn$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./5-beginning_and_end.rb 'hbtn' | cat -e
	$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$ ./5-beginning_and_end.rb 'h8n' | cat -e
	h8n$
	cobby@ubuntu:~/alx-system_engineering-devops/0x06-regular_expressions$  
	```
6. [Call me maybe](./6-phone_number.rb) :
* This task is brought to you by a professional advisor [Neha Jain](https://twitter.com/_nehajain), Senior Software Engineer at LinkedIn.
* Requirements
	- The regular expression must match a 10 digit phone number
	```sh
	sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
	4155049898$
	sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
	$
	sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
	$
	sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
	$
	sylvain@ubuntu$
	```
7. [OMG WHY ARE YOU SHOUTING?](./7-OMG_WHY_ARE_YOU_SHOUTING.rb) :
<img src="./extra/regex-task7.jpg" alt="Task-7" width=35%>

* Requirement:
	- The regular expression must be only matching: capital letters
- Example:
	```sh
	sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
	ILOVESYSADMIN$
	sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
	WHATSAY$
	sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
	$*
	sylvain@ubuntu$
	```
8. [Textme](./100-textme.rb) :
* This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on [Twitter](https://twitter.com/gui).
* For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.
* Requirements:
	- Your script should output: `[SENDER],[RECEIVER],[FLAGS]`
	- The sender phone number or name (including country code if present)
	- The receiver phone number or name (including country code if present)
	- The flags that were used
* Example:
	```sh
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
	Google,+16474951758,-1:0:-1:0:-1
	$
	$
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly ninety-two million miles is an utterly insignificant little blue green planet whose ape-descended] [udh:0:]'
	+17272713208,+19172319348,-1:0:-1:0:-1
	$
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:18572406905] [to:14022180266] [flags:-1:0:-1:-1:-1] [msg:136:Far out in the uncharted backwaters of the unfashionable end of the western spiral arm of the Galaxy lies a small unregarded yellow sun.] [udh:0:]'
	18572406905,14022180266,-1:0:-1:-1:-1
	$
	$
	$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-11 mdr: 2016-02-01 11:00:00 Sent SMS [SMSC:SYBASE1] [SVC:backendtextme] [ACT:] [BINF:] [FID:] [from:12392190384] [to:19148265919] [flags:-1:0:-1:-1:-1] [msg:99:life forms are so amazingly primitive that they still think digital watches are a pretty neat idea.] [udh:0:]'
	12392190384,19148265919,-1:0:-1:-1:-1
	$
	```
---
### Environment
* Language: Ruby Scripts
    * OS: Ubuntu 20.04 LTS
    * Executable: `chmod +x [filename]`; run with `./[filename]`
    * Style guidelines:
        - ?, 🤭just write clean scripts.
---
## Author

- **<em>Website</em>** - [Ayomide Kayode](https://github.com/AyomideKayode)
- **<em>ALX Software Engineering Program</em>** - [ALX_AFRICA](https://www.alxafrica.com/programmes/)
- **<em>Twitter</em>** - [@kazzy_wiz](https://www.twitter.com/kazzy_wiz)
