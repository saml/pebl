from bs4 import BeautifulSoup

import sys
import datetime
import os

def export(src_path, output_path):
	with open(src_path, 'r') as f:
		soup = BeautifulSoup(f)
		header = soup.find_all('div', class_='post_header')[0]
		body = soup.find_all('div', class_='post_body')[0]
		post_time_str = ' '.join(header.find('span', class_="post_time").string.split())
		post_time = datetime.datetime.strptime(post_time_str, '%B %d %Y, %I:%M %p')
		title = header.find('h3').string.strip()
		embed = body.find('div', class_='p_audio_embed')
		if embed:
			href = embed.a.get('href')
			href = href[href.find('/audio/'):]
			mp3 = soup.new_tag('a', href=href)
			mp3.string = 'Download'
			embed.a.replace_with(mp3)
		print(output_path)
		with open(output_path, 'wb') as output:
			s = (u'''---
title: %s
pub_date: %s
---
%s
%s
''' % (title, post_time.isoformat(), header.prettify(), body.prettify()))
			output.write(s.encode('utf-8'))


src_dir = sys.argv[1]
output_dir = sys.argv[2]

for dir_path, dirs, files in os.walk(src_dir):
	target_dir = os.path.join(output_dir, dir_path)
	if not os.path.exists(target_dir):
		os.makedirs(target_dir)
	for file_name in files:
		if file_name.endswith('.html'):
			file_path = os.path.join(dir_path, file_name)
			output_path = os.path.join(target_dir, file_name)
			export(file_path, output_path)

#export(sys.argv[1],'')