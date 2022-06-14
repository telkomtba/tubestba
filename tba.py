import requests
import streamlit as st

from distutils.log import error
from lib2to3.pgen2 import token
from pickle import FALSE
import string
from symtable import Symbol

def LexicalAnalyzer(kata):

    input_kata = kata.lower() + '#'
    transition_table ={}


    transition_table[('q0', ' ')] = 'q0'

    transition_table[('q0','a')] = 'q1'
    transition_table[('q1','b')] = 'q2'
    transition_table[('q2','a')] = 'q3'
    transition_table[('q3','h')] = 'q33'

    transition_table[('q0','o')] = 'q4'
    transition_table[('q4','m')] = 'q5'
    transition_table[('q5','a')] = 'q6'
    transition_table[('q6','k')] = 'q33'

    
    transition_table[('q0','u')] = 'q7'
    transition_table[('q7','w')] = 'q5'
    transition_table[('q5','a')] = 'q6'
    transition_table[('q6','k')] = 'q33'

        
    transition_table[('q0','b')] = 'q21'
    transition_table[('q21','u')] = 'q22'
    transition_table[('q22','k')] = 'q16'
    transition_table[('q16','u')] = 'q33'
        
    transition_table[('q0','p')] = 'q24'
    transition_table[('q24','e')] = 'q25'
    transition_table[('q25','n')] = 'q26'
    transition_table[('q26','s')] = 'q27'
    transition_table[('q27','e')] = 'q28'
    transition_table[('q28','l')] = 'q33'
            
    transition_table[('q0','p')] = 'q24'
    transition_table[('q24','e')] = 'q25'
    transition_table[('q25','m')] = 'q29'
    transition_table[('q29','a')] = 'q30'
    transition_table[('q30','d')] = 'q31'
    transition_table[('q31','a')] = 'q32'
    transition_table[('q32','m')] = 'q33'
                
    transition_table[('q0','m')] = 'q9'
    transition_table[('q9','u')] = 'q10'
    transition_table[('q10','m')] = 'q11'
    transition_table[('q11','a')] = 'q8'
    transition_table[('q8','s')] = 'q5'
    transition_table[('q5','a')] = 'q6'
    transition_table[('q6','k')] = 'q33'
                
    transition_table[('q0','m')] = 'q9'
    transition_table[('q9','u')] = 'q10'
    transition_table[('q10','m')] = 'q11'
    transition_table[('q11','b')] = 'q12'
    transition_table[('q12','o')] = 'q13'
    transition_table[('q13','l')] = 'q14'
    transition_table[('q14','i')] = 'q33'
                    
    transition_table[('q0','m')] = 'q9'
    transition_table[('q9','u')] = 'q10'
    transition_table[('q10','m')] = 'q11'
    transition_table[('q11','b')] = 'q8'
    transition_table[('q12','a')] = 'q15'
    transition_table[('q15','c')] = 'q16'
    transition_table[('q16','u')] = 'q33'
                
    transition_table[('q0','m')] = 'q9'
    transition_table[('q9','e')] = 'q17'
    transition_table[('q17','n')] = 'q18'
    transition_table[('q18','j')] = 'q19'
    transition_table[('q19','u')] = 'q20'
    transition_table[('q20','a')] = 'q33'



    transition_table[('q34','a')] = 'q1'
    transition_table[('q34','o')] = 'q4'
    transition_table[('q34','u')] = 'q7'
    transition_table[('q34','m')] = 'q9'
    transition_table[('q34','b')] = 'q21'
    transition_table[('q34','p')] = 'q24'

    # Final state
    transition_table[('q33',' ')] = 'q34'
    transition_table[('q33','#')] = 'accept'
    transition_table[('q34',' ')] = 'q34'
    transition_table[('q34','#')] = 'accept'


    # Main Program #
    current_token = ''
    state = 'q0'
    n = 0

    while state != 'accept':
        huruf = input_kata[n]
        current_token += huruf

        try:
            state = transition_table[(state, huruf)]
        except:
            state = None

        if state == 'q44':
            current_token = ''
        elif state == None:
            break

        n += 1

    if state == 'accept':
        #st.write('Semua kata telah dianalisis : ',kata,' -> valid')
        valid = True
        return valid

    elif state == None:
        #st.write('Semua kata telah dianalisis : ',kata,' -> tidak valid')
        valid = False
        return valid


