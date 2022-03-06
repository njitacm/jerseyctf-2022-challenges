#Library for calculating hashes in Python.
#Participants could also import os and use their OS' native commands.
import hashlib

#Open log file for processing.
file_in = open("dnsmasq-ip-extract-dnsmasq.log", "r")

#List to store discovered IP addresses.
ip_list = []

#String containing the answer output.
answer = ""

#Populate IP list, this will deduplicate addresses and maintain the
#order presented in the logs (important for correct hash generation).
for line in file_in:
    ip = ((line.split(" "))[-1]).strip("\n")
    if ip not in ip_list:
        ip_list.append(ip)

for ip in ip_list:
    ip_hash = (hashlib.sha256(ip.encode())).hexdigest()
    answer += (f"{ip} {ip_hash}\n")

#Get hash of answer from above and generate hash.
#Participant are instructed to output the answer to a file for hashing.
answer_hash = (hashlib.sha256(answer.encode())).hexdigest()
print(f"jctf{{{answer_hash}}}")