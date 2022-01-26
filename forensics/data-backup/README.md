# data-backup

## Challenge Text
* The backup of our data was somehow corrupted.  Recover the data and be rewarded with a flag.

## Hint
* Try a tool a surgeon might use.

## Solution

* Carve files from corrupted zip
```
foremost -i data-backup -o recover
```

* Fix broken zip
```
cd recover/zip
```

```
zip -FF 00001490.zip --out fixed.zip
```

* Flag is in the PDF file flag.pdf
* Flag: `jctf{fun_w17h_m461c_by735}`

## Credit
* Developed by [Rob](https://github.com/njccicrob)
