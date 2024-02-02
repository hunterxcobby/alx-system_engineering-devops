# Project: 0x10. HTTPS SSL

## Resources

### Read or watch:-

- [What is HTTPS?](https://www.instantssl.com/http-vs-https)
- [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
- [HAProxy SSL termination on Ubuntu16.04](https://docs.ionos.com/cloud/)
- [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
- [Bash function](https://tldp.org/LDP/abs/html/complexfunct.html)

## Learning Objectives

### General

- What is HTTPS SSL 2 main roles
- What is the purpose encrypting traffic
- What SSL termination means

## Tasks

0. [World wide web](./0-world_wide_web) :

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

- Add the subdomain `www` to your domain, point it to your `lb-01` IP (your domain name might be configured with default subdomains, feel free to remove them)
- Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
- Add the subdomain `web-01` to your domain, point it to your `web-01` IP
- Add the subdomain `web-02` to your domain, point it to your `web-02` IP
- Your Bash script must accept 2 arguments:
  1. `domain`:
     - type: string
     - what: domain name to audit
     - mandatory: yes
  2. `subdomain`:
     - type: string
     - what: specific subdomain to audit
     - mandatory: no
- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter domain is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
- When passing `domain` and `subdomain` parameters, display information for the specified subdomain
- Ignore `shellcheck` case `SC2086`
- Must use:
  - `awk`
  - at least one Bash function
- You do not need to handle edge cases such as:
  - Empty parameters
  - Nonexistent domain names
  - Nonexistent subdomains

Example:

```sh
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```

1. [HAproxy SSL termination](./1-haproxy_ssl_termination) :

“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`.

Requirements:

- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic
- HAproxy must serve encrypted traffic that will return the `/` of your web server
- When querying the root of your domain name, the page returned must contain `Holberton School`
- Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `1-haproxy_ssl_termination` must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy) is not available before v1.5.

Example:

```sh
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```

---

### Environment

- Language: Bash Scripts
  - OS: Ubuntu 20.04 LTS
  - Executable: `chmod +x [filename]`; run with `./[filename]`
  - Style guidelines:
    - [Shellcheck](https://github.com/koalaman/shellcheck)

---

