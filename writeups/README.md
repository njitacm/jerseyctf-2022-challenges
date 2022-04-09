# Write-ups
* This is a place that one can input their solutions to solving a challenge!

---

## To Contribute
* Check out [Contribution Guide](../.github/contributing.md)

---

## Sites / Others
<!-- Where anyone with websites will have the ctf -->
| name/handle | Description / URl 
| :--- | :--: 
|  | 

---
## Contributor write
<!-- Standardization write-up section-->
## Bin
- [bin](../bin)

| Challenge | Write-ups
| :----: | :----
| [block-game](../bin/block-game) | [writeups](block-game)
| [context-clues](../bin/context-clues) | [writeups](context-clues)
| [going_over](../bin/going_over) | [writeups](going_over)
| [kangaroo](../bin/kangaroo) | [writeups](kangaroo)                              )
| [misdirection](../bin/misdirection) | [writeups](misdirection)                  iteups]($chal)\n"; done < $category
| [patches](../bin/patches) | [writeups](patches)
| [symbolism](../bin/symbolism) | [writeups](symbolism)
| [win-bin-analysis](../bin/win-bin-analysis) | [writeups](win-bin-analysis)

### Crypto 
- [Crypto](../crypto) 

| Challenge | Write-ups
| :----: | :----
| [audio-transmission](../crypto/audio-transmission) | [writeups](audio-transmission)
| [file-zip-cracker](../crypto/file-zip-cracker) | [writeups](file-zip-cracker)   
| [hidden-in-plain-sight](../crypto/hidden-in-plain-sight) | [writeups](hidden-in-plain-sight)
| [inDEStructible](../crypto/inDEStructible) | [writeups](inDEStructible)
| [new-algorithm](../crypto/new-algorithm) | [writeups](new-algorithm)
| [salad](../crypto/salad) | [writeups](salad)
| [secret-message](../crypto/secret-message) | [writeups](secret-message)
| [would-you-wordle](../crypto/would-you-wordle) | [writeups](would-you-wordle)   
| [xoracle](../crypto/xoracle) | [writeups](xoracle)


### Forensics
- [Forensics](../forensics)

| Challenge  | Write-up
| :--: | :--
| [corrupted-file](../forensics/corrupted-file) | [writeups](corrupted-file)
| [data-backup](../forensics/data-backup) | [writeups](data-backup)
| [infected](../forensics/infected) | [writeups](infected)
| [recent-memory](../forensics/recent-memory) | [writeups](recent-memory)   
| [scavenger-hunt](../forensics/scavenger-hunt) | [writeups](scavenger-hunt)
| [speedy-at-midi](../forensics/speedy-at-midi) | [writeups](speedy-at-midi)
| [stolen-data](../forensics/stolen-data) | [writeups](stolen-data)

## Misc
- [Misc](../misc)

| Challenge | Write-ups
| :----: | :----
| [bank-clients](../misc/bank-clients) | [writeups](bank-clients)
| [check-the-shadows](../misc/check-the-shadows) | [writeups](check-the-shadows)
| [dnsmasq-ip-extract](../misc/dnsmasq-ip-extract) | [writeups](dnsmasq-ip-extract)
| [filtered-feeders](../misc/filtered-feeders) | [writeups](filtered-feeders)     
| [firewall-rules](../misc/firewall-rules) | [writeups](firewall-rules)
| [root-me](../misc/root-me) | [writeups](root-me)
| [snort-log](../misc/snort-log) | [writeups](snort-log)
| [we-will](../misc/we-will) | [writeups](we-will)


## OSINT
- [OSINT](../osint)

| Challenge | Write-ups
| :----: | :----
| [contributor](../osint/contributor) | [writeups](contributor)
| [dns-joke](../osint/dns-joke) | [writeups](dns-joke)
| [mystery](../osint/mystery) | [writeups](mystery)
| [photo-op-spot](../osint/photo-op-spot) | [writeups](photo-op-spot)
| [rarity](../osint/rarity) | [writeups](rarity)
| [sho-me-whats-wrong](../osint/sho-me-whats-wrong) | [writeups](sho-me-whats-wrong)


## Web
* [Web](../web)

| Challenge | Write-ups
| :----: | :----
| [apache-logs](../web/apache-logs) | [writeups](apache-logs)
| [buster](../web/buster) | [writeups](buster)
| [cookie-factory](../web/cookie-factory) | [writeups](cookie-factory)
| [flag-vault](../web/flag-vault) | [writeups](flag-vault)
| [heres-my-password](../web/heres-my-password) | [writeups](heres-my-password)   
| [road-not-taken](../web/road-not-taken) | [writeups](road-not-taken)
| [seigwards-secrets](../web/seigwards-secrets) | [writeups](seigwards-secrets) 


<!-- 
Works in Bash

# Get Challenge Names in Directories and outputs them to file
ls ../{CATEGORY} -l | grep '^d' | awk '{print $9}' | sed 's/.$//' > {CATEGORY}

ex. 
ls ../forensics/ -l | awk '{print $9}' | sed 's/.$//' > forensics

-----

# Get writeup format by category
category={CATEGORY}; while read -r chal; do printf "| [$chal](../$category/$chal) | [writeups]($chal)\n"; done < $category

ex.
category=bin; while read -r chal; do printf "| [$chal](../$category/$chal) | [writeups]($chal)\n"; done < $category

---

# make directory for all challenges
mkdir `cat bin crypto forensics misc osint web`

# add .keep file to all challenges
for dir in `ls -l | grep '^d' | awk '{print $9}'`; do cd $dir; touch .keep; cd ..; done

--> 