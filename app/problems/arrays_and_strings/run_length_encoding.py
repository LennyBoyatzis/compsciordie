MAX_RUN_LENGTH = 9

def encode_text(substring: str) -> str:
	"""Performs run-length encoding on a string"""
	char = substring[0]
	if len(substring) > MAX_RUN_LENGTH:
		divisor, remainder = divmod(len(substring), MAX_RUN_LENGTH)
		divisor_encoding = f'{MAX_RUN_LENGTH}{char}' * divisor
		remainder_encoding = f'{remainder}{char}'
		return f'{divisor_encoding}{remainder_encoding}'
	return f'{len(substring)}{char}'
	
def runLengthEncoding(text: str) -> str:
	repeat_seq_count = 1 
	ans = ''
	
	for i in range(1, len(text)):
		prev, curr = text[i-1], text[i]
		if prev == curr:
			repeat_seq_count += 1
		else:
			ans += encode_text(text[i-repeat_seq_count:i])
			repeat_seq_count = 1 
		
		if i == len(text) - 1:
			ans += encode_text(text[i+1-repeat_seq_count:i+1])
	return ans
