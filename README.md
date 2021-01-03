# IEEE How-To: AWS Webserver
Amazon Web Services (AWS) is one of the world's largest cloud platforms. As the world becomes more digitized, to satisfy the needs of industry and society, internet solutions migrate to cloud platforms to achieve light-speed performance and world-wide resilance. Come to the IEEE "How-To:AWS-Webserver" sesion, where we take a hands-on approach on learning the basics of the cloud. From the comforts of your own computer, learn how to lauch a webserver that can be accessed by the world.  

## Goals
- Getting familiar with AWS Console
- Launching an EC2 (Elastic Cloud Compute) Instance
- Logging into an EC2 instance remotely
- Creating and transferring files remotely
- Lauching a Flask Webserver
- Shutting down and cleaning workspace

### Tools Used 
- MobaXterm


## Steps
1.) Log into the AWS Console
2.) Select the EC2 Instance
3.) Select Launch Instance
4.) Create your EC2 Instance
-- a.) Select the: Amazon Linux 2 AMI 
-- b.) Select the Free Tier Options
-- c.) In the upper hot bar, Configure Security Groups
-- d.) Open all Ports to anywhere across: SSH, HTTP, and HTTPS
-- e.) Reveiew and Launch Instance
-- f.) GENERATE NEW PEM USER KEY AND KEEP THIS SAFE
5.) Use the Pem file and MobaXterm to remotely log in
6.) Install Python and Flask
7.) Transfer the Project Files
8.) Start the server with "sudo python3 core.py"
9.) Go to AWS console and find the public DNS address
10.) Follow the public address to your new webpage
11.) To shut down, go to EC2 console and stop all running instances


## Author
* **Russel Mendes** 

## Credits
* This seminar was created by Russel Mendes - https://github.com/Russel-Mendes
