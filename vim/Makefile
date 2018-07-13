SHELL := /bin/bash
.PHONY: clean help
.DEFAULT_GOAL := help
VIM_CFG=.vim_bwe_cfg

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
if match:
	target, help = match.groups()
	print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


install: ## installs vim from repo on local machine
	touch $$HOME/$(VIM_CFG)
	if [[ -f $$HOME/.vimrc ]];then \
		mv $$HOME/.vimrc $$HOME/.vimrc_old; \
		mv $$HOME/.vim $$HOME/.vim_old; \
	fi
	ln -fs $$(pwd)/.vim $$HOME/.vim
	ln -fs $$(pwd)/.vimrc $$HOME/.vimrc


uninstall: ## uninstalls vim from repo
	if [[ -f $$HOME/$(VIM_CFG) ]];then \
		echo "Found installation. Removing..."; \
		rm -rf $$HOME/$(VIM_CFG); \
		rm $$HOME/.vim; \
		rm $$HOME/.vimrc; \
		mv $$HOME/.vim_old $$HOME/.vim; \
		mv $$HOME/.vimrc_old $$HOME/.vimrc; \
	fi 
