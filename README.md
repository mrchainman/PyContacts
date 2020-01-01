# Contacts
A short script for adding and querying contacts in a folder in vcf format.

contacts_query.py is used to search contacts, just insert the name and press CTRL+g.
In the resulting menu the contact can be choosen and it is possible to copy the name, number or email to the clipboard.

contacts_add.py expects an email as argument, but will prompt for it if none is given.
The default name of the vcf file will be Name.vcf, where Name is the contactname

### TODO
* Cleanup regular expression, to allow functioning for different vcf features (for instance there is a problem when the vcf has the phonenumber type given)
* Change CTRL+g to enter

### Contributing
Please commit all changes and contributions to the development branch

