#! /bin/bash

if [ $# != 2 ];
then
  echo "Usage: $0 <source directory> <destination directory>"
  exit 1
fi

src=$1
dst=$2

if [ ! -d "$src" ] && [ ! -d "~/{$src}" ];
then
    echo "Error: Directory $src does not exists."
    exit 1
fi

if [ ! -d "$dst" ] && [ ! -d "~/{$dst}" ];
then
    echo "Error: Directory $dst does not exists."
    exit 1
fi

for f in $src/*
do
  mv $f "$dst"
  echo "Moving $f to $dst..."
done
