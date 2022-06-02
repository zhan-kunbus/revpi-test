import struct
import pytest
import paramiko
import spur
import scp
import os
import time
import wget

class RevPiSSHClient:
    ssh_client = None
    Hostname= None
    Username= None
    Password= None
    #constructor
    def __init__(self,Hostname,Username,Password):
        self.Hostname = Hostname
        self.Username = Username
        self.Password = Password
        self.ssh_client=paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def Connect(self):
        return self.ssh_client.connect(hostname=self.Hostname, username=self.Username, password=self.Password)

    def Disconnect(self):
        self.ssh_client.close()

    def UpdatePassword(self,NewPassword):
        self.Password = NewPassword

    def getTransport(self):
        return self.ssh_client.get_transport()

    def SSHExecute(self,command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        output = stdout.read()
        return output
