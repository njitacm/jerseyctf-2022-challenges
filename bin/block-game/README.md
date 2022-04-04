# block-game

## Challenge Text
* There's mining, and there's crafting, but something seems off...

## Hint
* This doesn't look like a standalone program, I wonder if it depends on something else to run...

## Solution

Reverse engineering challenge with a module for the game Terasology

JAR files are just `.zip` files with a different extension; there are various ways to view the contents (without decompiling):

* Use the `jar` command line tool to extract it
* Rename the file and use `unzip` or a similar tool
* Use a GUI tool like 7zip
* Use Vim or Neovim to explore the archive without extracting it

Then you can also decompile it to see the source code; note that the JAR also contains assets that aren't code, so both of these steps are important.
I usually decompile JAR files by googling "java decompiler online" or something similar and clicking on one of the first results;
there are command line tools like `jadx` that work too (and are probably faster if you have them installed).
Java class files retain quite a bit of information, so the result is pretty readable.

In any case, you should be able to notice the string "terasology" in several places;
if you look this up, you'll find that it's an open source game similar to Minecraft.
The JAR file is a Terasology "module"; similar to a mod, but using an official API for extending the game.

Figuring out what's going on takes a little bit of research into how Terasology works;
at a high level, the module creates 5 types of entities and a command called `printFlag` for the in-game console.
The command sends an event to all entities of the first type with some data;
then this entity transforms it a little bit and sends it to the next one through another event,
all the way to the last one which prints the result (the flag) to the in-game console.
As long as there's at least one entity of each type in the world, this results in the flag being printed out when the command is run.
(If one entity is missing, there's no one to receive one of the events in the chain and the data doesn't make it to the end.)
There's also some other indirection to throw you off, like duplicate events being sent to entities that don't have handlers for them,
and the fact that the names of all of the classes and entities are just random words.

From here, we can get the flag either statically or dynamically:

### Static

The transformations at each stage are fairly simple, so we can just write a short script to generate the flag ourselves.
Here's a Python script:

```py
# Starting values from RedSystem.DATA
buf = [104, 65, 111, -41, 119, -19, -59, 19, 118, 102, 92, -35, 70, -92, -49, -33, 61, -74, -17, -90, -128, 31, -86, -94, 67, -55, 16, -67, 91, -113, 63, 41, 81, 49, -75, 103, 79]
# Java only supports signed bytes; we can use this trick to make sure Python's binary representation is the same as Java's
buf = [x & 0xFF for x in buf]

# BlueSystem.DATA
blue = [-70, 74, -118, -9, 37, 105, 69, -119, 103, -88, 91, 19, -58, -58, -19, -16, 100, 65, 42, 79, 27, -45, -125, -38, 119, 8, -121, -8, 67, 71, -2, 62, -34, 93, 0, -116, 54]
# Same trick as before
blue = [x & 0xFF for x in blue]

# OrangeSystem.onCrystal
for i in range(len(buf)):
    buf[i] = (~buf[i]) & 0xFF

# YellowSystem.onGracious
for i in range(len(buf)):
    buf[i] ^= 0x47

# GreenSystem.onCruel
for i in range(1, len(buf)):
    buf[i] ^= buf[i-1]

# BlueSystem.onPrecious
for i in range(len(buf)):
    buf[i] ^= blue[i]

# PurpleSystem.onGraceful
flag = bytes(buf)
print(flag)
```

This approach has the advantage that it doesn't require downloading/setting up the game, but it also requires more precise reverse engineering.

### Dynamic

You can download the game by cloning the [official Github repository](https://github.com/MovingBlocks/Terasology).
You need to have Java 11 or newer installed to run the game.
Then, in the game directory, you can run `./groovyw module recurse CoreSampleGameplay` to install the CoreSampleGameplay gameplay template
(you need at least one to create a world, since *all* of Terasology's content is implemented through modules).
Then you can copy the provided JAR file into the `modules` folder, start the game with `./gradlew jar game`,
and create a new world with `My Module` selected on the Advanced page of the world creation dialog.

When the world loads, you can press `F1` or grave to open the in-game console.
Use the `spawnPrefab` command to spawn one of each entity (`AridEntity`, `ArcticEntity`, `BleakEntity`, `CanineEntity`, and `EarlyEntity`).
Finally, you can run the `printFlag` command to get the flag.

This approach has the advantage that you don't need to do as much reverse engineering, but figuring out how to set up the game might be a bit of a hassle.

Flag: `jctf{b3Tter_th4N_tH3_0r1giN4l_a093c0}`

## Credit
* Developed by [ContronThePanda](https://github.com/PAndaContron), part of [RUSEC](https://rusec.github.io/).

