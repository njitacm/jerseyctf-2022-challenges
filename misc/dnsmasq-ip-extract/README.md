# dnsmasq-ip-extract

## Challenge Text
* Extract all **unique** IPs from `dnsmasq-ip-extract-dnsmasq.log`, hash each IP (SHA256), and write the IP + hash to a text file (IP and hash should be separated by a space, and each IP + hash entry should be on a new line).

    **NOTE:** Alphabetical characters in the hash should be lower case, as seen in example below. Otherwise, your flag will be incorrect!

* Example of text file output contents:
    ```
    10.59.78.165 a6dd519bf8c7c50df5ae519963b5cf1590a471f88343c603168645ff335b26fe
    10.244.220.245 20657ea410e8dd2dbf979a12fea35dd1b94beb6c2cac34f1d49c5824d03de5a1
    10.18.47.24 c0e481d8f55dbb7de078cdcf67ebf627dc371e969e7dbb0b93afcce104e9247e
    ```

* The flag is the SHA256 hash of the output file. Example:
    ```
    jctf{138706baa74bac72c8ee1c42eb3a7c6add2f71c0737c5044dcdd9cba7409ead6}
    ```

## Hint
* Verify that the end of your file has a new blank line.

## Solution
* Outline:
  * Open the log file.
  * For this sample dnsmasq log, the IP addresses are at the end of the log line. Extract each IP address using any method (regex, string slicing, etc.) and add it to a list. Don't add new IP addresses to the list if they already exist (deduplication).
  * Do not sort the list of IPs, they need to be in the order seen in the logs.
  * Loop through the list of unique IP addresses, and calculate the SHA256 hash of each string.
  * Create a string consisting of each IP address string and SHA256 hash of same, separated by a single space.
  * Output this string to a file, ensuring each string is on a new line.
  * Calculate the hash of the file contents once all IP address/hash string have been written to the file. Note that the way the challenge was written, the answer file contains a new line character at the end, which will influence the file hash (and ultimately the flag). I've noted this in the hint.
  * The hash of the entire output file is the flag.

* I have written two solution scripts (PowerShell and Python) which demonstrate the outline above, see these files for details:
  * [dnsmasq-ip-extract-solution.ps1](dnsmasq-ip-extract/sol/solution_scripts/dnsmasq-ip-extract-solution.ps1)
  * [dnsmasq-ip-extract-solution.py](dnsmasq-ip-extract/sol/solution_scripts/challenge_1/dnsmasq-ip-extract-solution.py)
  
* Flag: `jctf{90dc97926e09a45aa02ca3a95db387bb00ff83ccff18f4d18a3eb96b4893e8bb}`

## Additional Files
* [dnsmasq-ip-extract-challenge-generator.py](dnsmasq-ip-extract/sol/dnsmasq-ip-extract-challenge-generator.py)
  * Script to generate a brand new challenge! Outputs the following:
    * A new sample log file (dnsmasq-ip-extract-dnsmasq.log);
    * A new answer file (dnsmasq-ip-extract-answer-list.txt);
    * A file containing the new challenge flag (dnsmasq-ip-extract-flag.txt).
* [dnsmasq-ip-extract-answer-list.txt](dnsmasq-ip-extract/sol/dnsmasq-ip-extract-answer-list.txt)
  * This is the output a participant's script should generate if completed properly.
* [dnsmasq-ip-extract-flag.txt](dnsmasq-ip-extract/sol/dnsmasq-ip-extract-flag.txt)
  * Contains the challenge flag.

## Credit
* Developed by Kevin McKenzie
