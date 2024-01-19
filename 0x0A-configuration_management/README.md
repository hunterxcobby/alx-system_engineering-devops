# Project: 0x0A. Configuration management

<img src="./main/cmd_on_wrong_server.gif" alt="cmd_on_wrong_server" width=85%>

## Resources

#### Read or watch:

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Tasks

0. [Create a file](./0-create_a_file.pp)

Using Puppet, create a file in `/tmp`.

Requirements:

- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

Example:

```sh
root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~#
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
```

1. [Install a package](./1-install_a_package.pp)

Using Puppet, install flask from pip3.

Requirements:

- Install `flask`
- Version must be `2.1.0`

Example:

```sh
root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
```

2. [Execute a command](./2-execute_a_command.pp)

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`

Example:

Terminal #0 - starting my process

```sh
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
```

Terminal #1 - executing my manifest

```sh
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/#
```

Terminal #0 - process has been terminated

```sh
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```

---

### Environment

- Language: Puppet Scripts
  - OS: Ubuntu 20.04 LTS
  - Executable: `chmod +x [filename]`; run with `./[filename]`
  - Style guidelines:
    - [Puppet lint](http://puppet-lint.com/)

---

## Author
