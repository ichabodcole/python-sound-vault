#!/bin/bash

# Get the most recent tag
# tag=$(git describe --tags $(git rev-list --tags --max-count=1))
tag=$(git tag --list 'v*.*.*' --sort=-v:refname | head -n 1)

# Split the tag into prefix and version parts
prefix=${tag%%v*}
version=${tag#*v}

# Split the version into major, minor, and patch
major=$(echo $version | cut -d. -f1)
minor=$(echo $version | cut -d. -f2)
patch=$(echo $version | cut -d. -f3)

# Increment the appropriate part of the version
case "$1" in
  --increment)
    case "$2" in
      major)
        major=$((major + 1))
        minor=$minor
        patch=$patch
        ;;
      minor)
        minor=$((minor + 1))
        patch=$patch
        ;;
      patch)
        patch=$((patch + 1))
        ;;
      *)
        echo "Invalid increment type. Must be 'major', 'minor', or 'patch'."
        exit 1
        ;;
    esac
    ;;
  *)
    echo "Invalid command. Use --increment 'major' | 'minor' | 'patch'"
    exit 1
    ;;
esac

# Construct the new tag
newtag="${prefix}v${major}.${minor}.${patch}"

echo "Previous tag version was $tag"

# Output the new tag
echo "Next tag version will be $newtag"

# Accept next tag version and tag the release
read -p "Tag the release with version $newtag? [y/n] " -n 1 -r
echo    # move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # If the user confirms, tag the release
    git tag -a $newtag -m "Version $newtag"
    echo "Tagged release with version $newtag"
else
    echo "Release was not tagged."
fi