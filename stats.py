def list_dict(dict):
    new_dict = []
    for key in dict:
        if key.isalpha():
             new_dict.append({"letter": key, "count" : dict[key]})
             
    return new_dict
        

def sort_on(dict): 
    return dict["count"]

def get_letter_count(text):
    letter_count = {"a": 0}
    
    for i in text:
        if i not in letter_count:
            letter_count[i] =1
        else:    
            letter_count[i] += 1
    return letter_count


def get_num_words(text):
    words = text.split()
    return len(words)

def print_dict(dict,path,count):
     
    sorted_dict = list_dict(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    sorted_dict.sort(reverse=True, key=sort_on)
    
    for i in sorted_dict:
        print(f"{i['letter']}: {i['count']}")
    print("============= END ===============")