import wikipedia
from collections import deque


def main():
    def params():
        start = raw_input("Start article: ")
        goal = raw_input("Goal article: ")
        return start, goal

    def seek_path(start, goal):
        prev_table = dict()
        prev_table[start] = None

        queue = deque()
        queue.append(start)

        def path(link, li):
            li.append(link)
            prev = prev_table[link]

            if prev is None:
                return li[::-1]
            return path(prev, li)

        i = 0
        while queue:
            i += 1
            #print "iteration", i, ",", len(queue), "links"
            current = queue.popleft()
            # print current
            try:
                for link in wikipedia.page(current).links:
                    #print link,
                    if link not in prev_table.keys():
                        prev_table[link] = current
                        queue.append(link)

                    if link == goal:
                        # print
                        return path(link, [])
                # print
            except wikipedia.DisambiguationError:
                continue
    start, goal = "Space Jam", "Adolf Hitler" #params()
    print " -> ".join(seek_path(start, goal))


if __name__ == "__main__":
    main()