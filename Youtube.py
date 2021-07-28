from pafy import new
import os
os.system('figlet Salah')
url = input ( ' enter you link here : ')
video = new ( url ) 
while(True):
	print('''
	[1] info for video 
	[2] download this video
	[3] exit from app ''')
	
	options=input("Select : ")
	
	if options == "1":
		print('Title video : ',video.title)
		print('Like video : ',video.likes)
		print('Rating video : ',video.rating)
		print('Dislike video : ',video.dislikes)
		print('ViewCount video : ',video.viewcount)
		print('Author video : ',video.author)
		print('Length video : ',video.length)
		print('Duration video : ',video.duration)
		#print('Description video : ',video.description)
	elif options == "2":
		stream = video.streams 
		for i in stream : 
			print ( i )
			if i =="normal:mp4@640x360":
				print("144")
			select=int(input("select streams video : "))
		stream [ select ] .download()
	elif options == "3":
		print("GoodBye ^-^")
		break
