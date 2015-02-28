#Name: findPaths
#Description: This module will check each Path of the Wikipedia tree to find a path to the desired article
import re
from lxml import html
import requests
import Queue

def findPaths(current_article, end_article):
	current_article.replace(' ', '_')
	end_article.replace(' ', '_')
	wiki_link_start = "http://en.wikipedia.org/wiki/" + current_article
	page=requests.get(wiki_link_start)
	tree=html.fromstring(page.text)
	links=tree.xpath('//a/@href')
	fid=open('result', 'w+')
	for i in range(0, len(links)):
		if (isValidLink(links[i])):
			fid.write(links[i] + '\n')
	fid.close()
	links_Queue = Queue.Queue()
	for i in range(0, len(links)):
		links_Queue.put(links[i])
	BFS(links_Queue, end_article)

def BFS(queue_links, end_article):
	end_article = "/wiki/" + end_article
	print end_article
	while not queue_links.empty():
		current_article = queue_links.get()
		print current_article
		if (current_article == end_article):
			print "Found"
			return
		else:
			#construct http:// string from current link
			search_link = "http://en.wikipedia.org" + current_article
			page = requests.get(search_link)
			tree = html.fromstring(page.text)
			links = tree.xpath('//a/@href')
			for i in range(0, len(links)):
				if (isValidLink(links[i])):
					queue_links.put(links[i])


	'''
	for i in range(0, len(links)):
		current_link = links[i]
		print current_link
		if (isValidLink(current_link)):
			if (current_link[6:] == end_article):
				print current_link[6:]
				return 1
	fid.close()
	for i in range(0,len(links)):
		current_link = links[i]
		if (isValidLink(current_link)):
			found = findPaths(current_link,end_article)
			if (found == 1):
				print current_link[6:]
				return 1
			else:
				continue
		
		else:
			continue
	return 0
		'''
def isValidLink(link):
	if (link[0]=='#'):
		return False
	if (link[:2]=='//'):
		return False
	link_without_wiki=link[6:]
	if (link_without_wiki[:5] == 'Help:'):
		return False
	if (link_without_wiki[:5] == 'File:'):
		return False
	if (link[:5] == 'http:'):
		return False
	return True

