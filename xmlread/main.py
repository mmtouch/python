from lxml import etree
import time


def lxml_read(file_path):
    path_list = list()
    path_map = dict()
    path_str = ""
    events = ("start", "end")
    context = etree.iterparse(file_path, events=events, huge_tree=True)

    for action, elem in context:
        tag = elem.tag

        if action == "start":
            if len(path_str) > 0:
                path_str += ","

            path_str += tag
            path_list.append(tag)
            if path_str in path_map:
                path_map[path_str] += 1
            else:
                path_map[path_str] = 1

        elif action == "end":
            path_list.pop()
            pos = path_str.rfind(",")
            if pos >= 0:
                path_str = path_str[0:pos]

        elem.clear()

    for path_key in path_map:
        print(f"[{path_map[path_key]}] {path_key}")


if __name__ == '__main__':
    file_path = "D:\\temp\\export.xml"
    print(f"Start Bench : Python : lxml_read")
    start_time = time.time()
    lxml_read(file_path)
    elapsed_time = int(time.time() - start_time)
    print(f"Elapsed Time(sec) : {elapsed_time}")

