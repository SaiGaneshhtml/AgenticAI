# creat own exception

def tea(flavor):
        print(f"give {flavor}")
        if flavor not in ['masala','green']:
            raise ValueError ('give one is not there')
        print(f"here is u r {flavor}")

tea('water')
