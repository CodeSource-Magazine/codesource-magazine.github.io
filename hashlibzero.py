"""A easier Python module for making hashes simpler."""
import hashlib
import time
import random

class Hasher:
    """The class that hashes your text."""
    def __init__(self, text, text_format="ascii"):
        """The init function, defining what to hash"""
        self.text = text
        self.text_format = text_format
    def to_bytes(self, text):
        """Convertes a string object to a bytes-like object, returning bytes_object."""
        if isinstance(text, str):
            bytes_object = text.encode(self.text_format)
            return bytes_object
        raise ValueError('Incorrect input type for input text')
    def from_bytes(self, text):
        """Converts a bytes-like object to a string object, returning string_object."""
        if isinstance(text, bytes):
            string_object = text.decode(self.text_format)
            return string_object
        raise ValueError('Incorrect input type for input text')
    def sha256(self, text=None):
        """Converts the self.text object into a SHA256 hash in hex."""
        if text is None:
            text = self.text
        final_output = hashlib.sha256(self.to_bytes(text)).hexdigest()
        return final_output
    def sha1(self, text=None):
        """Converts the self.text object into a SHA1 hash in hex."""
        if text is None:
            text = self.text
        final_output = hashlib.sha1(self.to_bytes(text)).hexdigest()
        return final_output
    def md5(self, text=None):
        """Converts the self.text object into a MD5 hash in hex."""
        if text is None:
            text = self.text
        final_output = hashlib.md5(self.to_bytes(text)).hexdigest()
        return final_output
def main():
    """A bunch of tests."""
    hasher = Hasher("This is a test hash string")
    print("Hashing string \"This is a test hash string\" once...")
    print("SHA256:")
    print(hasher.sha256())
    print("SHA1:")
    print(hasher.sha1())
    print("MD5:")
    print(hasher.md5())
    print("Calculating speed of 10,000 SHA256 hashes...")
    start_time = time.time()
    for _ in range(10000):
        hasher.sha256(str(random.randint(0,10^10)))
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time {total_time} seconds.")
    print("Calculating SHA256 hashes/second:")
    start_time = time.time()
    now = time.time()
    hashes = 0
    while now - start_time < 1:
        hasher.sha256(str(random.randint(0,10^10)))
        hashes += 1
        now = time.time()
    print(f"Computer has {hashes} hashes/second.")
    print("Tests over.")
    
if __name__ == "__main__":
    main()
