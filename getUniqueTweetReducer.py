#!/usr/bin/python
import sys
import itertools
data = {}
current_userId = None
userIdCountMap = {}
textWordMap = {}
originalList = []
userIdLst = []
rem = []
for line in sys.stdin:
    idText, totalCount = line.split(':::::', 1)
    originalList.append(idText+':::::'+totalCount);
    totalCount = int(totalCount)
    userId, text = idText.split('|', 1)
    if userId in userIdCountMap:
        userIdCountMap[userId].append(totalCount)
    else:
        userIdCountMap[userId] = [totalCount]
        userIdLst.append(userId)
for item in userIdLst:
    newList = userIdCountMap[item]
    (newList.sort())
    newList = newList[::-1]
    userIdCountMap[item] = newList
for items in originalList:
    idTextVal, totalReTweetsFav = items.split(':::::', 1)
    totalReTweetsFav = int(totalReTweetsFav)
    id, textVal = idTextVal.split('|', 1)
    if totalReTweetsFav in userIdCountMap[id]:
        userIdCountMap[id].remove(totalReTweetsFav)
        if textVal not in rem:
            rem.append(textVal)
            print '%s\t%s' % (idTextVal , totalReTweetsFav)





