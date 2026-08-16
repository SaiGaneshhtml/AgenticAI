def tea_ser(iteam,qunt):
    try:
        price={'masala':4}[iteam]
        cost=qunt*price# here oper overlading will be issue 
        #if user entere '' it print we need add a type check 
        print(f"here cost : {cost}")
    except KeyError:
        print('we did not have such iteam')
    except TypeError:
        print('qunt must be in  num')

tea_ser('balck',4)
tea_ser('masala',3)
tea_ser('masala','one')