def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = input_string.replace(" ", "")
	reverse_string = input_string[::-1].replace(" ", "")
	if new_string.lower() == reverse_string.lower():
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True