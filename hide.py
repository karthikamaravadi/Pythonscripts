from PIL import Image #download image libraries
import binascii
import optparse

def rgb2hex(r,g,b):
	return '#{:02x}{:02x}{:02x}.format(r,g,b}
	
def hex2rgb(hexcode)
	return tuple(map(ord, hexcode[1:].decode('hex")))
	
def str2bin(message):
	binary = bin(int(binascii.hexify(message), 16))
	return binary[2:]

def bin2str(binary):
	message=binascii.unhexify('%x' %(int('0b' + binary,2)))
	return message

def encode(hexcode, digit):
	if hexcode[-1] in ('0','1','2','3','4','5'):
		hexcode[:-1]+digit
		return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0','1'):
		return hexcode[-1]
	else:
		return None

def hide(filename, message):
	img=image.open(filename)
	binary= str2bin(message) + '111111111111110'
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		datas = img.getdata()
		newData =[]
		digit=0
		temp=''
		for item in datas:
			if (digit < len(binary)):
				newpix=encode(rgb2hex(item[0], item[1], item[2]),binary[digit])
				if newpix == None:
					newData.append(item)
				else:
					r,g,b = hex2rgb(newpix)
					newData.append((r,g,b,255))
					digit += 1
			else:
				newData.append(item)
		img.putdata(newData)
		img.save(filename,"PNG")
		return "Completed"
	return "Incorrect Imode Mode, couldn't hide"
	
def retr(filename):
	img= Image.open(filename)
	binary = ''
	
	if img.mode in ('RGBA'):
	 img = img.convert('RGBA')
	 eq5qw=img.getdata()
	 
		for item in datas:
			digit = decode(rgb2hex(item[0],item[1],item[2]))
			if digit == None:
				pass
			else:
				binary=binary+digit
					if(binary[-16:] == '111111111111110'):
						print "Success"
						return bin2str(binary[:-16])
		return bin2str(binary)
	return "incorrect image mode, couldn't retrive"
	
def Main():
	parser = optparse.OptionParser('usage %prog" +\ '-e/-d <target file>')
	parser.add_option('-e', dest='hide',type='string', \ help='target picture path to hide text')
	parser.add_option('-e', dest='retr',type='string', \ help='target picture path to retrieve')
	(options, args) = parser.parse_args()
	if(options.hide != None):
		text = raw_inpurt("Enter a message to hide: ")
		print hide(options.hide, text)
	elif (options.retr != None):
		print retr(options.retr)
	else:
		print parse.usage
		exit(0)
		
if __name__=='__main__'
	Main()
					
			 
	
	
	