import time
import random 
import string
import multiprocessing as mp
import pprint
import pickle

DURACION = 60

def random_word(length):
    word = string.ascii_letters + string.digits
    return ''.join(random.choice(word) for i in range(length))

    

def add_word(star_time, word_dict):
    diff_time = 0

    while(diff_time < DURACION):
        time_now = time.time()
        diff_time = time_now - star_time
        print(diff_time)

        word = random_word(5)
        if word in word_dict.keys():
            word_dict[word] =+ 1
        else:
            word_dict[word] = 0
        #pprint.pprint(word_dict.keys())



if __name__ == '__main__':
    start_time = time.time()
    manager = mp.Manager()
    word_dict = manager.dict()
    N_PROCESSES = 3

    pool = mp.Pool(N_PROCESSES)
    pool.apply_async(add_word, args = (start_time, word_dict))
    pool.close()
    pool.join()

    pprint.pprint(word_dict.values())
    
    elementos = len(word_dict)
    repetidos = 0
    for key in word_dict.keys():
        if word_dict[key] > 0:
            reetidos =+ 1
        
    diferentes = elementos - repetidos
    ''' salvar '''
    with open(pickefile, 'wb') as f:
        pickle.dump(word_dict,f)

    print(" --------------------------------------  ")
    print(f" ----  elementos  ---  {elementos}----  ")
    print(f" ----  repetidos  ---  {repetidos}----  ")
    print(f" ----  diferentes  ---  {diferentes}----  ")
