#!/bin/bash
# originally from https://github.com/ersiner/osx-env-sync
# moved to ~/bin because reasons.
grep export $HOME/.bash_profile | while IFS=' =' read ignoreexport envvar ignorevalue; do
  launchctl setenv ${envvar} ${!envvar}
done
