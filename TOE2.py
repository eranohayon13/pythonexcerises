Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def getBert(string):
    #converts the stringtolowercase string and splits around the string bert.
	newline=string.lower().split("bert")
    #if length of array is smaller than 2 then returns the second to penultimate joined to a string with empty space, and [::-1] return the string in reverse order.
	if len(newline) > 2:
		return "".join(newline[1:-1])[::-1]
	else: return ""