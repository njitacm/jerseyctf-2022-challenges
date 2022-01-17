# sho-me-whats-wrong
* Using Shodan for OSINT

## Challenge Text
* A company located in Italy that provides affordable satellite communication services appears to have a few devices with a known vulnerability. [Shodan](https://shodan.io) is a search engine that allows users to passively search for devices connected to the Internet worldwide. Find the vulnerability and use the flag format jctf{ENTER CVE HERE}.

* IMPORTANT: Shodan’s search results are real-life hosts. This flag needs to be found using completely legal, passive reconnaissance methods to explore OSINT on Shodan. Do not use any illegal or active reconnaissance methods for this challenge.
There are a limited number of searches whether you have an account or not, so make each one count! Signing up for a free account or with a .edu email provides you additional searches. 


## Solution
* Pick key words from the challenge text to filter, specifically `satellite` and `Italy` 
* Research [Shodan search filters](https://www.shodan.io/search/filters) and different key words for a satellite: `vsat` 
* In Shodan, search `"vsat" country:it` 
* Click one of the returned hosts, and note the vulnerability CVE for the flag.
* Flag: `jctf{CVE-2018-19052)`

---

## Challenge Message 
* TO DO

## Challenge Hints
* How do you filter through an Excel spreadsheet for the information you want?
