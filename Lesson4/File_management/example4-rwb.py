f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
#16
f.seek(5)      # Go to the 6th byte in the file
#5
f.read(1)
#b'5'
f.seek(-3, 2)  # Go to the 3rd byte before the end
#13
f.read(1)
#b'd'