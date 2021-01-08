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
1.) Log into the AWS Console<br>
2.) Select the EC2 Instance<br>
![S1](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S1.PNG)<br>
3.) Select Launch Instance<br>
![S2](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S2.PNG)<br>
4.) Create your EC2 Instance <br>
-- a.) Select the: Amazon Linux 2 AMI <br>
![S3](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S3.PNG)<br>
-- b.) Select the Free Tier Options <br>
![S4](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S3b.PNG)<br>
-- c.) In the upper hot bar, Configure Security Groups <br>
-- d.) Open all Ports to anywhere across: SSH, HTTP, and HTTPS <br>
![S5](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S3c.PNG)<br>
-- e.) Reveiew and Launch Instance <br>
-- f.) GENERATE NEW PEM USER KEY AND KEEP THIS SAFE <br>
![S6](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S3d.PNG)<br>
5.) Use the Pem file and MobaXterm to remotely log in<br>
![S7](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S4a.PNG)<br>
![S8](https://github.com/Russel-Mendes/IEEE-AWS-Webserver/blob/main/readme_img/S4b.PNG)<br>  
6.) Install Python and Flask<br>
7.) Transfer the Project Files<br>
8.) Start the server with "sudo python3 core.py"<br>
9.) Go to AWS console and find the public DNS address<br>
10.) Follow the public address to your new webpage<br>
11.) To shut down, go to EC2 console and stop all running instances<br>


## Author
* **Russel Mendes** 

## Credits
* This seminar was created by Russel Mendes - https://github.com/Russel-Mendes
