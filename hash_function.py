import hashlib

def custom_hash(input_string):
    # Create a hashlib object using SHA256 algorithm
    hash_object = hashlib.sha256()
    
    # Update the hash object with the input string
    hash_object.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    hashed_value = hash_object.hexdigest()
    
    return hashed_value

# Test the custom hash function
input_str = "Hello, world!"
hashed_value = custom_hash(input_str)
print("Hashed value:", hashed_value)
