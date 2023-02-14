# Ubuntu Config for syslog 
- You might need excon for ifconfig. Just hook it up no ip config required because of dhcp settings in ubuntu network file


- https://www.xmodulo.com/configure-syslog-server-linux.html

-(I think this HOSTNAME can be anything) $template RemoteLogs,"/var/log/%HOSTNAME%/%PROGRAMNAME%.log" *
*.*  ?RemoteLogs 
& ~


- (for all logs) $template IpTemplate,"/var/log/%FROMHOST-IP%.log" 
*.*  ?IpTemplate 
& ~ 


- The logs will be fount in /var/log for you to cat 