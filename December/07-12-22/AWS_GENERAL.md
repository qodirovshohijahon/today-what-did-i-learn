## Prep to Project Interview

**:one:AWS**
- **General**

    **[1. Что такое VPC?](../10-12/1.%20%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20VPC%3F.md)**

    **[2. Какой минимальный CIDR может быть использован для создания VPC?](../10-12/2.%20%D0%9A%D0%B0%D0%BA%D0%BE%D0%B9%20%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20CIDR%20%D0%BC%D0%BE%D0%B6%D0%B5%D1%82%20%D0%B1%D1%8B%D1%82%D1%8C%20%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%20%D0%B4%D0%BB%D1%8F%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%20VPC.md)**
    
    **[3. Сколько subnets можно создать в такой VPC?](../10-12/3.%20%D0%A1%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20subnets%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C%20%D0%B2%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B9%20VPC.md)**
    
    **[4. Какие есть зарезервированные IP адреса в  subnet, сколько их, для чего используются?](../10-12/4.%20%D0%9A%D0%B0%D0%BA%D0%B8%D0%B5%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%B7%D0%B0%D1%80%D0%B5%D0%B7%D0%B5%D1%80%D0%B2%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20IP%20%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0%20%D0%B2%20%20subnet.md)**
    
    **[5. Какие базовые средства security есть в VPC? (Security groups, NACL -  надо мочь объяснить как они работатют, специфику каждого из них)](../10-12/5.%20%D0%9A%D0%B0%D0%BA%D0%B8%D0%B5%20%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B5%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0%20security%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%B2%20VPC.md)**
    
    **[6. Какие вы знаете VPC Gateways? (Internet Gateway, NAT gateway, Transit Gateway, Virtual Private Gateway, Direct Connect Gateway - стоит разобраться в специфике каждого из них, для чего используется, как настраивается)](../10-12/6.%20%D0%9A%D0%B0%D0%BA%D0%B8%D0%B5%20%D0%B2%D1%8B%20%D0%B7%D0%BD%D0%B0%D0%B5%D1%82%D0%B5%20VPC%20Gateways.md)**
    
    **[7. Что такое VPC Endpoints? Какие есть? Как используются и как настраиваются? (Gateway Endpoint, Interface  Endpoint нужно достаточно хорошо понимать отличия и процесс настройки, в том числе DNS записи)](../10-12/7.%20%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20VPC%20Endpoints.md)**
    
    **[8. Как дать доступ к Endpoint из on-prem? (Нужно разобраться в деталях Site-to-site VPN, Virtual Private Gateway, Route table, Endpoints, DNS resolver)](../10-12/8.%20%D0%9A%D0%B0%D0%BA%20%D0%B4%D0%B0%D1%82%D1%8C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%20%D0%BA%20Endpoint%20%D0%B8%D0%B7%20on-prem.md)**
    
    **[9. Какие типы инстансов вы знаете? (Нужно разобраться какие основные типы инстансов есть, мочь идентифицировать их назначение по буквам)](../10-12/9.%20%D0%9A%D0%B0%D0%BA%D0%B8%D0%B5%20%D1%82%D0%B8%D0%BF%D1%8B%20%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%20%D0%B2%D1%8B%20%D0%B7%D0%BD%D0%B0%D0%B5%D1%82%D0%B5.md)**
  
    **[10. Что означает такое название инстанса m6ad.xlarge (нужно мочь объяснить значение каждой буквы/цифры в первой части до точки, вспомнить что есть Instance Store)](../10-12/10.%20%D0%A7%D1%82%D0%BE%20%D0%BE%D0%B7%D0%BD%D0%B0%D1%87%D0%B0%D0%B5%D1%82%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%B8%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%81%D0%B0%20m6ad.xlarge.md)**
    
    **[11. Что такое EC2 Metadata? Как получить к ней доступ? Какие данные можно от туда прочитать? Как запретить доступ к Metadata?](../10-12/11.%20%D0%A7%D1%82%D0%BE%20%D1%82%D0%B0%D0%BA%D0%BE%D0%B5%20EC2%20Metadata.md)**

    **[12. Как приложение запущенное в EC2 может получить доступ ресурсам AWS? (Нужно знать IAM role and policy, Instance profile, STS and assume role, стандартные места где могут храниться   AWS креды в Linux, в том числе возможность прочитать их из EC2 Metadata)](../10-12/12.%20%D0%9A%D0%B0%D0%BA%20%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B7%D0%B0%D0%BF%D1%83%D1%89%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%B2%20EC2%20%D0%BC%D0%BE%D0%B6%D0%B5%D1%82%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%20%D1%80%D0%B5%D1%81%D1%83%D1%80%D1%81%D0%B0%D0%BC%20AWS.md)**

    **[13. Каким типом дискового хранилища является EBS? (Block storage, для сравнения S3 -  object storage)](../10-12/13.%20%D0%9A%D0%B0%D0%BA%D0%B8%D0%BC%20%D1%82%D0%B8%D0%BF%D0%BE%D0%BC%20%D0%B4%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D0%BB%D0%B8%D1%89%D0%B0%20%D1%8F%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F%20EBS.md)**

    **[14. Какие типы EBS volumes вы знаете? (Нужно вспомнить как мимнимум gp2, gp3, io1, io2 - понимать как формируется IOPS, Throughput,  объяснить какие приимущества дают io диски, по сравнению с gp)](../10-12/14.%20%D0%9A%D0%B0%D0%BA%D0%B8%D0%B5%20%D1%82%D0%B8%D0%BF%D1%8B%20EBS%20volumes%20%D0%B2%D1%8B%20%D0%B7%D0%BD%D0%B0%D0%B5%D1%82%D0%B5.md)**