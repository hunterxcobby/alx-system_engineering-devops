# Project: 0x05. Processes and Signals

## Resources

#### Read or watch:

* [Linux PID](https://www.linfo.org/pid.html)
* [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
* [Linux signal](https://www.educative.io/answers/what-are-linux-signals)
* [Process management in linux](https://www.digitalocean.com/community/tutorials/process-management-in-linux)
## Learning Objectives

### General

* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored
## Description of what each file shows (Tasks)
* Files that start with with:
0. [What is my PID](./0-what-is-my-pid) :
* Write a Bash script that displays its own PID.
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./0-what-is-my-pid 
	4690
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
* <em>This may vary on your computer.</em>
1. [List your processes](./1-list_your_processes) :
* Write a Bash script that displays a list of currently running processes.
* Requirements:
	- Must show all processes, for all users, including those which might not have a TTY
	- Display in a user-oriented format
	- Show process hierarchy
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./1-list_your_processes | head -20
	USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
	root         1  0.0  0.2 225124  8840 ?        Ss   14:00   0:00 /sbin/init
	root         2  0.0  0.0   2324  1196 ?        Sl   14:00   0:00 /init
	root         5  0.0  0.0   2352    72 ?        Sl   14:01   0:00  \_ plan9 --control-socket 6 --log-level 4 --server-fd 7 --pipe-fd 9 --log-truncate
	root      1004  0.0  0.0   2332   112 ?        Ss   14:01   0:00  \_ /init
	root      1006  0.0  0.0   2348   116 ?        S    14:01   0:00  |   \_ /init
	cobby  1011  0.0  0.1  23248  5328 pts/0    Ss   14:01   0:00  |       \_ -bash
	cobby  6998  0.0  0.0  13324  3144 pts/0    S+   15:15   0:00  |           \_ bash ./1-list_your_processes
	cobby  7000  0.0  0.0  37968  3284 pts/0    R+   15:15   0:00  |           |   \_ ps auxf
	cobby  6999  0.0  0.0   7948   900 pts/0    S+   15:15   0:00  |           \_ head -20
	root      1012  0.0  0.0  78640  3572 pts/1    Ss   14:01   0:00  \_ /bin/login -f
	cobby  1182  0.0  0.1  23084  4808 pts/1    S+   14:01   0:00  |   \_ -bash
	root      1451  0.0  0.0   2328   116 ?        Ss   14:56   0:00  \_ /init
	root      1453  0.0  0.0   2344   120 ?        S    14:56   0:00  |   \_ /init
	cobby  1456  0.0  0.0   4640   780 pts/2    Ss+  14:56   0:00  |       \_ sh -c "$VSCODE_WSL_EXT_LOCATION/scripts/wslServer.sh" f1b07bd25dfad64b0167beb15359ae573aecd2cc stable code-server .vscode-server --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	cobby  1457  0.0  0.0   4640   868 pts/2    S+   14:56   0:00  |           \_ sh /mnt/c/Users/user/.vscode/extensions/ms-vscode-remote.remote-wsl-0.81.8/scripts/wslServer.sh f1b07bd25dfad64b0167beb15359ae573aecd2cc stable code-server .vscode-server --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	cobby  1462  0.0  0.0   4640   828 pts/2    S+   14:56   0:00  |               \_ sh /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/bin/code-server --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	cobby  1466  1.7  2.4 976944 98600 pts/2    Sl+  14:56   0:20  |                   \_ /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/node /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/server-main.js --host=127.0.0.1 --port=0 --connection-token=2916332039-816454802-618581055-3917032058 --use-host-proxy --without-browser-env-var --disable-websocket-compression --accept-server-license-terms --telemetry-level=all
	cobby  1500  0.4  1.6 676344 64832 pts/2    Sl+  14:56   0:05  |                       \_ /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/node /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/bootstrap-fork --type=ptyHost --logsPath /home/cobby/.vscode-server/data/logs/20231027T145627
	cobby  1636  0.0  0.1  23208  5396 pts/5    Ss+  14:56   0:00  |                       |   \_ /bin/bash --init-file /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/vs/workbench/contrib/terminal/browser/media/shellIntegration-bash.sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$
	```
2. [Show your Bash PID](./2-show_your_bash_pid) :
* Using your previous exercise command, write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
- Requirements:
	- You cannot use `pgrep`
	- The third line of your script must be `# shellcheck disable=SC2009` (for more info about ignoring `shellcheck` error [here](https://github.com/koalaman/shellcheck/wiki/Ignore))
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ shell 2-show_your_bash_pid 
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./2-show_your_bash_pid 
	cobby  1011  0.0  0.1  23248  5328 pts/0    Ss+  14:01   0:00  |       \_ -bash
	cobby  1182  0.0  0.1  23084  4808 pts/1    S+   14:01   0:00  |   \_ -bash
	cobby  1636  0.0  0.1  23208  5408 pts/5    Ss   14:56   0:00  |                       |   \_ /bin/bash --init-file /home/cobby/.vscode-server/bin/f1b07bd25dfad64b0167beb15359ae573aecd2cc/out/vs/workbench/contrib/terminal/browser/media/shellIntegration-bash.sh
	cobby  9825  0.0  0.0  13324  3168 pts/5    S+   15:25   0:00  |                       |       \_ bash ./2-show_your_bash_pid
	cobby  9829  0.0  0.0  14864  1008 pts/5    S+   15:25   0:00  |                       |           \_ grep bash
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
3. [Show your Bash PID made easy](./3-show_your_bash_pid_made_easy) :
* Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.
- Requirements:
	- You cannot use `ps`
	```sh
	sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
	4404 bash
	4555 bash
	sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
	4404 bash
	4557 bash
	sylvain@ubuntu$ 
	```
- Here we can see that:
	- For the first iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4555`
	- For the second iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4557`
* P.S (pun intended😅): 
	- The key point to note here is that the bash processes have the same PID in both iterations because they are the same processes that were running before you ran the script. However, the PID of the script (3-show_your_bash_pid_made_easy) is different in each iteration because a new instance of the script is being executed, and each instance of the script has a unique PID.
	- In the context of the script, it's listing the bash processes it finds, along with the PID of the script itself. This is why you see different script PIDs in each iteration, but the bash process PID remains the same because it's the same running bash process.
4. [To infinity and beyond](./4-to_infinity_and_beyond) :
* Write a Bash script that displays To infinity and beyond indefinitely.
	- Requirements:
		- In between each iteration of the loop, add a `sleep 2`
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./4-to_infinity_and_beyond 
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	^C
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
- <em>Note that I `ctrl+c` (killed) the Bash script in the example.</em>
5. [Don't stop me now!](./5-dont_stop_me_now) :
* We stopped our `4-to_infinity_and_beyond` process using `ctrl+c` in the previous task, there is actually another way to do this.
- Write a Bash script that stops `4-to_infinity_and_beyond` process.
- Requirements:
	- You must use `kill`
	<img src="./terminate-process.JPG" alt="Terminate-Process" width=100%>
- I opened 2 terminals in this example, started by running my `4-to_infinity_and_beyond` Bash script in terminal #0 and then moved on terminal #1 to run `5-dont_stop_me_now`. We can then see in terminal #0 that my process has been terminated.
6. [Stop me if you can](./6-stop_me_if_you_can) :
* Write a Bash script that stops `4-to_infinity_and_beyond` process.
- Requirements:
	- You cannot use `kill` or `killall`
7. [Highlander](./7-highlander) :
* Write a Bash script that displays:
	- `To infinity and beyond` indefinitely
	- With a `sleep 2` in between each iteration
	- `I am invincible!!!` when receiving a `SIGTERM` signal
- Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.
	<img src="./die-homelander.JPG" alt="die-homelander" width=100%>
- I started `7-highlander` in Terminal #0 and then run `67-stop_me_if_you_can` in terminal #1, for every iteration we can see `I am invincible!!!` appearing in terminal #0.
8. [Beheaded process](./8-beheaded_process) :
* Write a Bash script that kills the process `7-highlander`.
<img src="./homelander-finally.JPG" alt="homelander-dies" width=100%>

9. [Process and PID file](./100-process_and_pid_file) :
* Write a Bash script that:
	- Creates the file `/var/run/myscript.pid` containing its PID
	- Displays `To infinity and beyond` indefinitely
	- Displays `I hate the kill command` when receiving a SIGTERM signal
	- Displays `Y U no love me?!` when receiving a SIGINT signal
	- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./100-process_and_pid_file 
	./100-process_and_pid_file: line 20: /var/run/myscript.pid: Permission denied
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	^CY U no love me?!
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	^CY U no love me?!
	To infinity and beyond
	To infinity and beyond
	To infinity and beyond
	I hate the kill command
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
10. [Manage my process](./101-manage_my_process) :
* Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.
- Write a `manage_my_process` Bash script that:
	- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
	- In between every `I am alive!` message, the program should pause for 2 seconds
- Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)
- Requirements:
	- When passing the argument `start`:
		- Starts `manage_my_process`
		- Creates a file containing its PID in `/var/run/my_process.pid`
		- Displays `manage_my_process started`
	- When passing the argument `stop`:
		- Stops `manage_my_process`
		- Deletes the file `/var/run/my_process.pid`
		- Displays `manage_my_process stopped`
	- When passing the argument `restart`
		- Stops `manage_my_process`
		- Deletes the file `/var/run/my_process.pid`
		- Starts `manage_my_process`
		- Creates a file containing its PID in `/var/run/my_process.pid`
		- Displays `manage_my_process restarted`
	- Displays Usage: `manage_my_process {start|stop|restart}` if any other argument or no argument is passed
* Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.
	```sh
	sylvain@ubuntu$ sudo ./101-manage_my_process
	Usage: manage_my_process {start|stop|restart}
	sylvain@ubuntu$ sudo ./101-manage_my_process start
	manage_my_process started
	sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
	I am alive!
	I am alive!
	I am alive!
	I am alive!
	^C
	sylvain@ubuntu$ sudo ./101-manage_my_process stop
	manage_my_process stopped
	sylvain@ubuntu$ cat /var/run/my_process.pid 
	cat: /var/run/my_process.pid: No such file or directory
	sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
	^C
	sylvain@ubuntu$ sudo ./101-manage_my_process start
	manage_my_process started
	sylvain@ubuntu$ cat /var/run/my_process.pid 
	11864
	sylvain@ubuntu$ sudo ./101-manage_my_process restart
	manage_my_process restarted
	sylvain@ubuntu$ cat /var/run/my_process.pid 
	11918
	sylvain@ubuntu$ tail -f -n0 /tmp/my_process 
	I am alive!
	I am alive!
	I am alive!
	^C
	sylvain@ubuntu$ 
	```
11. [Zombie](./102-zombie.c) :
* Read [what a zombie process is](https://zombieprocess.wordpress.com/what-is-a-zombie-process/).
- Write a C program that creates 5 zombie processes.
- Requirements:
	- For every zombie process created, it displays `Zombie process created, PID: ZOMBIE_PID`
	- Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
	- When your code is done creating the parent process and the zombies, use the function below
	```c
	int infinite_while(void)
	{
		while (1)
		{
			sleep(1);
		}
		return (0);
	}
	```
	```sh
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ betty 102-zombie.c 

	========== 102-zombie.c ==========
	infinite_while
	main
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ gcc 102-zombie.c -o zombie
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ ./zombie 
	Zombie process created, PID: 27987
	Zombie process created, PID: 27988
	Zombie process created, PID: 27989
	Zombie process created, PID: 27991
	Zombie process created, PID: 27990
	^C
	cobby@ubuntu:~/alx-system_engineering-devops/0x05-processes_and_signals$ 
	```
	```sh
	sylvain@ubuntu$ ps aux | grep -e 'Z+.*<defunct>'
	sylvain  13527  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
	sylvain  13528  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
	sylvain  13529  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
	sylvain  13530  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
	sylvain  13531  0.0  0.0      0     0 pts/0    Z+   01:19   0:00 [zombie] <defunct>
	sylvain  13533  0.0  0.1  10460   964 pts/2    S+   01:19   0:00 grep --color=auto -e Z+.*<defunct>
	sylvain@ubuntu$
	```
* In Terminal #0, I start by compiling `102-zombie.c` and executing `zombie` which creates 5 zombie processes. In Terminal #1, I display the list of processes and look for lines containing `Z+.*<defunct>` which catches zombie process.
---
### Environment
* Language: Bash Scripts
    * OS: Ubuntu 20.04 LTS
    * Executable: `chmod +x [filename]`; run with `./[filename]`
    * Style guidelines:
        - [Shellcheck](https://github.com/koalaman/shellcheck)
---
## Author

