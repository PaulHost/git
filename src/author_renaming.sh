#!/bin/bash
git filter-branch -f --env-filter '
WRONG_NAME='$1'
NEW_NAME='$2'
if [ "$GIT_COMMITTER_NAME" = "$WRONG_NAME" ]
then
	export GIT_COMMITTER_NAME="$NEW_NAME"
fi
if [ "$GIT_AUTHOR_NAME" = "$WRONG_NAME" ]
then
	export GIT_AUTHOR_NAME="$NEW_NAME"
fi' --tag-name-filter cat -- --branches --tags