from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

net.setLogLevel('info')

#Switches
net.addP4Switch('s1', cli_input='s1-commands.txt')
net.setThriftPort('s1',9081)
net.addP4Switch('s2', cli_input='s2-commands.txt')
net.setThriftPort('s2',9082)
net.addP4Switch('s3', cli_input='s3-commands.txt')
net.setThriftPort('s3',9083)
net.addP4Switch('s4', cli_input='s4-commands.txt')
net.setThriftPort('s4',9084)

# Routers
# There is no p4router API in p4utils.mininetlib.network_API, 
# use a specific p4 script that implements the router functionality.
net.addP4Switch('r1', cli_input='r1-commands.txt')
net.setThriftPort('s4',9091)
net.addP4Switch('r2', cli_input='r2-commands.txt')
net.setThriftPort('s4',9092)

# P4 files
net.setP4Source('s1','basic.p4')
net.setP4Source('s2','basic.p4')
net.setP4Source('s3','basic.p4')
net.setP4Source('s4','basic.p4')

net.setP4Source('r1','router.p4')
net.setP4Source('r2','router.p4')

#Hosts
net.addHost('h1')
net.addHost('h2')
net.addHost('h3')
net.addHost('h4')
net.addHost('h5')
net.addHost('h6')

#Links
net.addLink('h1','s1', port1=1, port2=2, addr1="00:00:0a:00:01:01", addr2="00:00:00:00:01:02")
net.addLink('h2','s1', port1=1, port2=3, addr1="00:00:0a:00:01:02", addr2="00:00:00:00:01:03")
net.addLink('h3','s2', port1=1, port2=2, addr1="00:00:0a:00:02:01", addr2="00:00:00:00:02:02")

net.addLink('s1','r1', port1=1, port2=2, addr1="00:00:00:00:01:01", addr2="00:00:00:00:05:02")
net.addLink('s2','r1', port1=1, port2=3, addr1="00:00:00:00:02:01", addr2="00:00:00:00:05:03")
net.addLink('r2','r1', port1=1, port2=1, addr1="00:00:00:00:06:01", addr2="00:00:00:00:05:01")
net.addLink('s3','r2', port1=1, port2=2, addr1="00:00:00:00:03:01", addr2="00:00:00:00:06:02")
net.addLink('s4','r2', port1=1, port2=3, addr1="00:00:00:00:04:01", addr2="00:00:00:00:06:03")

net.addLink('h4','s3', port1=1, port2=2, addr1="00:00:0a:00:03:01", addr2="00:00:00:00:03:02")
net.addLink('h5','s3', port1=1, port2=3, addr1="00:00:0a:00:03:02", addr2="00:00:00:00:03:03")
net.addLink('h6','s4', port1=1, port2=2, addr1="00:00:0a:00:04:01", addr2="00:00:00:00:04:02")

# Links parameters
net.setBw('s1','h1', 20) # Mbps
net.setDelay('s1','h1', 10) # ms
net.setBw('s1','h2', 20)
net.setDelay('s1','h2', 3)
net.setBw('s2','h3', 20)
net.setDelay('s2','h3', 10)

net.setBw('s1','r1', 10)
net.setDelay('s1','r1', 3)
net.setBw('s2','r1', 10)
net.setDelay('s2','r1', 3)

net.setBw('r1','r2', 1000)
net.setDelay('r1','r2', 5)

net.setBw('r2','s3', 10)
net.setDelay('r2','s3', 3)
net.setBw('r2','s4', 20)
net.setDelay('r2','s4', 10)

net.setBw('s3','h4', 20)
net.setDelay('s3','h4', 3)
net.setBw('s3','h5', 20)
net.setDelay('s3','h5', 3)
net.setBw('s4','h6', 20)
net.setDelay('s4','h6', 3)

# IPs for hosts
net.setIntfIp('h1','s1','10.0.1.10/24')
net.setIntfIp('h2','s1','10.0.1.20/24')
net.setIntfIp('h3','s2','10.0.2.10/24')
net.setIntfIp('h4','s3','10.0.3.10/24')
net.setIntfIp('h5','s3','10.0.3.20/24')
net.setIntfIp('h6','s4','10.0.4.10/24')
# IPs for switch
net.setIntfIp('s1','h1','10.0.1.2/24') # port 2 = s1-eth2
net.setIntfIp('s1','h1','10.0.1.3/24') # port 3 = s1-eth3
net.setIntfIp('s1','r1','10.0.1.1/24') # port 1 = s1-eth1

net.setIntfIp('s2','h3','10.0.2.2/24')
net.setIntfIp('s2','r1','10.0.2.1/24')

net.setIntfIp('s3','h4','10.0.3.2/24')
net.setIntfIp('s3','h5','10.0.3.3/24')
net.setIntfIp('s3','r2','10.0.3.1/24')

net.setIntfIp('s4','h6','10.0.4.2/24')
net.setIntfIp('s4','r2','10.0.4.1/24')
# IPs for routers
net.setIntfIp('r1','s1','10.0.1.5/24')
net.setIntfIp('r1','s2','10.0.2.5/24')
net.setIntfIp('r2','s3','10.0.3.5/24')
net.setIntfIp('r2','s4','10.0.4.5/24')
net.setIntfIp('r1','r2','192.168.1.1/24')
net.setIntfIp('r2','r1','192.168.1.2/24')


net.setDefaultRoute('h1', '10.0.1.5')
net.setDefaultRoute('h2', '10.0.1.5')
net.setDefaultRoute('h3', '10.0.2.5')
net.setDefaultRoute('h4', '10.0.3.5')
net.setDefaultRoute('h5', '10.0.3.5')
net.setDefaultRoute('h6', '10.0.4.5')

#net.mixed()
net.enablePcapDumpAll()
#net.enableLogAll()

net.enableCli()

#net.addTaskFile('tasks.txt')
net.startNetwork()