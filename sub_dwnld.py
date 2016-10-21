'''
Subtitle downloader 1.0
Using SubDB API
Made By: Mohammad asif
Github: mohdasif2294
'''
import urllib2 #For Get requests
import os #For directory and filenames
import hashlib #to convert file name in to hash
import sys #For argument passing

def get_hash(name): #To get the file hashcode (Hexcode)
		readsize = 64 * 1024
		with open(name, 'rb') as f:
			size = os.path.getsize(name)
			data = f.read(readsize)
			f.seek(-readsize, os.SEEK_END)
			data += f.read(readsize)
		return hashlib.md5(data).hexdigest()

vid_ext=[".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp",".dat"] #File extensions

def sub_downloader(fname): # Function for downloading subtitles

	srt_name=fname
	
	for i in vid_ext:
		srt_name=srt_name.replace(i,"") #Getting file name and removing the extension
	
	if(srt_name==fname):
		print "Video extension is not there or file is not a video!\nPlease try with different file"
		exit()

	hash_code=get_hash(fname) #calling hashing function for movie hash code

	subfile=srt_name+".srt"

	if os.path.isfile(subfile):
		print "Already subtitle for the file exists!"
		exit()

	headers = { 'User-Agent' : 'SubDB/1.0 (asif/1.0; http://github.com/mohdasif2294/sub_download)' } #SubDB version and User Client as Header
	url="http://api.thesubdb.com/?action=download&hash="+hash_code+"&langauge=en" #SubDB API request for downloading english subtitle
	
	try:
		req = urllib2.Request(url,'', headers) #Urllib2 request with header
		response = urllib2.urlopen(req).read() #reading the content of response
		fd=open(subfile,'wb')
		fd.write(response) # making a srt file
		fd.close()
	except:
			print "No subtitle found!"
			exit()

def main():
	if(len(sys.argv)<2): #for argument as filename
		print "Filename missing"
		exit()
	else:
		sub_downloader(sys.argv[1]);

if __name__ == '__main__':
	main()