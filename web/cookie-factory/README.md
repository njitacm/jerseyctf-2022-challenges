# Granny's Cookie Factory

## Challenge Text
* Here at Granny's Old-Fashioned Home-Baked Cookie Factory, we pride ourselves on our cookies AND security being the best in the business.  Start here: https://jerseyctf-cookie-factory.chals.io/

## Hint
* None, this is a hard challenge

## Solution
* Recognize that the `user` cookie is a JWT
* Decode it to see that the data has the structure `{"username": ...}`
* On the dashboard page, read the attached CVE to learn the the vulnerability is a user-controlled `alg` parameter
* Realize that the header and data are Base64 encoded
* Set the algorithm to `"none"` and Base64-encode the header section
* Set the username to `"admin"` and Base64-encode the data section
* Leave the signature section blank
* Flag: `jctf{GEEZ_WHAT_A_TOUGH_COOKIE}`

## Credit
* Developed by Edward
