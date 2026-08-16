class Out (Exception):
    pass
# we build a own excetion by using inher 
def coffee(suger,milk):
    if suger ==0 or milk==0:
        raise Out ('WE r out suger or milk')

coffee(1,0)