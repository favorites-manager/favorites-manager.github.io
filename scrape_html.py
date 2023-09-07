import sys, re, csv, shutil, os, webbrowser

# Assign values from input arguments
HTML = str(sys.argv[1])	# The HTML file of the TikTok liked videos page
THUMBNAILS = str(sys.argv[2])	# The directory where the thumbnails are stored
if not THUMBNAILS.endswith('/'):
	THUMBNAILS+= '/'
CURRENT_LIKED_MEDIA_FN = str(sys.argv[3])	# CSV of media you've already liked, probably liked_vids.csv
NEW_THUMBNAILS_DIR = 'new_liked'

# Create an array of all the media you've already liked
already_liked = []
with open(CURRENT_LIKED_MEDIA_FN, 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		already_liked.append(row[1])

# Extract the HTML file into a single string
lines = ''
with open(HTML, 'r') as html:
	lines = ' '.join(html.readlines())

os.makedirs(NEW_THUMBNAILS_DIR, exist_ok=True)

# Get every liked video and its corresponding thumbnail from the saved HTML file
regex = r'<a href="(https://www.tiktok.com/@.+?/video/\d+?)".+?src="[^/]+?/(.+?\.jpeg)".+?href="\1"'
firstFlag = True
with open('new_liked.csv', 'w') as f:
	writer = csv.writer(f)
	for m in re.finditer(regex, lines):
		MEDIA_URL = m.group(1)	# e.g. https://www.tiktok.com/@favorites-manager/video/3141592653589790288
		MEDIA_THUMBNAIL = m.group(2)	# e.g. o07feIsQnhmOhEKlgDbpA7AkF8RTyIGIlSejf8~tplv-photomode-zoomc.jpeg
		MEDIA_ID = MEDIA_URL.split('/')[-1]	# e.g. 3141592653589790288

		# If you haven't already tagged this piece of media, play it in the browser and tag it
		if MEDIA_ID not in already_liked:
			webbrowser.open(MEDIA_URL, 1 if firstFlag else 0)
			tags = input("Comma-Separated Tags: " if firstFlag else "Tags: ")
			firstFlag = False
			writer.writerow(['tiktok', MEDIA_ID, MEDIA_URL] + tags.split(','))
			shutil.copyfile(THUMBNAILS+MEDIA_THUMBNAIL, '{}/{}.jpg'.format(NEW_THUMBNAILS_DIR, MEDIA_ID))