def parser(kalimat):
    non_terminal = ['S', 'NN', 'VB']
    terminal = ['abah', 'omak','uwak','buku','pensel','pemadam','mumasak','mumboli','mumbacu','menjua']

    parse_table = {}

    tokens = kalimat.lower().split()
    tokens.append('EOS')

    parse_table[('S','abah')] = ['NN', 'VB', 'NN']
    parse_table[('S','omak')] = ['NN', 'VB', 'NN']
    parse_table[('S','uwak')] = ['NN', 'VB', 'NN']
    parse_table[('S','buku')] = ['NN', 'VB', 'NN']
    parse_table[('S','pensel')] = ['NN', 'VB', 'NN']
    parse_table[('S','pemadam')] = ['NN', 'VB', 'NN']
    parse_table[('S','mumasak')] = ['error']
    parse_table[('S','mumboli')] = ['error']
    parse_table[('S','mumbacu')] = ['error']
    parse_table[('S','menjua')] = ['error']
    parse_table[('S','EOS')] = ['error']

    parse_table[('NN','abah')] = ['abah']
    parse_table[('NN','omak')] = ['omak']
    parse_table[('NN','uwak')] = ['uwak']
    parse_table[('NN','buku')] = ['buku']
    parse_table[('NN','pensel')] = ['pensel']
    parse_table[('NN','pemadam')] = ['pemadam']
    parse_table[('NN','mumasak')] = ['error']
    parse_table[('NN','mumboli')] = ['error']
    parse_table[('NN','mumbacu')] = ['error']
    parse_table[('NN','menjua')] = ['error']
    parse_table[('NN','EOS')] = ['error']

    parse_table[('VB','abah')] = ['error']
    parse_table[('VB','omak')] = ['error']
    parse_table[('VB','uwak')] = ['error']
    parse_table[('VB','buku')] = ['error']
    parse_table[('VB','pensel')] = ['error']
    parse_table[('VB','pemadam')] = ['error']
    parse_table[('VB','mumasak')] = ['mumasak']
    parse_table[('VB','mumboli')] = ['mumboli']
    parse_table[('VB','mumbacu')] = ['mumbacu']
    parse_table[('VB','menjua')] = ['menjua']
    parse_table[('VB','EOS')] = ['error']

    stack = []
    stack.append('#')
    stack.append('S')

    if valid == True:
        idx_token = 0
        simbol = tokens[idx_token]

        while (len(stack) > 0 ):
            top = stack[len(stack)-1]

            if top in terminal:

                if top==simbol:
                    stack.pop()
                    idx_token = idx_token + 1
                    simbol = tokens[idx_token]

                    if simbol == 'EOS':
                        stack.pop()

                else:
                    #print("GRAMMAR ERROR")
                    break

            elif top in non_terminal:

                if parse_table[(top,simbol)][0] != error:
                    stack.pop()
                    simbol_to_be_pushed = parse_table[(top, simbol)]

                    for i in range(len(simbol_to_be_pushed)-1, -1, -1):
                        stack.append(simbol_to_be_pushed[i])

                else:
                    #print("GRAMMAR ERROR")
                    break
            else:
                #print("GRAMMAR ERROR")
                break

        if (simbol == 'EOS') and (len(stack) == 0):
            st.write("Lexical Analyzer : '",kalimat, "' valid :white_check_mark: ")
            st.write("Parser : '", kalimat, "' valid :white_check_mark: ")
        else:
            st.write("Lexical Analyzer : '",kalimat, "' valid :white_check_mark:")
            st.write("Parser : '", kalimat, "' tidak valid :x: ")

# Proses Front End Website #
st.set_page_config(page_title="TUBES TBA", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

with st.container():
    st.title("TUBES TBA")
    st.subheader("Lexical Analyzer dan Parser Sederhana untuk Teks Bahasa Alami")

with st.container():
    st.write("---")
    st.subheader("Anggota Kelompok : ")
    st.subheader("-")
    st.subheader("-")
    st.subheader("-")

with st.container():
    st.write("---")
    left,mid, right = st.columns(3)

    st.header("LIST KATA")
    
    st.write("---")

with st.container():
    mid = st.subheader(" abah | omak |uwak | buku | pensel | pemadam | mumasak | mumboli | mumbacu | menjua ")
    st.write("---")
with st.container():

    st.write("Subjek (NN) : Abah, Omak, Uwak")
    st.write("---")

    st.write("Verb (VB) : Mumasak, Mumboli, Mumbacu, Menjua")    
    st.write("---")
            
    st.write("Object (NN) : Buku, Pensel, Pemadam")

    st.write("---")
#
with st.container():
    st.write(" ")
    st.header("Lexical Analyzer dan Parser")
    st.write("---")

with st.container(): 
    st.subheader("CFG yang merepresentasikan aturan bahasa sederhana untuk bahasa manusia.")
    st.write("Gunakan bahasa melayu yang ada di LIST KATA")

with st.container():
    
    st.header("Masukkan kalimat")
    kalimat = st.text_input("")
    st.write("Accepted Sentence : NN + VB + NN")
    
    if kalimat != "":
        valid = LexicalAnalyzer(kalimat)

        if valid == True:
            st.write("---")
            st.subheader("Keterangan : ")
            parser(kalimat)
        elif valid == False:
            st.write("---")
            st.subheader("Keterangan : ") 
            st.write("Lexical Analyzer : '", kalimat, "' tidak valid :x:")
            st.write("Parser : '", kalimat, "' tidak valid :x:")

st.write("---")



    



    


    
        

    
