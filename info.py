from graphics import graphics

def main():
    '''
    This function will ask the user for an input file and call all
    other functions. it will also create the canvas for the infographic.
    '''
    #determines input file based on user choice
    file_name = input('Enter input file:\n')
    input_file = open(file_name, "r")
    lines = input_file.readlines()
    #read the lines
    wordlist = readlist(lines)
    countedwords = word_counts = countwords(wordlist)
    s_most_c, m_most_c, l_most_c, s_most_w,m_most_w, l_most_w  =\
    most_used(wordlist,word_counts)
    small, medium, large =\
    word_lengths(wordlist)
    cap, not_cap =\
    unique_capitalized(word_counts.keys())
    punc, not_punc = unique_punc(word_counts.keys())
    gui = graphics(650,750, 'infographic')
    #the implementation of small, medium, and large characters
    #and the number of times they occur
    variable=\
    str(s_most_w)+' ('+str(s_most_c)+'x) '\
    +str(m_most_w)+' ('+str(m_most_c)+'x) '\
    +str(l_most_w)+' ('+str(l_most_c)+'x)'
    graphic(gui, file_name, word_counts,\
    small, medium, large,cap, not_cap,punc,not_punc, variable)

def readlist(lines):
    '''
    This function will read all of the lines and words of
    the text file and split them up and remove the extra space.
    '''
    wordlist = []

    for line in lines:
        words = line.rstrip().split()
        for word in words:
            wordlist.append(word)
    return wordlist

def countwords(wordlist):
    '''
    This function will count all the words in the text file.
    '''
    word_counts = {}

    for word in wordlist:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    return word_counts

def most_used(wordlist,word_counts):
    '''
    This function will determine most used words in file.
    s,m,l are all diffrent sets, made in order to decipher
    between small, medium, and large words.
    '''
    s ={}
    m={}
    l={}

    #getting all of the counts
    for word in wordlist:
        word=word.strip('\n')
        if len(word)<=4:
            if word not in s:
                s[word]=0
            s[word]+=1

        elif len(word)<=7:
            if word not in m:
                m[word]=0
            m[word]+=1
        else :
            if word not in l:
                l[word]=0
            l[word]+=1

    s_most_c=0
    s_most=''
    m_most_c=0
    m_most=''
    l_most_c=0
    l_most=''

    #loop through dictionary, which one appeared the most
    for key, value in word_counts.items():
        if value>s_most_c and key in s:
            s_most_c=value
            s_most_w=key
        elif value>m_most_c and key in m:
            m_most_c=value
            m_most_w=key
        elif value>l_most_c and key in l:
            l_most_c=value
            l_most_w=key
    return s_most_c, m_most_c, l_most_c,\
    s_most_w, m_most_w,l_most_w

def word_lengths(wordlist):
    '''
    This function will count the characters in each word
    to determine if it is a small, medium, or large word.
    '''
    wordlist=set(wordlist)
    small = 0
    medium = 0
    large = 0

    for word in wordlist:
        if len(word) <= 4:
            small += 1
        elif len(word) <= 7:
            medium += 1
        else:
            large += 1
    return small, medium, large

def unique_capitalized(unique_words):
    '''
    Determines what words are capitalized and which are not.
    '''
    cap = 0
    not_cap = 0

    for word in unique_words:
        if word[0].isupper():
            cap += 1
        else:
            not_cap += 1
    return cap, not_cap

def unique_punc(unique_words):
    '''
    Determines if a word has punctuation or not.
    '''
    unique_words=set(unique_words)
    punc = 0
    not_punc = 0
    punc_chars = '!,.?'
    for word in unique_words:
        if word[len(word) - 1] in punc_chars:
            punc += 1
        else:
            not_punc += 1
    return punc, not_punc
def graphic(gui, file_name, word_counts, small, medium, large,\
cap, not_cap,punc, not_punc, variable):
    '''
    Draws the entire canvas of words and bar graphs that calcualtes how many
    unique words there are.
    f=characters of the words counted, this can be divided
    in order to determine measurement of the blocks
    '''
    #calulations behind the coordinates of the blocks
    f = len(word_counts.keys())
    d = (450/f) * small
    d1 = (450/f) * medium
    d2 = (450/f) * large
    c = (450/f) * cap
    c1 = (450/f) * not_cap
    p = (450/f) * punc
    p1 = (450/f) * not_punc
    #build of graphics
    gui.rectangle(-100,-100,1000,1000, 'gray26')
    gui.text(40, 50, file_name, 'cyan', 30)
    gui.text(40, 100, 'Total Unique Words: '+ str(len(word_counts.keys())), 'white', 30)
    gui.text(40, 150, 'Most used words (s/m/l): ', 'white', 20)
    gui.text(275, 150,variable,'cyan', 20)
    gui.text(40, 200, 'Word lengths', 'white', 25)
    gui.text(235, 200, 'Cap/Non-Cap', 'white', 25)
    gui.text(425, 200, 'Punct/Non-Punct', 'white', 25)
    #word length blocks(small, medium, large words)
    gui.rectangle(40, 250, 180, d,'dodger blue',)
    gui.rectangle(40, 250 + d, 180, d1, 'forest green')
    gui.rectangle(40, 250 + d1+d , 180, d2, 'dodger blue')
    #word length text
    gui.text(45, 255, 'small words', 'white', 11)
    gui.text(45, 255+d, 'medium words', 'white', 11)
    gui.text(45, 255+d1+d, 'large words', 'white', 11)
    #Capitalization blocks(Capitilized or Not)
    gui.rectangle(235, 250, 180, c, 'dodger blue')
    gui.rectangle(235, 250+c, 180, c1, 'forest green')
    #Capitalization text
    gui.text(240, 255, 'Capitalized', 'white', 11)
    gui.text(240, 255+c, 'Non Capitalized', 'white', 11)
    #punctiated/non blocks
    gui.rectangle(425, 250, 180, p, 'dodger blue')
    gui.rectangle(425, 250+p, 180, p1, 'forest green')
    #punctiated/non text
    if p>0:
        gui.text(430, 255, 'Punctuated', 'white', 11)
    gui.text(430, 255+p, 'Non Punctuated', 'white', 11)

main()
