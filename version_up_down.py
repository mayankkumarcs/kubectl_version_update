import argparse
import json
import os
import re
import subprocess
import sys

updated_version = 'v1.21.0'

def stringify(value):
    if isinstance(value, bytes):
        stringified_value = value.decode()
    else:
        stringified_value = str(value)
    return stringified_value

def execute(cmd_string, sudo=False, env=None,
            current_working_directory=None):
    command = subprocess.run(cmd_string, capture_output=True)
    cmd_output = command.stdout.decode("utf-8")
    cmd_error = sys.stderr.buffer.write(command.stderr)
    return stringify(cmd_output), stringify(cmd_error)

def remove_current_kubectl():
    print('Removing Kubectl ')
    res, err = execute(['sudo', 'rm', '/usr/local/bin/kubectl'])
    print(res)
    print('Kubectl Removed !')

def download_kubectl(version):
    print('Downloading Kubectl '+ str(version))
    command_to_exec = 'curl -LO https://dl.k8s.io/release/'+version+'/bin/linux/amd64/kubectl'
    print(command_to_exec)
    res, err = execute(command_to_exec.split())
    print(res)

def install_kubectl():
    print('Installinhg the Kubectl Version')
    install_command = 'sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl'
    res, err = execute(install_command.split())
    print(res)

def main():
    remove_current_kubectl()
    download_kubectl(updated_version)
    install_kubectl()

if __name__ == '__main__':
    main()
