def parse_Input(file):
    updates:list = []
    rules:list = []
    onUpdates = False
    for line in file:

        if line.__contains__("\n"):
            line = "".join(filter(lambda c: c != "\n", line))

        if onUpdates:
            updates.append(line)
        elif line == "":
            onUpdates = True
            continue
        else:
            rules.append(line)

    return rules, updates



def check_line(update:list, rules:list):
    validLines:list = []
    for page in updates:
        pageOrdered = True
        for rule in rules:
            rule = rule.split("|")
            if rule[0] in page and rule[1] in page:
                if not (int(page.index(rule[0])) < int(page.index(rule[1]))):
                    validLines.append(order_Line(page.split(","),rules))
                    break
        # if pageOrdered:
        #     validLines.append(page)
    print(validLines)
    return validLines

def order_Line(page:list, rules:list):
    ordered = True
    while True:
        ordered = True
        for rule in rules:
            rule = rule.split("|")
            if rule[0] in page and rule[1] in page:
                if not (int(page.index(rule[0])) < int(page.index(rule[1]))):
                        page[page.index(rule[0])] = rule[1]
                        page[page.index(rule[1])] = rule[0]
                        ordered = False
                        break
        if ordered:
            break
    return page

def get_middle_pages(validUpdates:list):
    middleList:list =[]
    for page in validUpdates:
        middleList.append(page[len(page)//2])
    return list(map(int,middleList))

file = open("Day5.txt","r")


rules, updates = parse_Input(file)

print(sum(get_middle_pages(check_line(updates, rules))))
# print(rules)
# print("----------------")
# print(updates)