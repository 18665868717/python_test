import concurrent.futures
import blog_spider
import time


start_time=time.time()
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls=pool.map(blog_spider.craw,blog_spider.urls)
    # print(list(htmls))
    htmls=list(zip(blog_spider.urls,htmls))
    # h_t=htmls[0]
    # print(type(h_t),h_t)
    for url,html in htmls:
        print(url,len(html),"\n")
end=time.time()
print(end -start_time)