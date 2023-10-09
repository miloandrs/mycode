#!/bin/bash


echo "Adding files..."
git add *
echo "Done"
echo "**************************"
echo "Committing..."
echo "What is the message? \n>>"
read message
git commit -m "$message"
echo "Done"
echo "**************************"
echo "Pushing..."
git push
echo "Done"
echo "**************************"
git status
echo "All Done!"
