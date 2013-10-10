# -*- coding: utf-8 -*-
import wikipedia
from collections import deque


def main():
    def userInput():
        def verifyInput(prompt):
            while True:
                title = raw_input(prompt)
                try:
                    wikipedia.page(title).load()
                except wikipedia.PageError:
                    print "Not a page"
                    continue
                except wikipedia.DisambiguationError:
                    print "Don't use disambiguation pages"
                    continue
                return title

        start = verifyInput("Start article:\t")
        target = verifyInput("Target article:\t")
        return start, target

    def seek(start, target):
        prev_table = dict()
        prev_table[start] = None

        def backtrace(link, li):
            li.append(link)
            prev = prev_table[link]

            if prev is None:
                return li[::-1]
            return backtrace(prev, li)

        level = 0
        queue = deque()
        queue.append((start,0))
        while queue:
            current = queue.popleft()
            if current[1] > level:
                print
                level = current[1]
            print ".",
            try:
                for link in wikipedia.page(current[0]).links:
                    if link not in prev_table.keys():
                        prev_table[link] = current[0]
                        queue.append((link, level+1))

                    if link == target:
                        return backtrace(link, [])
            except wikipedia.DisambiguationError, wikipedia.PageError:
                continue
        return ["No path found"]
    start, target = userInput()
    path = seek(start, target)
    print
    print " -> ".join(path)


if __name__ == "__main__":
    main()