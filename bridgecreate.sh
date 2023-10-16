#!/bin/bash


#name spaces are considered like hosts or end points in a network
echo "Create name spaces"
sudo ip netns add ohost
sudo ip netns add phost
sudo ip netns add whost
sudo ip netns add yhost
sudo ip netns add prouter
sudo ip netns add yrouter
sudo ip netns add wrouter
sudo ip netns add orouter
sudo ip netns add crouter

echo "verify the name spaces"
ip netns


#Bridges are obviously switches. 
echo "Create the bridges"

#This will create 4 bridges(switches)
sudo ip link add name pbridge type bridge
sudo ip link add name ybridge type bridge
sudo ip link add name wbridge type bridge
sudo ip link add name obridge type bridge


echo "Check"
brctl show

#Activate all of the bridges(switches)
sudo ip link set dev pbridge up
sudo ip link set dev obridge up
sudo ip link set dev ybridge up
sudo ip link set dev wbridge up

echo "build the Veths"

#What is a veth?
#Veth literally stands for Virtual Ethernet, based on logic, these are the cables that connect each device.

# Connects phost to the pbridge (1)
#Sets the veth from bridge to host
sudo ip link add phost2pbrg type veth peer name pbrg2phost
#creates the virtual cable 
sudo ip link set phost2pbrg netns phost
#Assigns the pbridge as master for the veth
sudo ip link set dev pbrg2phost master pbridge
#set the interface up
sudo ip link set dev pbrg2phost up

# Connects prouter to the pbridge (2)
sudo ip link add prout2pbrg type veth peer name pbrg2prout
sudo ip link set prout2pbrg netns prouter
sudo ip link set dev pbrg2prout master pbridge
sudo ip link set dev pbrg2prout up

# Connects yhost to the ybridge (3)
sudo ip link add yhost2ybrg type veth peer name ybrg2yhost
sudo ip link set yhost2ybrg netns yhost
sudo ip link set dev ybrg2yhost master ybridge
sudo ip link set dev ybrg2yhost up

# Connects yrouter to the ybridge (4)
sudo ip link add yrout2ybrg type veth peer name ybrg2yrout
sudo ip link set yrout2ybrg netns yrouter
sudo ip link set dev ybrg2yrout master ybridge
sudo ip link set dev ybrg2yrout up

# Connects whost to the wbridge (5)
sudo ip link add whost2wbrg type veth peer name wbrg2whost
sudo ip link set whost2wbrg netns whost
sudo ip link set dev wbrg2whost master wbridge
sudo ip link set dev wbrg2whost up

# Connects wrouter to the wbridge (6)
sudo ip link add wrout2wbrg type veth peer name wbrg2wrout
sudo ip link set wrout2wbrg netns wrouter
sudo ip link set dev wbrg2wrout master wbridge
sudo ip link set dev wbrg2wrout up

# Connects ohost to the obridge (7)
sudo ip link add ohost2obrg type veth peer name obrg2ohost
sudo ip link set ohost2obrg netns ohost
sudo ip link set dev obrg2ohost master obridge
sudo ip link set dev obrg2ohost up

# Connects orouter to the obridge (8)
sudo ip link add orout2obrg type veth peer name obrg2orout
sudo ip link set orout2obrg netns orouter
sudo ip link set dev obrg2orout master obridge
sudo ip link set dev obrg2orout up

# Connects prouter to crouter (9)
sudo ip link add crout2prout type veth peer name prout2crout
sudo ip link set crout2prout netns crouter
sudo ip link set prout2crout netns prouter

# Connects yrouter to crouter (10)
sudo ip link add crout2yrout type veth peer name yrout2crout
sudo ip link set crout2yrout netns crouter
sudo ip link set yrout2crout netns yrouter

# Connects wrouter to crouter (11)
sudo ip link add crout2wrout type veth peer name wrout2crout
sudo ip link set crout2wrout netns crouter
sudo ip link set wrout2crout netns wrouter

# Connects orouter to crouter (12)
sudo ip link add crout2orout type veth peer name orout2crout
sudo ip link set crout2orout netns crouter
sudo ip link set orout2crout netns orouter

# Connects crouter to nat
# Connects nat to crouter (13)
sudo ip link add crout2nat type veth peer name nat2crout
sudo ip link set crout2nat netns crouter

#Leave the other end of the veth DANGLE in the root namespace.

#Verification
ip link
