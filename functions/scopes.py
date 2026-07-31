def saia_chai ():
    sai_chai = 'water'#local
    print(f"this our local {sai_chai}")

sai_chai ="milk"
saia_chai()
print(f"this outer {sai_chai}")
#######################################################
def chai():
    hello_outter="butter" # encloser 
    
    def chai_type():
        hello_inner="black"
        print(f"this inner fun scop{hello_inner}")
    chai_type()

    print(f"this is out side of the{hello_outter}")

hello_global='rrr'
chai()
print(f"this is global{hello_global}")