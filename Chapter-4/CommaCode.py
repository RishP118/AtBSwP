def cc(spam):
    for i in range(len(spam)):
        if i<(len(spam)-1):
            print(spam[i],end=", ")
        else:
            print("and",spam[i])
spam=['apples', 'bananas', 'tofu', 'cats']
cc(spam)
