formatter = "%r %r %r %r" 

print formatter % (
'one', "two", "three", "four")

print formatter % (True, False, True, False)

print formatter % (formatter, formatter, formatter, formatter)

print formatter % ("i had this thing.", "that you could type up right.", "But it didn't sing.", "So i said goodnight.")

print formatter % (1, 2, 3, 4)

