# SSH Honeypot

![Honeypot](https://img.shields.io/badge/Honeypot-SSH-blue)
![Python](https://img.shields.io/badge/Python-3.x-brightgreen)

## Overview

This Python program acts as an SSH honeypot, designed to attract and monitor SSH login attempts. It generates a simulated SSH server that records login attempts, providing insight into potential security threats and unauthorized access attempts.

## Features

- Simulated SSH server using Paramiko.
- Records login attempts to a log file.
- Thread-safe handling of multiple connection attempts.
- Easy to configure and deploy as a honeypot for SSH attacks.
- Command line argument -p to select if the IP addresses of inbound connections should be recorded.

## Prerequisites

- Python 3.x
- Paramiko library (`pip install paramiko`)

## Usage

1. Clone the repository or download the script:

   <code>git clone https://github.com/Urs4M4j0r/ssh-honeypot.git</code><br><br>

2. Install required packages:
     
     <code>pip3 install -r requirements.txt</code><br><br>
     <em>alternatively</em><br><br>
     <code>pip3 install paramiko</code>
      <br><br>
3. <b>OPTIONAL:</b> Update the port number on line 10 to whichever port you want to listen on.<br><br>
4. Run the script:
     <em>Without recording IP addresses:</em><br>
     <code>python3 IntruderBait.py</code>
   <br>
     <em>With recording IP addresses:</em><br>
      <code>python3 IntruderBait.py -p</code>
   <br>
     
   <br><br>


While running passed usernames and password will be printed. Additionally, they will be logged in the logins.txt file in format "username:password".<br>

### Example console output:<br>
##### - With -p:<br>
![image](https://github.com/Urs4M4j0r/IntruderBait/assets/46537737/c1ca34fd-a2da-4523-9c66-98edc049aae5)
<br>
##### - Without -p:<br>
![image](https://github.com/Urs4M4j0r/IntruderBait/assets/46537737/048c3635-f20e-4276-811d-a72f48878e14)



### Note: the output file logins.txt will not write duplicate username password combinations unlike the console.
