import bcrypt

password = "husnain"
passwordBytes = password.encode("utf-8")
hash = bcrypt.hashpw(passwordBytes,bcrypt.gensalt())
userpassword = "husnai"
userpasswordBytes = userpassword.encode("utf-8")
print(bcrypt.checkpw(userpasswordBytes,hash))