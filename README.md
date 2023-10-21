# favorites-manager.github.io
## Update TikTok list from your Favorites
1. Navigate to your TikTok profile and click "Favorites."
2. Scroll down until all your recent favorited media are loaded in the browser.
3. Save the page to your hard drive, e.g. to "~/Downloads/liked.html" with media in the "~/Downloads/liked/" directory.
4. Run `python3 scrape_html.py ~/Downloads/liked.html ~/Downloads/liked_files/ liked_vids.json` in the Terminal.
5. Tag each video as prompted, pressing Enter after each completed list of tags.
6. Once you're done, manually merge `new_liked.json` into `liked.json`.
7. Move the contents of the "new_liked" directory into the "liked" directory.
8. Commit and push.