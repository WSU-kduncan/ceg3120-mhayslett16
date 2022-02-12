# Project 2  
# Macie Hayslett  
  
## Part 1: Build a VPC  
1.Create a VPC:  
![VPC Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC%20Details.JPG)  
2.Create a subnet  
![Subnet Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC-subnet%20Details.JPG)  
3.Create an internet gateway  
![Internet Gateway Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC-gw%20Details.JPG)  
4.Create a route table  
![Route Table Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC-routetable%20Details%201.JPG)  
![More Route Table Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC-routetable%20Details%202.JPG)  
5.Create a security group  
![Security Group Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC-sg%20Details%201.JPG)  
![More Security Group Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/VPC-sg%20Details%202.JPG)  
  
## Part 2: EC2 Instances  
1.Creating a new instance: Selected the Amazon Linux 2 AMI with the default username of ec2-user. Used the t2.micro instance type because it was a cheap option.  
2.Attaching instance to VPC: Selected “Next:Configure Instance Details”, then attached it to my VPC under the “Network” drop-down.  
3.I chose not to auto-assign public IPv4. This was mostly because I was following the in-class demo.  
4.Attaching a Volume to the instance: Hit “Add New Volume” in the “Add Storage” section of the AMI creation steps. Used default settings.  
5.Tagging the Instance: In “Add Tags” section of AMI creation, selected “Add tag” and typed it in. Use the tag “Name” with the value off what I wanted to name it (HAYSLETT-instance in this case)   
6.Associate your Security Group: Selected my security group name from the list under the “Select from an existing security group” option in the AMI creation process.  
7.Reserve an Elastic IP Address: Went to the “Elastic Ips” section in the EC2 menu (under “Network & Security” section). Selected “Allocate Elastic IP Address” in the top-right corner. Used defaults and named It “HAYSLETT-EIP”. In the Elastic IP addresses section, hit the “Actions” drop-down menu, and select “Associate IP” and select your instance you want to assign the IP to.  
8.My Instance Details:   
![AMI Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/AMI-instance%201.JPG)   
![More AMI Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/AMI-instance%202.JPG)  
9.Change the hostname of our AMI: I first copied the contents of /etc/hostname to a file called /etc/hostname.old as suggested, just to be safe. I followed this 5 step guide: https://www.cyberciti.biz/faq/set-change-hostname-in-amazon-linux-ec2-instance-server/  
- Use the hostnamectl command to set your hostname; we’re using hayslett-amazonlinux2  
- Open the /etc/hosts file
- Append “hayslett-amazonlinux2” to the 127.0.0.1 entry in /etc/hosts  
- Save and close the /etc/hosts file  
- Reboot   
10. Running the ssh connection:  
![ssh Details]( https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/project2/AMI-ssh.JPG)   

