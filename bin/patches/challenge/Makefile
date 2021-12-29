SHELL=/bin/bash

all = compile

compile:
	@gcc -o patches patches.c

dump: compile
	@touch dump.txt
# Get the .rodata section from Executable
	@objdump -s -j .rodata patches >> dump.txt
	@printf "\n" >> dump.txt
# Get Intel Assembly Syntax on the main function
	@objdump -M intel -d patches | awk -v RS= '/^[[:xdigit:]]+ <main>/' >> dump.txt
	@printf "\n" >> dump.txt
	@objdump -M intel -d patches | awk -v RS= '/^[[:xdigit:]]+ <a>/' >> dump.txt
	@printf "\n" >> dump.txt
	@objdump -M intel -d patches | awk -v RS= '/^[[:xdigit:]]+ <b>/' >> dump.txt
# Show output
	@cat dump.txt

clean:
ifneq (,$(wildcard ./a.out))
	@rm ./a.out
endif
ifneq (,$(wildcard ./patches))
	@rm ./patches
endif
ifneq (,$(wildcard ./dump.txt))
	@rm dump.txt
endif