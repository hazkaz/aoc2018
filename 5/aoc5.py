import cProfile
import re
import string
import operator

def react(polymer,remove=None):
    # print(f'{str.lower(remove)}|{str.upper(remove)}',"".join(polymer),remove)
    polymer = list(re.sub(f'{str.lower(remove)}|{str.upper(remove)}','',"".join(polymer)))
    done=False
    length = len(polymer)
    while(done==False):
        done=True
        index=0
        while(index<length-1):
            char=polymer[index]
            nextChar = polymer[index+1]
            if(char!=nextChar and str.lower(char)==str.lower(nextChar)):
                done=False
                del polymer[index:index+2]
                length-=2
                index-=1
                # print(char,nextChar)
            index+=1
        # print("before",a,len(a))
        # print("after",a,len(a))
    # print(a)
    return len(polymer)

def main():
    with open('input5.txt') as file:
        a = list(file.read().strip())
        effectiveness = {}
        for letter in string.ascii_lowercase:
            shrunk_length = react(list(a),letter)
            effectiveness[letter]= shrunk_length
            print(letter,shrunk_length)
        print(min(effectiveness.items(),key=operator.itemgetter(1)))
if __name__ == '__main__':
    cProfile.run("main()")
    # main()
