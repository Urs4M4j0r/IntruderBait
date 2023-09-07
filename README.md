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

   ```bash
   git clone https://github.com/yourusername/ssh-honeypot.git
