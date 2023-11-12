
# UCS2501-Computer Networks-Team 2-Establishing a Home PC Server: Enabling Remote File Retrieval via FTP


This project demonstrates the creation of a FTP server on one's home PC, and allows users across the Internet to retrieve files from it. 

This project aims to address the challenges of establishing a secure FTP server in network environments with restrictions on NAT, port forwarding, and firewall configurations. Leveraging Python for server-side scripting and ngrok for secure external access, the project offers a solution that bypasses traditional obstacles. The accompanying front-end, built with HTML, JavaScript, jQuery, and AJAX, provides a user-friendly interface for seamless interaction.




## Authors

- [Pooja Premnath](https://github.com/PoojaPremnath2003)
- [Rakshith Subramanian](https://github.com/CoderRak)
- [Tejas Venkataramanan](https://github.com/tejasv16)
- [Yashasvee Vijaykumar](https://github.com/Yashasvee-second)



## Tech Stack

**Client:** HTML, JavaScript, JQuery, TailwindCSS

**Server:** Python3


## System Configuration

If you're using a Windows PC, it is necessary to make some changes to enable FTP on your PC.

**Enabling FTP:**
To enable FTP on a Windows system, one must do the following: First, navigate to the "Control Panel" and select "Programs and Features." From there, choose "Turn Windows features on or off" and locate "Internet Information Services." Expand the "FTP Server" option, check "FTP Extensibility" and "FTP Service," and proceed with the installation. Once installed, configure FTP settings within IIS, specifying authentication methods and access permissions for enhanced security. This integration allows for the seamless utilization of FTP protocols, transforming the Windows machine into an FTP server.

<img width="778" alt="image" src="https://github.com/PoojaPremnath2003/NetworksProject_TeamNo2/assets/88699435/89961093-272b-49e8-94d1-5bd0a86c6e6d">

**Circumventing Firewalls:**
When dealing with rigid firewall settings, it might be necessary to temporarily disable or adjust the firewall to facilitate smooth communication. In Windows, access the "Control Panel" and navigate to "System and Security" and then "Windows Defender Firewall." Here, one can either create specific inbound rules to permit FTP traffic on the designated port or, in situations where FTP access is impeded, temporarily disable the firewall for testing purposes. 

<img width="588" alt="image" src="https://github.com/PoojaPremnath2003/NetworksProject_TeamNo2/assets/88699435/abbe548e-2655-48a0-90a1-c890c05ac60f">


## Installation

Download Ngrok for Windows/MacOs/Linux

[Ngrok Download](https://ngrok.com/download)
## Run Locally

Clone the project

```bash
  git clone https://github.com/PoojaPremnath2003/NetworksProject_TeamNo2
```

Go to the project directory where the FTP server Python file is present

```bash
  cd ..\Simple_FTP_Server
```

Start the server

```bash
  python ftpserver.py
```

Run Ngrok by clicking on the Application file downloaded

Establish a connection with Ngrok, using the port number specified in the code 

```bash
  ngrok tcp 1515 
```

Copy the link created in the Ngrok terminal into a web browser

```bash
  http://0.tcp.in.ngrok.io:12584
```


## Usage/Examples

**Run Python script to start the server**\
<img width="424" alt="image" src="https://github.com/PoojaPremnath2003/NetworksProject_TeamNo2/assets/88699435/d8383902-52f2-453b-a314-8d235a88b9c8">

**Initialize and begin an Ngrok session**\
<img width="728" alt="image" src="https://github.com/PoojaPremnath2003/NetworksProject_TeamNo2/assets/88699435/a4365870-6dab-42d2-9162-82f5876d4f57">

**Server Administrator Login**\
<img width="655" alt="image" src="https://github.com/PoojaPremnath2003/NetworksProject_TeamNo2/assets/88699435/fd7caa23-d940-4d29-b3d5-c2bbcfb56720">

