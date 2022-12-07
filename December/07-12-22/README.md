## Prep to Project Interview

**:one:AWS**
- **VPC**
    **1. Что такое VPC?**
    - It allows you provision a logically isolated section of the AWS Cloud where you can launch AWS    resources in a virtual network that you define
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
    - **:seven: Egress-only** 
      - Internet Gateway: A stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet.
    
    Какие вы знаете VPC Gateways? (Internet Gateway, NAT gateway, Transit Gateway, Virtual Private Gateway, Direct Connect Gateway - стоит разобраться в специфике каждого из них, для чего используется, как настраивается)
    Что такое VPC Endpoints? Какие есть? Как используются и как настраиваются? (Gateway Endpoint, Interface  Endpoint нужно достаточно хорошо понимать отличия и процесс настройки, в том числе DNS записи)
    Как дать доступ к Endpoint из on-prem? (Нужно разобраться в деталях Site-to-site VPN, Virtual Private Gateway, Route table, Endpoints, DNS resolver)
    Какие типы инстансов вы знаете? (Нужно разобраться какие основные типы инстансов есть, мочь идентифицировать их назначение по буквам)
    Что означает такое название инстанса m6ad.xlarge (нужно мочь объяснить значение каждой буквы/цифры в первой части до точки, вспомнить что есть Instance Store)
    Что такое EC2 Metadata? Как получить к ней доступ? Какие данные можно от туда прочитать? Как запретить доступ к Metadata?
    Как приложение запущенное в EC2 может получить доступ ресурсам AWS? (Нужно знать IAM role and policy, Instance profile, STS and assume role, стандартные места где могут храниться   AWS креды в Linux, в том числе возможность прочитать их из EC2 Metadata)
    Каким типом дискового хранилища является EBS? (Block storage, для сравнения S3 -  object storage)
    Какие типы EBS volumes вы знаете? (Нужно вспомнить как мимнимум gp2, gp3, io1, io2 - понимать как формируется IOPS, Throughput,  объяснить какие приимущества дают io диски, по сравнению с gp)


Linux 

что такое Load Average? (стоит освежить что это и как работает на одноядерных и многоядерных серверах, мочь объяснить суть своими словами)
Какие состояния процессов есть в Linux? (стоит освежить знания по Systemd)
Как проверить сетевую доступность между EC2 и RDS, если на  EC2 установлена минимальная сборка Linux? (Разобраться какие команды могут использоваться кроме telnet, в том числе как использовать echo)
Kubernetes

Жизненный цикл pods поднятых при помощи Deployments и StatefulSet. Что происходит если Pod фейлится? (знать нюансы и отличия в обоих случаях)
Probes - как Кубернетес отрабатывает если фейлятся те или иные пробы? (нужно знать как работают все 3 вида probes, и что делает Kubernetes в случает если probe провалена - знать отличия)
Что такое K8s Service? Как работает? Какие есть варианты?
Быть готовым к вопросам по Helm+