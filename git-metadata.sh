#!/bin/bash

for f in $(git ls-files | grep .py); do \
  git log -1 --pretty=format:'%ad %ae %h ' --date=format:'%d-%b-%y %H:%M:%S' $f; echo $f; \
done | sort