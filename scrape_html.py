import sys, re, json, shutil, os, webbrowser

# Assign values from input arguments
HTML = str(sys.argv[1])	# The HTML file of the TikTok liked videos page
THUMBNAILS = str(sys.argv[2])	# The directory where the thumbnails are stored
if not THUMBNAILS.endswith('/'):
	THUMBNAILS+= '/'
CURRENT_LIKED_MEDIA_FN = str(sys.argv[3])	# CSV of media you've already liked, probably liked_vids.csv
NEW_THUMBNAILS_DIR = 'new_liked'

# Create an array of all the media you've already liked
already_liked_ids = []
with open(CURRENT_LIKED_MEDIA_FN, 'r') as f:
	already_liked = json.load(f)
	already_liked_ids = [media['id'] for media in filter(lambda m: 'id' in m, already_liked)]

# Extract the HTML file into a single string
lines = ''
with open(HTML, 'r') as html:
	lines = ' '.join(html.readlines())

os.makedirs(NEW_THUMBNAILS_DIR, exist_ok=True)

# Get every liked video and its corresponding thumbnail from the saved HTML file
# regex = r'<a href="(https://www.tiktok.com/@[^"]+?/video/\d+?)".+?src="[^/]+?/([^/]+?\.jpeg)".+?href="\1"'
regex = r'<a href="(https://www.tiktok.com/@[^"]+?/video/\d+?)".+?src="[^/]+?/([^/]+?\.jpeg)".+?</a>'
firstFlag = True
new_liked = []
for m in re.finditer(regex, lines):
	MEDIA_URL = m.group(1)	# e.g. https://www.tiktok.com/@favorites-manager/video/3141592653589790288
	MEDIA_THUMBNAIL = m.group(2)	# e.g. o07feIsQnhmOhEKlgDbpA7AkF8RTyIGIlSejf8~tplv-photomode-zoomc.jpeg
	MEDIA_ID = MEDIA_URL.split('/')[-1]	# e.g. 3141592653589790288
	
	# If you haven't already tagged this piece of media, play it in the browser and tag it
	if MEDIA_ID not in already_liked_ids:
		webbrowser.open(MEDIA_URL, 1 if firstFlag else 0)
		tags = input("Comma-Separated Tags: " if firstFlag else "Tags: ")
		firstFlag = False
		new_liked.append({
			'platform': 'tiktok',
			'id': MEDIA_ID,
			'url': MEDIA_URL,
			'tags': tags.split(',')
		})

		with open('new_liked.json', 'w') as f:
			json.dump(new_liked, f, ensure_ascii=False, indent='\t')
		shutil.copyfile(THUMBNAILS+MEDIA_THUMBNAIL, '{}/{}.jpg'.format(NEW_THUMBNAILS_DIR, MEDIA_ID))
