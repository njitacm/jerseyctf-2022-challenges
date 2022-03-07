# Contributing

* Your one stop shop for contributing! 

---
## How to Contribute

### Creating a challenge
* **Be sure your flag looks like `jctf{your_text_here}`**

1. Go to Directory of category that you wish to create a challenge for 

    | Categories
    | :--
    | [crypto](../crypto)
    | [forensics](../forensics)
    | [misc](../misc)
    | [bin](../bin)
    | [web](../web)
    | [osint](../osint)

1. Run `python3 ../makeChallenge.py <ChallengeName>` and this will automatically instantiate all the standardization to make a challenge.
    - _NB: This assumes you have followed Step 1_
    * Be sure that ChallengeName is `one word` (has no space) or `encapsulated by single quotes` 
    * Feel free to add new files or folders that aren't part of the standardization process
        * _Try not to deviate, unless necessary_

1. Once you finish to **Remember to Append that Challenge to the README.md in that Category Directory based on Difficulty**

    | README.md's Categories
    | :--
    | [crypto/README.md](../crypto/README.md)
    | [forensics/README.md](../forensics/README.md)
    | [misc/README.md](../misc/README.md)
    | [bin/README.md](../bin/README.md)
    | [web/README.md](../web/README.md)
    | [osint/README.md](../osint/README.md)

---
### Creating a writeup for a challenge
* *Helping both Beginners and More Seasoned Github Users*

#### For Github Beginners
1. **Fork** github repository 
    ![](https://assets.digitalocean.com/articles/eng_python/PullRequest/GitHub_Repo.gif)
1. _**(In a terminal)**_ **Clone** forked repository and move to cloned Directory 
    * `git clone https://github.com/<your-username>/ctf-challenges.git`
    * `cd ctf-challenges`
1. **Create** and **Switch** to new branch
    * `git checkout -b <branch name>` <!--`git checkout -b` is actually based-->
    * Preferably `<branch name>` is name challenge(s) 
1. Change Directory into writeups and into challenge that you have / want to make a write-up for
    * `cd writeups/<challenge>`
1. Run `python3 ../../createWriteup.py <Name/Handle>`
    * This will create a structure that looks like this: 
    ```txt
    +--- <challenge: dir>
    |    \--- <name/handle: dir>
    |         \--- <solution: dir>
    |         +--- README.md
    ```
1. Put all custom files / scripts that helped with the answering of the problem in the `<solution>` directory. Basically anything necessary goes in solution
1. Document your method in the `README.md` file which is located in the `<challenge>/<name/handle>` directory  
1. Change Directory until you are at `ctf-challegnges/writeups`
1. Git Add Files
    * `git add .`
1. Git Commit
    * `git commit -m "<Describe edits / commit>"`
1. Git Push
    * `git push origin <branch name>`
1. With everything pushed onto Github, [follow this last tutorial](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) and you should be on your way!

---

### For More Experienced Github Frequenters 
1. Create a fork of Github repo, and 
1. Change directory into `writeups/<challenge>`, with `<challenge>` being the challenge the writeup is written for
1. Run `python3 ../../createWriteup.py <Name/Handle>`
    * This will standardized the writeups in the repository
1. Dump any scripts/file in `<solution>` directory located in `writeups/<challenge>/<Name/Handle>/<solution>` and describe Method in `writeups/<challenge>/<Name/Handle>/README.md`
1. Create a PR Request from
    * _Note_: Organizers may request edits on your PR
1. Wait and Drink Campagne during the Code Review process (if you are of the legal age) 
    * _Note_: Will probably only check if the proper steps have been taken to create the writeup


## DM / PM any of the organizers to help with the writeup process

---
## Resources
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [DigitalOcean - How to create a Pull Request](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github)
* [Github Docs - Creating a Pull Request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
* [Generate ASCII Tree Structures](https://cmatskas.com/generate-ascii-folder-structures-for-windows-with-tree/)

---
## Last Resort
Contact `Logan R#7154` or `AndersOrve#9714` on Discord if clarification or help is needed 
