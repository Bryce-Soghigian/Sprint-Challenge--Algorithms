'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

const count = (word) => {
    if(word.length===2){
        if(word[1]=='th'){
            return true
        }else{
            return false
        }
    }else if (word.length <2){
        return false
    }else{
        if word is between 0 and 2 
        return true + recurse
    }

}


'''
def count_th(word):

#Recursion if 
    if len(word) <= 2:
        if word[:2] == 'th':
            return 1
        else:
            return 0
    elif len(word)<2:
        return 0
    else:
        if word[0] + word[1] == 'th':
            return 1 + count_th(word[1:])
        else:
            return 0 + count_th(word[1:])

# count_th('yeeth')