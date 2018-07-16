#!/bin/bash

# Create temporary storage
temp=$TMPDIR$(uuidgen)
mkdir -p $temp/mount

# Download installer
curl $4 > $temp/1.dmg

# Mount installer
yes | hdiutil attach -noverify -nobrowse -mountpoint $temp/mount $temp/1.dmg

# If the dmg contains an app, unpack the app; if it's a .pkg, install the pkg silently
if ls $temp/mount/*.app 1> /dev/null 2>&1; then
  cp -r $temp/mount/*.app /Applications
elif ls $temp/mount/*.pkg 1> /dev/null 2>&1; then
  /usr/sbin/installer -package $temp/mount/*.pkg -target /
fi

# Clean up
hdiutil detach $temp/mount
rm -r $temp