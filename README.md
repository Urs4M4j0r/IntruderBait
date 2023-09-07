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

## Prerequisites

- Python 3.x
- Paramiko library (`pip install paramiko`)

## Usage

1. Clone the repository or download the script:

   <code>git clone https://github.com/Urs4M4j0r/ssh-honeypot.git</code>

2. Install required packages:
     
     <code>pip3 install -r requirements.txt</code><br><br>
     <em>alternatively</em><br><br>
     <code>pip3 install paramiko</code>

3. <b>OPTIONAL:</b> Update the port number on line 10 to whichever port you want to listen on.

4. Run the script:
     python3 IntruderBait.py


While running passed usernames and password will be printed. Additionally, they will be logged in the logins.txt file in format "username:password".

   
