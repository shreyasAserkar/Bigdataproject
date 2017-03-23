#!/usr/bin/python
import sys

cat1=[]
cat2=[]
cat3=[]
cat4=[]
outPut1 = {}
#set of classified data we got from paper. Based on this we will classify our own data.
l = ["1:archives,archive,books,book,list,read,bestselling,articles,cookbook,benefit,photo ,cover,picture,history,cookbook,reads,info,news,check,collection,booklist,article,peek,edition,essay,essays,guide,document,documents,readers,resource,resources","2:readinglist,school,excited,encourage,happy,love,wisdom,enjoyed,parents,favourite,readeverywhere,learning,kids,favourite,blog,http,show,lovely,exciting,movie,movies,film,films,myths,ideas,popular,think,thinking,look,oscar,oscars","3:join,celebration,libraries,opening,program,party ,creative,story,questions,today,community,art,family,summer,spring,fun,celebrate,creative,club,check,questions,story,joined,meet,meeting,participate,communities,celebrating,enjoy,thanks,thank you,ready,open,congratulations,award,publishers,congrats","4:public,librarian,visit,staff,branch,exhibit,welcome,opening,event,program,food,library,friends,park,explore,events,webinar,hosted,host,hosting,activities,exhibitions,offers,offer,workshop,librarians,music,reminder,tomorrow,campaign,tonight ,day,update,week,newsletter,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday,subscribe,alert,working,upcoming,watch"]

#this step will add each category to respective list
for line in l:
    try:
        id, l = line.split(':')
        lsit  = l.split(',')
        if id is '1':
            cat1=lsit
        if id is '2':
            cat2=lsit
        if id is '3':
            cat3=lsit
        if id is '4':
            cat4=lsit
    except:
        pass

#this section will iterate through each line and then subsection will iterate through each word
#then we are checking the category of that word and incrementing the respective counter.
#If count is max among the other counts respective category is assigned to current tweet(line) 		
for line in sys.stdin:
    #check for validity of data
	try:
        # split the line into keys
        words = line.split(':::::')
        wordsInLine = words[0].split('|')[1].split(' ')
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0

        for aword in wordsInLine:
            if aword in cat1:
                c1 = c1 +1
            if aword in cat2:
                c2 = c2 + 1
            if aword in cat3:
                c3 = c3 + 1
            if aword in cat4:
                c4 = c4 + 1
        if c1 is 0 and c2 is 0 and c3 is 0 and c4 is 0:
            c2=99
        mapOfcat = {'c1':c1,'c2':c2,'c3':c3,'c4':c4}
        if str(words[0].split('|')[2]+'|'+max(mapOfcat, key=mapOfcat.get)).strip() in outPut1:
            outPut1[str(words[0].split('|')[2] + '|' + max(mapOfcat, key=mapOfcat.get)).strip()] = outPut1[str(words[0].split('|')[2] + '|' + max(mapOfcat, key=mapOfcat.get)).strip()] + int(words[1].strip())
        else:
            outPut1[str(words[0].split('|')[2]+'|'+max(mapOfcat, key=mapOfcat.get)).strip()] = int(words[1].strip())
    except:
        pass

outPut2 = {}
for key in outPut1:
    if key.split('|')[0].strip() not in outPut2:
        outPut2[key.split('|')[0].strip()] = [key.split('|')[1].strip()+'|'+str(outPut1[key])]
    else:
        outPut2[key.split('|')[0].strip()].append(key.split('|')[1].strip()+'|'+str(outPut1[key]))



for k in outPut2:
    mx = 0;
    catg = 'c2';
    for values in outPut2[k]:

        v,CurrMx = values.split('|',1)
        if int(CurrMx) > int(mx) :
            mx = int(CurrMx)
            catg = v
    catg = catg.strip()

    if catg == 'c1':
        print '%s\t%s' % (k, 'Literature Exhibit')  # append M so that reducer can differentiate data from two tables
    if catg == 'c2':
        print '%s\t%s' % (k, 'Engaging Topics')  # append M so that reducer can differentiate data from two tables
    if catg == 'c3':
        print '%s\t%s' % (k, 'Comminity Building')
    if catg == 'c4':
        print '%s\t%s' % (k, 'Library Showcasing')
