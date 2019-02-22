from tkinter import *
import feedparser
import datetime
import options

def getMaxTimePassed(date):

    dif=datetime.datetime.utcnow()-date

    years=round(dif.days/365)
    months=round(dif.days/30)
    weeks=round(dif.days/7)
    hours=round(dif.seconds/3600)
    minutes=round(dif.seconds/60)

    if years > 0:
        return ("%i years ago"%(round(dif.days/365)))
    elif months > 0:
        return("%i months ago"%(round(dif.days/30)))
    elif weeks > 0:
        return("%i week ago"%(round(dif.days/7)))
    elif dif.days > 0:
        return("%i days ago"%(dif.days))
    elif hours > 0:
        return("%i hours ago"%(round(dif.seconds/3600)))
    elif minutes > 0:
        return("%i minutes ago"%(round(dif.seconds/60)))
    elif dif.seconds > 0:
        return("%i seconds ago"%(dif.seconds))

def getList():
	print("Getting your list...")	
	with open ("AnimeList.txt", "r") as myfile:
		data=myfile.readlines()
	return (data)
animeList=getList()
def onepiece():
	print("Gathering RSS news from Nyaa...")
	aL=[]
	feed = feedparser.parse(options.url)
	for l in animeList:
		for i in feed['items']:
			if (options.group in i['title'])and (options.quality in i['title']):
				if(l[:-1] in i['title']):
					i=(i['title'],i['links'][0]['href'],datetime.datetime(int(i['published_parsed'][0]), int(i['published_parsed'][1]), int(i['published_parsed'][2]), int(i['published_parsed'][3]), int(i['published_parsed'][4]), int(i['published_parsed'][5])))				
					aL.append(i)
					break
	return(aL)

def setQuality(self):
	options.quality=v.get()
	listB.delete(0, last=9)
	listBDate.delete(0, last=9)
	listB2.delete(0, last=9)
	info=onepiece()
	for i,e in enumerate(info):
		listB.insert(i, "%s" %(e[0]))
		listBDate.insert(i, "Uploaded %s" %(getMaxTimePassed(e[2])))
		listB2.insert(i, e[1])

root=Tk()

root.wm_title("Nyaa RSS Gatherer")
root.iconbitmap("Nyaa.ico")

topFrame=Frame(root)
topFrame.pack()
midFrame=Frame(root)
midFrame.pack()
botFrame=Frame(root)
botFrame.pack()


mb = Menubutton(topFrame, text='Click to see your current list', relief=RAISED)
mb.grid(row=0, column=0)
mb.menu = Menu(mb, tearoff=0)
mb['menu'] = mb.menu


for i in animeList:
	var=IntVar()
	mb.menu.add_checkbutton(label=i[:-1],variable=var)
	

optionList = ('480', '720', '1080')
v = StringVar()
v.set(optionList[optionList.index(options.quality)])
om = OptionMenu(midFrame, v, *optionList, command=setQuality)

om.pack(side="left")
	

info=onepiece()

listB=Listbox(botFrame, width=65)
listBDate=Listbox(botFrame, width=25)
listB2=Listbox(botFrame, width=41)


for i,e in enumerate(info):
	listB.insert(i, "%s" %(e[0]))
	listBDate.insert(i, "Uploaded %s" %(getMaxTimePassed(e[2])))
	listB2.insert(i, e[1])

listB.pack(side="left")
listBDate.pack(side="left")
listB2.pack(side="left")

print("Ready to go!")

root.mainloop()