from datetime import datetime as dt
from datetime import timedelta
import hashlib
import ipaddress
import random

#Set number of IPs should be in the answer sheet.
#Larger list will discourage the use of manual tools to accomplish the task.
num_answers = 5000

#Create files containing dnsmasq log, answer output and flag.
question_file = open("dnsmasq-ip-extract-dnsmasq.log", "w+")
answer_list = open("dnsmasq-ip-extract-answer-list.txt", "w+")
flag_out = open("dnsmasq-ip-extract-flag.txt", "w+")

#Get all IPs in the 10 private range.
print("Getting private IPs in 10.0.0.0/8 range...")
priv_addresses = [str(ip) for ip in ipaddress.IPv4Network('10.0.0.0/8').hosts()]

#Generate a random list of IP addresses in the private range.
print(f"Getting {num_answers} random IPs...")
random_ips = (random.sample(priv_addresses, num_answers))

#Internal string containing answer list, used to calculate hash later.
answer_list_internal = ""

#Generate answer list. Gets each random IP (in order), hashes the string and
#outputs a line containing each IP and hash, separated by a space.
print("Generating answer list...")
for ip in random_ips:
    ip_hash = (hashlib.sha256(ip.encode())).hexdigest()
    answer_list.write(f"{ip} {ip_hash}\n")
    answer_list_internal += (f"{ip} {ip_hash}\n")

#Set random start time for challenge logs.
seed_time = (dt.now() - timedelta(days=5))

#Strings to generate fake dnsmasq logs.
dnsmasq_string = "dnsmasq[28478]:"
query_string = "query[A] dns.google.com from"
forward_string = "forwarded dns.google.com to"
cached_string = "cached dns.google.com is"
reply_string = "reply dns.google.com is"

#Generate dnsmasq logs using randomly selected IPs above.
for i in range(len(random_ips)):
    ip = random_ips[i]
    log_type = random.randint(0,1)
    step_time = random.uniform(3, 16)
    seed_time = seed_time + timedelta(seconds=step_time)
    log_time = (seed_time.strftime("%b %d %H:%M:%S"))

    #Log entries for cached DNS records.
    if log_type == 0:
        question_file.write(f"{log_time} {dnsmasq_string} {query_string} {ip}\n")
        question_file.write(f"{log_time} {dnsmasq_string} {forward_string} {ip}\n")
        question_file.write(f"{log_time} {dnsmasq_string} {reply_string} {ip}\n")
    
    #Log entries for forwarded DNS requests.
    else:
        question_file.write(f"{log_time} {dnsmasq_string} {query_string} {ip}\n")
        question_file.write(f"{log_time} {dnsmasq_string} {cached_string} {ip}\n")
        question_file.write(f"{log_time} {dnsmasq_string} {reply_string} {ip}\n")

#Write flag to file.
flag_hash = (hashlib.sha256(answer_list_internal.encode())).hexdigest()
flag_out.write(f"jctf{{{flag_hash}}}")
