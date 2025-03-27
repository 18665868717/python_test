import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
def get_test():
    url='https://clustrmaps.com/persons/Edward-Snowden'
    header={
        #"Sec-Fetch-Mode":"navigate",
        #"Sec-Ch-Ua":'Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115',

            "Content-Type":"text/json;charser=utf-8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9",
            #"Upgrade-Insecure-Requests":"1",
            #"Sec-Ch-Ua-Platform":"Windows",
            #"Sec-Fetch-Dest":"document",
            #"Referer":"https://clustrmaps.com/a/?__cf_chl_tk=Q5z2YqLGc1p2TeDnmoLaYKPOlXzgkZ2LmeRW1MOfDy0-1690204900-0-gaNycGzNCns",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",

            }
    cookie={"PHPSESSID":'k9qfpig827lii5sk78u3dmp08i'}
    data={
        "md":"XZvp5bbmoAL.pPkCgfDNskLGqBpiAjMV3.7VC02yKOo-1690207424-0-Acpt7_QEO91AC8Ljbc8OSFydEp5ijWtpUc6pSeIXpnB8z65uqD7yykn6L_YnXLkb66WmgnfCFrlnzfGHi13hB1SVOh4ItwaSO8YIGPD3T-uHKeszNm8qUnAcGJjxzA2CjcblCsSCPaADqplhDbCfGZFDlj5u9XNkfUZmKGJw_611NzxkcO0hWkCXkqSOvpinzWrPjBlr9A6ospwAQ8K5bRwD3CTTrgr3LdO2h9dGGhMXYqPbIv5Ujcj7WZpaEV7j2gvdnvzRzfW9BjhaqYpRiXUxwODcAAMnDpebTmT3YqJWPM7H7iKM6WzaYB6zGg8QRrcOHLm6sP0Rh5HNwlaoJrHixAvlg0dg0bcfJ1zqX0UeV1k7CtqBfU1KyMHxVuAOKveDPxCDKQ50a_4_FyGv6oVduX174vrlbr6JT3mfs4XrrOWdb6tynojVk6EX51edBN-AMMAmqvvD3vtxPdboVh-bkAscFCKsFOZKBy-24Dl1Fa-QwaGpEg8KyQbl25HVpRYdFqaZoXWikdW64kfueEBuXjaWjOkqlfmZoK7LiN_3tRmRrBXzbbl9H1GPkTXd6lS88O68tYUyoV_CiOlIKpLC8CwSUkArkpgPCNKguLv0z9B-fBcM1p_GemDFOd0XkyuqagxWiLOKzDGVjk6-ayFnhUYf2gxU5uHSrclOtD5Ff95E7o7Z2trQuYqIwOw4Ktz8iYAqNMJmctjLg5NirsHL3ZoI0mLc9Vk7wDLXMUEXauxXN_LFPi1cGlEiXJpLV4Y3_6SqGKW4dZaYq_WZr9OAFgfWuNkDm1aFOe5IdyY58pyX2ovMADFd1bUIvevk4QqhF3M0OmJOHvlGxDUV10pglPaUzUEebNU0OC0Pti6DMtmRVw7EukvP15nuBS9rwkthUs3dTeOBiixNWpD8_vzsw5OdyOm7_tHRkwG6aUvS_lBh1BXx_1iLzzHh99JY7GblJCp7VGvpxKvwB_-vtppcxMalh6kagy8BraPkmheqgYTzPa62d9D021rfkRX5EhliXE-XsIzGFCZETT3Cgxs_efqSQk0OsCKYV7nrR-CbOr0QH5N6ni6n5DwOOv1Nlo8th_DaqvWeQj3Cq1V7_Qd9HJ0_0-NL41521D7s7_7wm4Qt67MezvkwWCnBoIuHBdKph9Swa2Swc8iEouhGyjVUyKlXPjqUAP_6sC85U9aVwvVj31zmvabor6Xrsa9DBHggmGVnXlcKzrfipxPFaeeT_GxduPuyghWJFb1atby7RsAyRL4WY8F5IereuQ3J97Hkj0sX1FiZ4s2n95DBNBhAJwTepQOAYn9AFxC4KgGz_wcS0lmyhkJ-9I2sUKZO5j8KsdP2Zn1Ikw1W_jJTlQ-XMrRtTVBtnIojh5RsWAnA8F5mhiMpJ2ykyGw2VaUPWLMnW_1m5kwQPX54xNOEStTq75m48gTJT7P4QhxjUNPgd21Y-3D7SatPg3uKJuYJnjLFDxqLK7tYmnx-s-JMf7VVT4l3XBcKqjdUJXjiCh4cn1sBBAOWtgPj4FR4pm9khJwqIVrn_9RRHmax_QJZQClNtslvsoGFPP5yjrPGcw5nbFXHU7TdWhjJ_H1UCPVsKjUdv1faZgEUPySl9nROjaQqaMaWlGClxX0c8P0cAUQhdzbYufWYp-5Ge0ty8uuxt6Awhc-zDXixy_x9loP_38vbu7jY-4L06xEvgc4GbWTcVtT-cC70FRLKPvENXML_K9aSipknabMhDr4KedZ2USKNBY-wzeZDnGZMyGuO77esfs3zID5y92UY8hGBsp4j1ZqnOj5Wx6TTAfYfyrJZIW6cppXF0x4WZ3lzTClXgoP5FlytskLhTXOESim1esUwTsYrKNGqaYe9RtRVaBAdVMxyyEamtgSStQbgpCQ7ieenaU2Hj42SCqZhdoFr3Of5YJhRaeWV5MHQF_zloaF0jQv0-yjEfE2G2HhRYx7OgRdTAvRaGZA-b6ELF1JUAESH5g5JCmqOuPx6I-DcSCgSgeQgfEtUNulFFRWze0Mbgb19vgKrIYdjwooYbedTglxKc7hhNbxyCBQGfdEYkWOTuSAFqGLxH_3nDYBkefhaoRo9tprcnTdH5ZoQNTQc7aR5PKDXNvW8-VmdXeWyO9E52oWAsCIuPpAk-h9fCLX9lMcJ4zEj-qAF3oyvDSWoiCWeoWESiEMt9C2rsHb-NhA96Lt2gVuXBjyGc8xeZlM7bAkZWbXawPuhUbAD2kM5h7L3RCdTmTQyIdL9Est0ACwkKM33r2JuiUgsQN4xHfYsK_F_0bs6u-n_dY4oWhwuHkw6NfTTOxDhN9DBk9hMrlE_psVCoY8PMPzUgXJxadUm18YA4xgnrQnUdKrNRMHUai7OcUvknEVd0uL7Dopqu99jyVsmNnCsIK0F-oqfYjJgKO7NvNgluSzTgsghr5mGdLe8IlFgEMr0ZjMrYC9HZD0TEFgNbmND6VKH_d8Z0oUe3lO2sRqvh78GZWF0zUA4Hv_-ag6TKjnLMuM5BNmTPS8f_k-dZLfVWzPRMNI37DYmAmUBBDYHtkxj-_XyVb413lBXP_6rbtww9DP2OqNeWCEiUwiz5FbT6y8xmL_GCtNMIHkPMqlsw88eYgdkuTcYQpMo6cEt6EhxudmO_sMaYnKtgHnpjITP2RLTXLKnqBQQX3z5ar5B39MrPDK4oafR_VkzJLXCn3fnlF7Fw3ycPjBuz9U680wvtZpGmCjRB_vm_Jwe9gYVrTdFS2xy7_iExdX3YdTs9H1C1VlasmL1Z51CC53RQ8hUIUDDwWQY7KfR1qn6KRzyXBP7UbKcmE26V5cTH7CxEdXCkRvIes8Vth9lZkp3ktA7eobxFSbyBapBE8oD4sajn_xWfkBfBX9WvbLVNV5s3rJUDw6UOUSEcrZ8_vKsdHV5G8Pvf0fA78JqZVXQRWynyjxwXpKr3LPMhgOIrUMWfncuN-BDb4HxantGsku6eTApr08yzQ6L_QotLCmIcq2mpriJa_iNjjlp8aXs7qkhp-XNOetubtL-7udpZx2X_elYfoEskxgQp7umEujTLaqs-n8SxY-bkooHQ0rn29VT1NiO8BsXHTXBJdQG-l6nZ9M6amudz3AXHDHEDmsnUn7LQ7TOCGUmGz2p8d5UEPhKNUh7cDUGiI2HMsQAQDH1ZJ54AzoT3BHqLieacOp4gdEEBflSdfmTh57CO49lzpHStrHV15sfm4AUUIxPYHg3h6oWp15x9ABC0p_Qp7DBeTSCkoOlETOxzp9VoQI-fxHwLyitHYUw6u6cWee-TMx2QS9tIqgo3iI-74KT0cHxAvxM1UP7CgrqbE4vnqoTx8iA4_CjV0IdfmjAheGiiHXwADKO88dk9Kutny6oFluZtZz70gkqefsx-fCHTi0MGQ",
        "sh":"5fbb5621372f8fc61bca1cfa6465554a",
        "aw":"GgNcImfLnoNU-1-7ebcb5524c5f04d2",
    }
    rep=requests.get(url=url,headers=header,allow_redirects=False)
    response=rep.text
    print(response)
    # soup = BeautifulSoup(response,'html.parser')
    # print(soup)
    # result = soup.select('body div:nth-of-type(2) div div:nth-of-type(2) div div')
    # print(result)
    # print(soup.text)
    # result_all=soup.select('body div:nth-of-type(2)')
    # print(result_all)
    # selector = etree.HTML(rep)
    # links = selector.xpath('body>div:nth-of-type(2)')
    # print(links)
def get_url(name):
    url="https://clustrmaps.com/persons/"+name
    response=requests.get(url=url)
    content=response.content
    return BeautifulSoup(content,'html.parser')
if __name__ == '__main__':
    get_test()