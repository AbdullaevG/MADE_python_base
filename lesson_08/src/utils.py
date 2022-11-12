
import heapq
import ujson
import requests
from bs4 import BeautifulSoup

# l1 = [1, 2, 3, 4]
# l2 = [2, 4, 6]

# out: [2, 4]


def merge(lst1, lst2):
    i, j = 0, 0
    res = []    
    while i < len(lst1) and  j < len(lst2):
        if lst1[i] == lst2[j]:
            if not res or res[-1]!=lst1[i]:
                res.append(lst1[i])
            i += 1
            j += 1
            continue 
        elif lst1[i] < lst2[j]:
            i += 1

        else:
            j += 1
    
    print(res)
    return res


def sort_k(lists):
    res = []
    heap = []
    k = len(lists)
    if not k:
        return res
    for idx in range(k):
        if lists[idx]:
            heapq.heappush(heap, (lists[idx][0], idx, 0))
    while heap:
        val, lst_idx, el_idx = heapq.heappop(heap)
        res.append(val)
        if el_idx + 1 < len(lists[lst_idx]):
            heapq.heappush(heap, (lists[lst_idx][el_idx+1], lst_idx, el_idx+1))

    return res


def convet_lenta_xml_to_json():
    lenta_rss_url = "https://lenta.ru/rss/top7"
    response = requests.get(lenta_rss_url)
    xml_content = response.content
    soup = BeautifulSoup(xml_content, features = "xml")
    items = soup.findAll("item")
    json_doc = []
    MAX_DOCS =1
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        author = item.find('author').text
        json_doc.append({"title": title, "link": link, "author": author})
        if len(json_doc) > MAX_DOCS:
            break
        print(f"{title=}, {link=}, {author=}")

    return json_doc



def main():
    convet_lenta_xml_to_json()


if __name__ == "__main__":
    main()
