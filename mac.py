
#empty list
mac1=[]
#each line is passed as an argument
def delimit(x):
  counter = 0
#each line's words are split into strings
  y=x.split()
  z=x.split()
#IN each line check if any mac is present -> if mac is present, search if it is unique -> if unique add to a list, at the end of each line return mac, IP and hostname
  for word1 in y:
#count number of ":" characters, if 5, it means it is a mac and take action(append mac1 list,  copy IP and hostname and return to the calling function(assignment.py)
    colon=word1.count(":")
    if colon==5:
#Discard the duplicate MAC entries, if a mac is found in a line, break the loop and return 'None'
      if word1 in mac1:
        break
#If it is a first time MAC address entry, append the "mac1" list
      else:
        mac1.append(word1)
# search for hostname in the same line, look for word right after mac-address.
#Identify real hostname with opening '(' and closing ')' parenthesis. If '(' and ')' characters not found in word succeding mac-address, use empty ''
        host1 = y[counter+1]
        if '(' in host1 and ')' in host1:
          host = host1
        else:
          host = ''
#Identify ip addesses. Look for three dots('.') in a word. If found  note it.
        for word2 in z:
          dot = word2.count(".")
          if dot == 3:
            ip = word2
#Return the noted mac-address, ip and hostname for a line of text. Will be returned as tuple data-structure.
            return word1,ip,host
#increment the counter to keep track of location of mac-address in the list of each line.
    else:
      counter = counter + 1
