#!/bin/bash


echo "Adding files..."
git add *
sleep 3
echo "Done"
echo "Committing..."
echo "What is the message? \n>>"
read message
git commit -m "$message"
sleep 3
echo "Done"
echo "Pushing..."
git push
sleep 5
git status
sleep 3
echo "All Done!"

