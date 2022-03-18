# Project 4  
  
## Part 1 - CloudFormation Template TODOs  
  
- Changes have been made to the included cf-template.yml file  
  
## Part 2 - Setup Load Balancing TODOs  
  
1. Create an /etc/hosts file on each system that correlates hostnames to private IPs: 
- There was already a /etc/hosts file on each of the systems. I basically just configured them by typing the private IP address followed by the name I wanted to associate it with. (Example: 10.0.1.10 webserv1 would show that the address 10.0.1.10 is associated with webserv1)  
2. Document how to SSH between the systems utilizing their private IPs:  
- From the proxy instance we can ssh into our two web servers. I chose to do what I'm more familiar with, so I copied the key file from my local machine. That way I can use ssh -i [key] ubuntu@[privateIP] to move between systems. I just logged into the proxy instance 3 times and opened an instance of each web server by ssh'ing in like this.  
3. HAProxy Configuration & Documentation:    
- Edited the haproxy.cfg file under /etc/haproxy to make edits and add frontend and backend configurations  
- Commented out unecessary https configurations under global section.  
- Added frontend section. Put proxy instance's public ip as frontend address. Binded to proxy instance's private ip. Made the default backend set as web_servers.  
- Added backend section and set as web_servers. Set allocation method as roundrobin and enabled "option httpchk HEAD /". Set webserv1 and webserv2 as servers in the pool and provided their private ips attached to port 80.
- This configuration allows the proxy to pull the webpages from webserv1 and webserv2 in alternation on the proxy's ip address.  
- restart the haproxy service with sudo systemctl restart haproxy  
- I relied mainly on the resources that were provided (webex and sites), but also googled my way through some basic commands.  
4. Webserver Configurations & Documentation:    
- Edited the index.html file under /var/www/html to change the web pages of the 2 web servers  
- These site content files are located under /var/www/html because that's where apache looks for the content by default.  
- Use systemctl restart apache2 to restart the apache2 service  
5. Proxy server connections: 
- ![webserver1](https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project4/server1-proof.JPG)  
- ![webserver2](https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project4/server2-proof.JPG)
6. Link to webpage:  
- (It's nothing fancy, just the example webpages you provided)  184.73.54.136
7. Reasons I suck:
- I struggled for 30+ minutes trying to get the webpages to show up in th ereal world before making haproxy or anything. Love it.    
