**Что такое EC2 Metadata? Как получить к ней доступ? Какие данные можно от туда прочитать? Как запретить доступ к Metadata**

- metadata is “data that provides information about other data” (Wikipedia). 

- in AWS, **Instance Metadata Service** (IMDS) provides `data about your instance that you can use to configure or manage the running instance. Instance metadata is divided into categories, for example, host name, events, and security groups`.

- every instance has access to its own MDS using any HTTP client request, such as, **curl** command from the instance to `http://169.254.169.254/latest/meta-data`

- contains data such as instance ID, public address, AMI ID, user data, and much more.

- the instance metadata is divided into categories, such as host name, events, and security groups.

- make a request to `http://169.254.169.254/latest/` without passing any additional data this time.

```bash
curl --write-out "\n" --request GET "http://169.254.169.254/latest/meta-data/ami-id" --header "X-aws-ec2-metadata-token: $TOKEN

curl --write-out "\n" --request GET "http://169.254.169.254/latest/" --header "X-aws-ec2-metadata-token: $TOKEN"
```
- you can also use instance metadata to access user data that you specified when launching your instance.
    - for example, you can specify parameters for configuring your instance, or include a simple script. 

- you can build generic AMIs and use user data to modify the configuration files supplied at launch time.
  - for example, if you run web servers for various small businesses, they can all use the same generic AMI and retrieve their content from the Amazon S3 bucket that you specify in the user data at launch. 

- to add a new customer at any time, create a bucket for the customer, add their content, and launch your AMI with the unique bucket name provided to your code in the user data. 

- if you launch more than one instance at the same time, the user data is available to all instances in that reservation. 

- each instance that is part of the same reservation has a unique ami-launch-index number, allowing you to write code that controls what to do. 