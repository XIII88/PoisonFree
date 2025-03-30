import os, re
import base64
# @SoftQWK1XIII

NOTE = "# DECODED BY HYPER X SQUAD >>> TOP 1 \n# @decoded_softs\n\n"

EXEC_PATTERN =  r"exec\(\(_\)\(b'(.+?)'\)\)"

COMMENTS_PATTERN = r"#(.*?)\n"
# @SoftQWK1XIII


def base_decode(file_name: str, new_filename: str, user_choice: str) -> bool:
	"""Decoding files that have been encoded with base64 (1) or base32 (2) or base16 (3) and write the result to a new file"""
	try:
		if user_choice == "1":
            # @SoftQWK1XIII
			pattern = r"_\s*=\s*lambda\s*__\s*:\s*__import__\('base64'\)\.b64decode\(__\[::-1\]\);"
			special = base64.b64decode

		elif user_choice == "2":
            # @SoftQWK1XIII
			pattern = r"_\s*=\s*lambda\s*__\s*:\s*__import__\('base64'\)\.b32decode\(__\[::-1\]\);"
			special = base64.b32decode

		elif user_choice == "3":
            # @SoftQWK1XIII
			pattern = r"_\s*=\s*lambda\s*__\s*:\s*__import__\('base64'\)\.b16decode\(__\[::-1\]\);"
			special = base64.b16decode

		with open(file_name, "r", encoding = "utf-8") as f:
      		# @SoftQWK1XIII
			code = f.read() 
			
		match = re.search(pattern, code) 
			
		if not match:
            # @SoftQWK1XIII
			print("Обфускация не обнаружена.")
			return False 
			
		def decode_layer(encoded_str: str) -> str:
			"""Decoding 1 layer and return result"""
			try:
                # @SoftQWK1XIII
				padding = len(encoded_str) % 4 
				if padding:
					encoded_str += "=" * (8-padding) 
				
				decoded_str = special(encoded_str[::-1]) 
				
				return decoded_str.decode("utf-8")
		
			except Exception as e:
                # @SoftQWK1XIII
				print(f"Ошибка! {e}")
				return False
		
		while re.search(EXEC_PATTERN, code): 
			code = re.sub(EXEC_PATTERN, lambda m: decode_layer(m.group(1)), code)
   
        # @SoftQWK1XIII
		code = code.replace(f"_ = lambda __ : __import__('base64').{special.__name__}(__[::-1]);", "") 
			
		while re.search(COMMENTS_PATTERN, code):    
			code = re.sub(COMMENTS_PATTERN, "" , code)  
		
		with open(new_filename, "w", encoding = "utf-8") as f:
			f.write(NOTE + code.strip()) 
		
		return True
        # @SoftQWK1XIII
	except Exception as e:
		print(f"Произошла ошибка! {e}")
		return False
    # @SoftQWK1XIII

def menu() -> None:
    user_choice = input("Файл кидать в папку с софтом \nВыбери функцию:\n1-Base64 decode\n2-Base32 decode\n3-Base16 decode\n\n->> ")
    # @SoftQWK1XIII
    while True: 
        file_name = input("Введите название файла: ").strip()
		
        if "." in file_name and not file_name.endswith("py"): 
            print("Файл должен иметь расширение .py ")
            continue 
        # @SoftQWK1XIII
        file_name = f"{file_name}" if file_name.endswith(".py") else f"{file_name}.py" 

        if not os.path.exists(file_name):
            print(f"Файл {file_name} не найден.\n")
            # @SoftQWK1XIII
        else:
            break

    new_filename = file_name[:-3] + '_DecodedByHXSRE.py' 
    # @SoftQWK1XIIIs
    if base_decode(file_name, new_filename, user_choice): 
        print(f"Успешно декодировано! Файл - {new_filename}")
    
    else:
	    print("Деобфускация не удалась.")

if __name__ == "__main__":
    menu()
    