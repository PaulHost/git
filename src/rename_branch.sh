#!/bin/sh
git branch -m $1
git branch -m $1 $2
git push origin :$1 $2
git push origin -u $2
