import concurrent.futures
txt_list=[1,2,3,4,5,6,7,8]
def te_print(va):
    print(va)

def print_with_thread_pool(txt_list):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        pool.map(te_print, txt_list)

if __name__ == '__main__':
    print_with_thread_pool(txt_list)
