# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 07:20:12 2023

@author: ASUS
"""

word=input("enter a word to check")
if "i" in word and "u" in word:
    print("the word have a both of letters")
    replace_words=word.replace("i", "*").replace("u","*")
    print("replace_words", replace_words)
    i_indexing=[i for i in range(len(word)) if word [i]=="i"]
    u_indexing=[i for i in range(len(word)) if word [i]=="u"]
    print("the indexing of i : ",i_indexing)
    print("the indexing of u : ",u_indexing)
    
elif "i" in word:
    print("the word have i just")
    replace_i=word.replace("i","**")
    I_indexing=[i for i in range(len(word)) if word (i)=="i"]
    print("the indexing of i : ",I_indexing)
elif "u" in word:
    print("the word have u just")
    replace_u=word.replace("u","***")
    U_indexing=[i for i in range (len(word)) if word [i]=="u"]
    print("the indexing of u :", U_indexing)
else:
    print("we dont have the letters ")
    