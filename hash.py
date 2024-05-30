import hashlib
msg = "i move lads"
m = hashlib.md5()
m.update(msg.encode('utf-8'))
word_hash = m.hexdigest()
print(word_hash)