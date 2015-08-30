
domains = { "de": "Germany", "sk": "Slovakia", "hu": "Hungary"}
domains2 = { "us": "United States", "no": "Norway" }

domains.update(domains2)

print "----------------DICT------------------------------"
print domains
print "-------------------------KEYS-------------------------"
print domains.keys()
print "----------------------VALUES---------------------"
print domains.values()
print "--------------------DICT INTO LIST FOR TRAVERSAL--------------"
print domains.items()

for k,v in domains.items():
        print "%s : %s" % (k,v)

print "---SORTED--"

for k,v in sorted(domains.items()):
	print "%s : %s" % (k,v)

print "----REMOVE ITEM---"

domains.pop("de")

for k,v in sorted(domains.items()):
        print "%s : %s" % (k,v)

