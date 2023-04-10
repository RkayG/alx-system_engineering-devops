 SSL

In this project, I learned about the importance of HTTPS and how it works. I
configured my HolbertonBnB web servers with `certbot` certificate and HAproxy
SSL termination.

## Tasks :page_with_curl:

* **1. World wide web**
  * [1-world_wide_web](./1-world_wide_web): Bash script that displays
  information about subdomains on my configured servers.
  * Usage: `./1-world_wide_web <domain> <subdomain>`
  * Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and
  points to [DESTINATION]`
  * If no `subdomain` parameter is passed, displays information about the
  subdomains `www`, `lb-01`, `web-01` and `web-02`, in that order.

* **2. HAproxy SSL termination**
  * [2-haproxy_ssl_termination](./2-haproxy_ssl_termination): HAproxy
  configuration file that accepts encrypted SSL traffic for the subdomain
  `www.` on TCP port 443.

* **3. No loophole in your website traffic**
  * [100-redirect_http_to_https](./100-redirect_http_to_https): HAproxy
  configuration file that automatically redirects HTTP traffic to HTTPS.
    log     /dev/log local0
    maxconn 2048
    user    haproxy
    group   haproxy
    tune.ssl.default-dh-param 2048

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    retries 3
    option  redispatch
    timeout connect  5000
    timeout client  10000
    timeout server  10000
    option  forwardfor
    option  http-server-close

frontend www-http
    bind   0.0.0.0:80
    reqadd X-Forwarded-Proto:\ http
    default_backend www-backend
    redirect scheme https code 301 if !{ ssl_fc }

frontend www-https
    bind   0.0.0.0:443 ssl crt /etc/haproxy/certs/www.rkayg.site.pem
    reqadd X-Forwarded-Proto:\ https
    acl    letsencrypt-acl path_beg /.well-known/acme-challenge/
    use_backend letsencrypt-backend if letsencrypt-acl
    default_backend www-backend

backend www-backend
    balance  roundrobin
    redirect scheme https if !{ ssl_fc }
    server 375-web-01 104.196.168.90:80 check
    server 375-web-02 35.196.46.172:80 check

backend letsencrypt-backend
    server letsencrypt 127.0.0.1:54321

