'''
Name: findPaths
Description: This module does the searching for the end article using a BFS.
'''

import re
from lxml import html
import requests
from sets import Set
import Queue
import WikiNode
import time 

visited = Set([]) #set of visited articles
web  = dict({})   #hashtable of visited WikiNodes

'''
Name: findPaths(current_article, end_article)
	current_article -- starting article
	end_article -- destination article
Description: Breadth first search to find the destination article 
'''
def findPaths(current_article, end_article):
	global web
	current_article = current_article.replace(' ', '_')
	end_article = end_article.replace(' ', '_')
	wiki_link_start = "http://en.wikipedia.org/wiki/" + current_article
	page=requests.get(wiki_link_start)
	tree=html.fromstring(page.text)
	links=tree.xpath('//a/@href')
	start_art_wiki = "/wiki/" + current_article		
	global visited
	visited.add(start_art_wiki)
	end_art_wiki = "/wiki/" + end_article
	if end_art_wiki in links:
		print "Found."
		return
	links_Queue = Queue.Queue()
	i=0
	j=0
	while i<10:
		print "hi"
		if (isValidLink(links[j])):
			visited.add(links[j])
			links_Queue.put(links[j])
			currentNode = WikiNode.WikiNode(start_art_wiki, links[j])
			web[links[j]] = currentNode
			i=i+1
			i=i+1
		else: 
			j=j+1
	start = WikiNode.WikiNode("-1", start_art_wiki)
	web[start_art_wiki] = start
	BFS(links_Queue, end_article)


#breadth first search
def BFS(queue_links, end_article):
	global visited
	global web
	end_article = "/wiki/" + end_article
	while not queue_links.empty():
		current_article = queue_links.get()
		print current_article + " " + end_article
		if (current_article == end_article):
			print "Found."
			return
		else:
			search_link = "http://en.wikipedia.org" + current_article
			try:
				page = requests.get(search_link)
			except requests.ConnectionError:
				continue
			tree = html.fromstring(page.text)
			links = tree.xpath('//a/@href')
			if end_article in links:
				print "Found."
				print "_______"
				printPath(end_article, current_article)
				return 
			i=0
			j=0
			while i<2:
				if (isValidLink(links[j])):
					visited.add(links[j])
					queue_links.put(links[j])
					current = WikiNode.WikiNode(current_article, links[j])
					web[links[j]] = current
					i=i+1
					j=j+1
				else: 
					j=j+1

#Function to use to get page in bad connection situations					
def getPage(search_link):
	try:
		page = requests.get(search_link)
		return page
	except requests.ConnectionError:
		time.sleep(1)
		return getPage(search_link)

#function that uses WikiNodes to print the path taken once destination article is found
def printPath(end_article, article):
	global web
	currNode = web[article]
	parent = currNode.parent
	stack = []
	stack.append(currNode)
	while (parent != "-1"):
		currNode = web[parent]
		stack.append(currNode)
		parent = currNode.parent

	while (len(stack)!=0):
		currNode = stack.pop()
		print currNode.name 
		print "  --->  "

	print end_article

#function that checks if a given link is valid
def isValidLink(link):
	global visited
	if (link in visited):
		return False
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
	bad_strings = []
	bad_strings.append("disambiguation")
	bad_strings.append("Protection_policy")
	bad_strings.append("Requests_for_page_protection")
	bad_strings.append("Template_messages")
	bad_strings.append("Editnotices")
	bad_strings.append("Wikipedia:")
	bad_strings.append("Template")
	bad_strings.append("Free_content")
	bad_strings.append("Logo_of_Wikipedia")
	bad_strings.append("Content")
	bad_strings.append("Portal")
	bad_strings.append("Talk:")
	bad_strings.append("index.php")
	for bad in bad_strings:
		if bad in link:
			return False

	return True




