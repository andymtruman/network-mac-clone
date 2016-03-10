#	Created by Andrew Truman
#	Available at https://github.com/andymtruman/network-mac-clone.git under the GNU public Licence


#	Thanks to http://coderstalk.blogspot.co.uk/2010/02/create-network-interfaces-list-using.html for network interface code

import nmap # import python-nmap, available at http://xael.org/pages/python-nmap-en.html. My thanks to Alexandre Norman for his fantastic work.
import netifaces # import netifaces, available at https://bitbucket.org/al45tair/netifaces. My thanks to Alastair Houghton for his fantastic work.
import subprocess

nm = nmap.PortScanner() 
hostList = list() # List to store host information
macList = list() # List to store mac information


ifaces = netifaces.interfaces()

nc = 0
for ni in ifaces:
	print (nc, " ", ni) # prints content of list
	nc = nc+1
	
netSelect = raw_input("Which interface would you like to use? Please select a number: ")

netSelect = int(netSelect) # converts string to int ready for selection of array
netlist = str(ifaces[netSelect]) # takes selection and puts it in a string
netList = netlist.split() # splits string

print (netList)

print ('--------------------------')
varRange = raw_input("Please enter IP Range ""Example 192.168.0.1/24"": ") # insert range for nmap scan
print ('--------------------------')

print ('Scanning... ', varRange)

nm.scan(hosts=(varRange), arguments='-O') # Actual Scan command

for h in nm.all_hosts(): # Starts Loop of all hosts in Ip range
	if 'mac' in nm[h]['addresses']: # if mac address is available
		hostList.append (nm[h]['addresses']) # add it to list

print ('--------------------------')		
print ('Select a Mac Address Below')	
print ('--------------------------')

i = 0 # starts list count

for p in hostList:
	print (i, " ", p) # prints content of list
	i = i+1 # goes to next item in list

print ('--------------------------')
varSelect = raw_input("Which would you like to use? Please select a number: ")
print ('--------------------------')

varSelect = int(varSelect) # converts string to int ready for selection of array
splitlist = str(hostList[varSelect]) # takes selection and puts it in a string
macList = splitlist.split() # splits string
netList = str(netList) # converts to string
netList = netList[2:-2] # takes useless characters off the end
macList = str(macList[1])# takes useless characters off the end
macList = macList[1:-2]# takes useless characters off the end

print (netList) # Shows what interface is being used
print (macList) # shows what mac is being used

ifconfigdown = list() # Creates list for input into subprocess
ifconfigdown = ['ifconfig', netList, 'down'] # populates list

ifconfigmacswitch = list() # Creates list for input into subprocess
ifconfigmacswitch = ['ifconfig', netList, 'hw', 'ether', macList] # populates list


ifconfigup = list() # Creates list for input into subprocess
ifconfigup = ['ifconfig', netList, 'up'] # populates list

s.subprocess.call(ifconfigdown) # Turns iface off
s.subprocess.call(ifconfigmacswitch) # Changes MAC
s.subprocess.call(ifconfigup) # Turns iface on

s.kill # just in case im a bad coder, kills subprocess

print ('--------------------------')
print ('Closing...')


