# sho-me-whats-wrong

## Challenge Text
* A company that provides affordable satellite communication services appears to have devices scattered across the Internet with a known vulnerability. SNMP seems to be in-use with these devices, although the vulnerability is with another service. [Shodan](https://shodan.io) is a search engine that allows users to passively search for devices connected to the Internet worldwide. Find the vulnerability and use the flag format jctf{ENTER CVE HERE}.

* IMPORTANT: Shodan’s search results are real-life hosts. This flag needs to be found using completely legal, passive reconnaissance methods to gather OSINT on Shodan. Do not use any illegal or active reconnaissance methods for this challenge.
There are a limited number of searches whether you have an account or not, so make each one count! Signing up for a free account or with a .edu email provides you additional searches. 

## Hint
* How do you filter through an Excel spreadsheet for the information you want?
* Very-small-aperture terminal

## Solution
* Pick key words from the challenge text to filter, specifically `satellite` and `SNMP` 
* Research [Shodan search filters](https://www.shodan.io/search/filters), different Shodan key words for a satellite: `vsat`, and the SNMP UDP port: `161` 
* In Shodan, search `"vsat" port:161` 
* Click one of the returned hosts, and note the vulnerability CVE for the flag.
* Flag: `jctf{CVE-2018-19052}`

## Credit
* Developed by [Logan](https://github.com/Git-Logan)
