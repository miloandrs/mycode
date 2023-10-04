#!/bin/bash


echo "Adding files..."
git add *
echo "Done"
echo "Committing..."
echo "What is the message? \n>>"
read message
git commit -m $message
echo "Done"
echo "Pushing..."
git push
git status
echo "All Done!"

