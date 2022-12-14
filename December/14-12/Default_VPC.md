### Default VPC

- all new AWS accounts have a default VPC
- new EC2 instances are launched into the dafault VPC if no subnets is specified
- default VPC has Internet Connectivity and all EC2 instances inside it has public IPv4 addresses


You can have multiple VPCs in an AWS region (max 5 per region - soft limit)
Max CIDR per VPC is 5 for each CIDR
    min size is /28 (16 IP addresses)
    max size is /16 (65535 IP adesses) 


VPC is private, only the Private IPv4 ranges are allowed:
- 10.0.0.0 - 10.255.255.255 (10.0.0.0/8)
- 172.16.0.0 - 172.31.255.255 (172.16.0.0/12)
- 192.168.0.0 - 192.168.255.255 (192.168.0.0/16)


**VPC - Subnet**
- AWS reserves 5 IP addresses (first 4 & last 1) in each subnet
- These 5 IP addresses are not available for use and can't be assigned to an EC2 instance
- Example - if CIDR block 10.0.0.0/24 then reserved IP addresses are:
  - 10.0.0.0 - **Network address**
  - 10.0.0.1 - reserved by AWS for the **VPC router**
  - 10.0.0.2 - reserved by AWS for mapping to **Amazon-provided DNS**
  - 10.0.0.3 - reserved by AWS for the **future use**
  - 10.0.0.255 - **Network Broadcast Address**. AWS does not support broadcast in a VPC therefore the address is reserved


**Exam Tip**, if you need 29 IP addresses for EC2 instances:
- You **can't choose** a subnet of size `/27` 
  - (32 IP addresses, 32 - 5 = 27 < 29)
- You **need to choose** a subnet of size `/26` 
  - (64 IP addresses, 64 - 5 = 59 > 29)