How To Connect To Security Server On Networking Lab Computers
---------------------
- Look at the sticker on the computer tower under the table and look for your desk and pc number.
- On the racks at the end of the desks, find the section for your desk.
- Plug an Ethernet cable from your PC# port to the Sec port on the right bottom of the panel.
- Run the following commands on your computer to set up the ip and routing
    - sudo ip address add 10.12.50.101/16 dev eth0 broadcast +
        - Your IP will vary. See labIP.jpg for your IP
    - sudo ip link set dev eth0 up
    - sudo ip route add default via 10.12.0.1

Need To Know Nmap Commands:
---------------------
- nmap -A
    - Runs all scripts and checks software versions
- nmap -T(0-5)
    - Sets the run speed for the network scan. 0 lowest, 5 is highest. Generally you want to use T3 for most things, but on a closed network, feel free to use T4 or T5.
- nmap -p XX
    - Scan a port or port range
    - -p 21 Single Port
    - -p 21-30 Port Range
    - -p- Scans All Ports 
- nmap 10.12.0.0/XX
    - Scans a subnet based on the mask you set. Use [this site](https://www.adminsub.net/ipv4-subnet-calculator/10.12.0.0/16) to help calculate subnets

Need To Know Metasploit Commands:
---------------------
- msfconsole
    - Starts Metasploit in your terminal
- search "Some service"
    - Searches the Metasploit database for any exploit relating to a service or program
- use
    - use /expoit/path/something
    - Loads the module and prepares the exploit
- show options
    - Lists all the required inputs
- set XXXX
    - set rhost 0.0.0.0
    - sets the module settings to target your desired IP

Python Command For Full Shell
---------------------
python -c "import pty;pty.spawn('/bin/bash')"
