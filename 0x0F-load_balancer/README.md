# Project: 0x0F. Load balancer

## Resources

### Read or watch :-

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)

## Tasks

0. [Double the number of webservers](./0-custom_http_response_header) :

In this first task you need to configure `web-02` to be identical to `web-01`. Fortunately, you built a Bash script during your web server project, and they’ll now come in handy to easily configure `web-02`. Remember, always try to automate your work!

Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.

Requirements:

- Configure Nginx so that its HTTP response contains a custom header (on `web-01` and `web-02`)
  - The name of the custom HTTP header must be `X-Served-By`
  - The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `0-custom_http_response_header` so that it configures a brand new Ubuntu machine to the requirements asked in this task
  - Ignore SC2154 for `shellcheck`

Example:

```sh
cobby@cobby-VirtualBox:~/alx-system_engineering-devops/0x0F-load_balancer$ curl -sI 100.25.151.196 | grep X-Served-By
X-Served-By: 444607-web-02
cobby@cobby-VirtualBox:~/alx-system_engineering-devops/0x0F-load_balancer$ curl -sI 100.26.11.61 | grep X-Served-By
X-Served-By: 444607-web-01
cobby@cobby-VirtualBox:~/alx-system_engineering-devops/0x0F-load_balancer$
```

If your server’s hostnames are not properly configured ([STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.), follow this [tutorial](https://repost.aws/knowledge-center/linux-static-hostname).

The Hostname configuration in server:

- ssh into server `ssh ubuntu@your_web_ip`
- Edit the Nginx default configuration file: `sudo vi /etc/nginx/sites-available/default`
- Add the following line inside the server block, just above the closing brace (}): `add_header X-Served-By $hostname;`
- Restart Nginx to apply the configuration: `sudo service nginx restart`

Repeat saem steps for web-02!🥂

1. [Install your load balancer](./1-install_load_balancer) :

Install and configure HAproxy on your `lb-01` server.

Requirements:

- Configure HAproxy so that it send traffic to `web-01` and `web-02`
- Distribute requests using a roundrobin algorithm
- Make sure that HAproxy can be managed via an init script
- Make sure that your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. If not, follow this [tutorial](https://repost.aws/knowledge-center/linux-static-hostname).
- For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements

Example:

```sh
cobby@cobby-VirtualBox:~/alx-system_engineering-devops/0x0F-load_balancer$ curl -Is 34.229.137.67
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Mon, 08 Jan 2024 16:34:00 GMT
content-type: text/html
content-length: 612
last-modified: Wed, 03 Jan 2024 14:15:41 GMT
etag: "65956c0d-264"
x-served-by: 444607-web-01
accept-ranges: bytes

cobby@cobby-VirtualBox:~/alx-system_engineering-devops/0x0F-load_balancer$ curl -Is 34.229.137.67
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Mon, 08 Jan 2024 16:34:47 GMT
content-type: text/html
content-length: 612
last-modified: Mon, 08 Jan 2024 15:45:21 GMT
etag: "659c1891-264"
x-served-by: 444607-web-02
accept-ranges: bytes

cobby@cobby-VirtualBox:~/alx-system_engineering-devops/0x0F-load_balancer$
```

Make sure that HAProxy is installed in the lb-01 server before running the curl commands in your terminal.

2. [Add a custom HTTP header with Puppet](./2-puppet_custom_http_response_header.pp) :

Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

- The name of the custom HTTP header must be `X-Served-By`
- The value of the custom HTTP header must be the hostname of the server Nginx is running on
- Write `2-puppet_custom_http_response_header.pp` so that it configures a brand new Ubuntu machine to the requirements asked in this task

---

### Environment

- Language: Bash Scripts
  - OS: Ubuntu 20.04 LTS
  - Executable: `chmod +x [filename]`; run with `./[filename]`
  - Style guidelines:
    - [Shellcheck](https://github.com/koalaman/shellcheck)

---