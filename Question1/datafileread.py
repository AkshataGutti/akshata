import string
print 'Template file reader:'
with open("template.txt") as f:
    data = f.read()
    print data
    
print "Data file reader:"
with open("data.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content] 
print content

print "Replaced the data"
for change in content:
    new_str = string.replace(data, 'NAME', change)
    print(new_str)