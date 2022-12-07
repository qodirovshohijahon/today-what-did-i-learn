### AWS Organizations 

- is an **account management service** that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. 
- includes account management and consolidated billing capabilities that enable you to better meet 
  - the budgetary,
  - security,
  - compliance needs of your business. 
  
As **an administrator of an organization**, you can create accounts in your organization and invite existing accounts to join the organization.

**Features**
- **Consolidated Billing** - one billing account for all aws accounts
- **Organization Units** - Organizations accounts in groups
- **Service Control Policies** - a type of organization policies that you can use to manage permissions in your organization (accounts or Org Units)

**Root account** - the root user has complete access to all AWS services and resources in the AWS account
**Member account**
    - invited 
    - Created 

**Organizations Units** 
  - it can be used organizational units (OUs) to group accounts together to administer as a single unit. 
  - this greatly simplifies the management of your accounts. 
  - for example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. 
  - it can be created multiple OUs within a single organization,
  - and you can create OUs within other OUs. 
  - each OU can contain multiple accounts, and you can move accounts from one OU to another. 
  - however, OU names must be unique within a parent OU or root.