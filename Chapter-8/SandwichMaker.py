import pyinputplus as pyip
p={'Wheat':20,'White':30,'Sourdough':15,'Chicken':30,'Turkey':40,'Ham':20,'Tofu':40,'Cheddar':20,'Swiss':30,'Mozzarella':20,'Mayo':10,'Mustard':10,'Lettuce':5,'Tomato':5}
while True:
    order=[]
    a= pyip.inputMenu(['Wheat','White','Sourdough'], prompt="Bread Type: ",numbered=True)
    order.append(a)
    b= pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'], prompt="Protein Type: ",numbered=True)
    order.append(b)
    c= pyip.inputYesNo(prompt="Do you want cheese?")
    if c=='Yes':
        d= pyip.inputMenu(['Cheddar','Swiss','Mozzarella'], prompt="Cheese Type: ",numbered=True)
        order.append(d)
    e= pyip.inputYesNo(prompt="Do you want mayo?")
    if e=='Yes':
        order.append('Mayo')
    f= pyip.inputYesNo(prompt="Do you want mustard?")
    if f=='Yes':
        order.append('Mustard')
    g= pyip.inputYesNo(prompt="Do you want lettuce?")
    if g=='Yes':
        order.append('Lettuce')
    h= pyip.inputYesNo(prompt="Do you want tomato?")
    if h=='Yes':
        order.append('Tomato')
    i=pyip.inputInt(prompt="No. of Sandwiches you want: ", min=1)
    t=0
    for s in order:
        c=p[s]
        t+=c
    print("Total: ",t*i)
