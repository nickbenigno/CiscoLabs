# NetworkDeviceAccessControlAndInfrastructureSecuritySummary

## SSH on ALL Devices 
- In this secion of the lab we enabled SSH. This was done by creating a domain name and then creating an rsa key. Then I had to enable ssh on the vty lines. 
- Some of the challanges included compatability issues between linux, the switches and the routers. I had to look up how to change the algorithm type on Linux to support legacy mac algorithms like sha-1. As of right now, I still dont think the swtiches can ssh with the router becuase I am unable to allow legacy to the routers in the lab 

## Creating LOCAL users 
- In this secion of the lab I created LOCAL users on all swtiches, and creating three local users on swtich 1 with levels of access. 
- The challange here was to figure out how to not get locked out of the swtich. I also had to figure out what commands I can give to Operator and Learner that would allow them to use show commands without changing much. 

## AAA
- In this section I configured TACACs on all devices using https://tacacsgui.com/ connected locally. 
- Some of the challange was figuring out how I can allow local users to login when the vlan interface is not up. Using `if authenticated` on certain commands was big here becuase it would take some time for the interfaces to come up and allow for connectivity to the TACACS server. 
- Another bit of challange was figuring out my TACACS deployment, how to configure it and if I should run in on a already made Ubuntu server or out of a .oba file. The OVA file was way easier. 
- I used my SOHO router to route the TACACs traffic between my lab and the server. I had to create a static route for this to work. 
- At one point I had to use debugs to figure out why there is no connectivity, using `show tacacs public` also helped and I got to understand the fact that traffic can be sent to the TACACs server but there may be not traffic coming back. This caused the sockets to close becuase there is no connection ofc. 
- There was also this bug in my TACACS server configuraiton where a backspace character caused the deamon to stop working. 

## ZBFW 
- In this lab I set out to configure ZBFW on the router so that only certain traffic would be permitted between zones. I was unable to block traffic to www.youtube.com since this is as url and the ACLS I had were unable to block every ip dns gave back. I would Like to in the future explore URL filtering, but for now I just blocked all web traffic in the security zone which worked when I ran wget. 
- This part was the most difficult becuase at first I did not undserstand how the zone pair worked. So in ZBFW only the states that you define are permitted, so if you permitt a tcp connection from inside to outside, it would allow that, but if you dont configure the other way around for when you need connections source for the outside, you intial zone pair from inside to outside will not work. To fix this I created a zone pair from outside to inside to allow these connsection sourced outside. 
- Figuring out the ACLs to use was also a difficulty I had. I had to uderstand what traffic was source and destined with what protocol and protocol number. Running packet captures helped me with this. 
- DHCP was also very difficult to configure. I think I was either using the wrong ACLs or I did not specify any polices for DHCP to be source from the outside. A better look at the DHCP process is needed. 


## Create COPP 
- For this secion of the lab I created COPP polocies to drop Offensive ICMP Traffic. I utilized the ACL for ICMP in the ZBFW configuration and that seemed to work just fine. I was able to test this by running ICMP traffic with large packet sizes. This was blocked due to my policy and can be notice when running the show command `show policy-map control-plane input`

## Harden all Devices 
- In this secion I hardend all the devices in the topology. 
- I disabled things like proxy arp and LLDP CDP 
- This was the easiest becuase it was a checklist pretty much
- In the future I would like to find more ways to harden devices and see if I can test them. 



