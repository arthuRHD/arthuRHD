

[![docker](https://img.shields.io/badge/Docker_Hub-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/u/arichard76)
[![pypi](https://img.shields.io/badge/PyPI.org-3775A9?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/user/arthuRHD/)
[![googleplaystore](https://img.shields.io/badge/Play_Store-00AC47?style=for-the-badge&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/developer?id=arthuRHD)
[![readdotcv](https://img.shields.io/badge/Read.cv-111111?style=for-the-badge&logo=readdotcv&logoColor=white)](https://read.cv/arthurrhd)
[![bentome](https://img.shields.io/badge/Bento.me-FFFFFF?style=for-the-badge&logo=bento&logoColor=black)](https://bento.me/arthurrhd)

```ini
[proxy]

; NTLM server(s) to connect through. IP:port, hostname:port
;   Multiple proxies can be specified comma separated. Px will iterate through
;   and use the one that works
server =

; PAC file to use to connect
;   Use in place of --server if PAC file should be loaded from a URL or local
;   file. Relative paths will be relative to the Px script or binary
pac =

; PAC file encoding
;   Specify in case default 'utf-8' encoding does not work
; pac_encoding =

; Network interface(s) to listen on. Comma separated, default: 127.0.0.1
;   --gateway and --hostonly override this to bind to all interfaces
listen = 127.0.0.1

; Port to run this proxy on - default: 3128
port = 3128

; Allow remote machines to use proxy. 0 or 1, default: 0
;   Overrides --listen and binds to all interfaces
gateway = 0

; Allow only local interfaces to use proxy. 0 or 1, default: 0
;   Px allows all IP addresses assigned to local interfaces to use the service.
;   This allows local apps as well as VM or container apps to use Px when in a
;   NAT config. Overrides --listen and binds to all interfaces, overrides the
;   default --allow rules
hostonly = 0

; Allow connection from specific subnets. Comma separated, default: *.*.*.*
;   Whitelist which IPs can use the proxy. --hostonly overrides any definitions
;   unless --gateway mode is also specified
;   127.0.0.1 - specific ip
;   192.168.0.* - wildcards
;   192.168.0.1-192.168.0.255 - ranges
;   192.168.0.1/24 - CIDR
allow = *.*.*.*

; Direct connect to specific subnets or domains like a regular proxy. Comma separated
;   Skip the NTLM proxy for connections to these hosts
;   127.0.0.1 - specific ip
;   192.168.0.* - wildcards
;   192.168.0.1-192.168.0.255 - ranges
;   192.168.0.1/24 - CIDR
;   example.com - domains
noproxy =

; Override or send User-Agent header on client's behalf
useragent =

; Authentication to use when SSPI is unavailable. Format is domain\username
; Service name "Px" and this username are used to retrieve the password using
; Python keyring if available.
username =

; Force instead of discovering upstream proxy type
;   By default, Px will attempt to discover the upstream proxy type. This
;   option can be used to force either NEGOTIATE, NTLM, DIGEST, BASIC or the
;   other libcurl supported upstream proxy types. See:
;     https://curl.se/libcurl/c/CURLOPT_HTTPAUTH.html
;   To control which methods are available during proxy detection:
;     Prefix NO to avoid method - e.g. NONTLM => ANY - NTLM
;     Prefix SAFENO to avoid method - e.g. SAFENONTLM => ANYSAFE - NTLM
;     Prefix ONLY to support only that method - e.g ONLYNTLM => ONLY + NTLM
;   Set to NONE to defer all authentication to the client. This allows multiple
;   instances of Px to be chained together to access an upstream proxy that is not
;   directly connected:
;     Client -> Auth Px -> no-Auth Px -> Upstream proxy
;       'Auth Px' cannot directly access upstream proxy but 'no-Auth Px' can
auth =

[client]

; Client authentication to use when SSPI is unavailable. Format is domain\username
; Service name "PxClient" and this username are used to retrieve the password using
; Python keyring if available.
client_username =

; Enable authentication for client connections. Comma separated, default: NONE
; Mechanisms supported: NEGOTIATE, NTLM, DIGEST, BASIC
;   ANY     = enable all supported mechanisms
;   ANYSAFE = enable all supported mechanisms except BASIC
;   NTLM    = enable only NTLM, etc.
;   NONE    = disable client authentication altogether (default)
client_auth = NONE

; Disable SSPI for client authentication on Windows. default: 0
;   Set to 1 to disable SSPI and use the configured username and password
client_nosspi = 0

[settings]

; Number of parallel workers (processes). Valid integer, default: 2
workers = 2

; Number of parallel threads per worker (process). Valid integer, default: 32
threads = 32

; Idle timeout in seconds for HTTP connect sessions. Valid integer, default: 30
idle = 30

; Timeout in seconds for connections before giving up. Valid float, default: 20
socktimeout = 20.0

; Time interval in seconds before refreshing proxy info. Valid int, default: 60
;   Proxy info reloaded from manual proxy info defined in Internet Options
proxyreload = 60

; Run in foreground when compiled or run with pythonw.exe. 0 or 1, default: 0
;   Px will attach to the console and write to it even though the prompt is
;   available for further commands. CTRL-C in the console will exit Px
foreground = 0

; Enable debug logging. default: 0
;   1 = Log to script dir [--debug]
;   2 = Log to working dir
;   3 = Log to working dir with unique filename [--uniqlog]
;   4 = Log to stdout [--verbose]. Implies --foreground
;   If Px crashes without logging, traceback is written to the working dir
log = 0
```
