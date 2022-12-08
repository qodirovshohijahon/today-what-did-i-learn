## Prep to Project Interview

**:one:AWS**
- **VPC**
    **1. Что такое VPC?**
    - it enables you to launch AWS resources into a virtual network that you've defined. 

    - this virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

    - it allows you provision a logically isolated section of the AWS Cloud where you can launch AWS    resources in a virtual network that you define
    - you have complete control over your 
      - virtual networking environment,
      - including selection of your own IP address range,
      - creation of subnets,
      - configuration of route tables 
      - network gateways.
      
    **2. Какой минимальный CIDR может быть использован для создания VPC?**
    **3. Сколько subnets можно создать в такой VPC?**
    - How many Subnets can you have per VPC? - There are **200** Subnets per VPC

    - default CIDR block of `10.0.0.0/16`

    **4. Какие есть зарезервированные IP адреса в  subnet, сколько их, для чего используются?**
  
    **5. Какие базовые средства security есть в VPC? (Security groups, NACL -  надо мочь объяснить как они работатют, специфику каждого из них)**
    - A Virtual Private Cloud: A logically isolated virtual network in the AWS cloud. You define a VPC’s IP address space from ranges you select.
    - **:one: Subnet:** 
      - A segment of a VPC’s IP address range where you can place groups of isolated resources.
    - **:two: Internet Gateway:** 
      - The Amazon VPC side of a connection to the public Internet.
    - **:three: NAT Gateway:** 
      - A highly available, managed Network Address Translation (NAT) service for your resources in a private subnet to access the Internet.
    - **:four: Virtual private gateway:** 
      - The Amazon VPC side of a VPN connection.
    - **:five: Peering Connection:**
      - A peering connection enables you to route traffic via private IP addresses between two peered VPCs.
    - **:six: VPC Endpoints:** 
      - Enables private connectivity to services hosted in AWS, from within your VPC without using an Internet Gateway, VPN, Network Address Translation (NAT) devices, or firewall proxies.
    - **:seven: Egress-only Internet Gateway:** 
      - A stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet.
    
    **5. Какие вы знаете VPC Gateways?** 
      - Internet Gateway, 
      - NAT gateway, 
      - Transit Gateway, 
      - Virtual Private Gateway, 
      - Direct Connect Gateway 
    - стоит разобраться в специфике каждого из них, для чего используется, как настраивается

