stuff = ET.fromstring(input) 
lst = stuff.findall('users/user') 
print 'Usercount:',len(lst)
for item in lst: 
	print 'Name',item.find('name').text 
	print 'Id',item.find('id').text 
	print 'Attribute',item.get('x')
