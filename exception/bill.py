# we build a bill app

class Notthere(Exception): pass

def bill(item, cups):
    order = {'masala': 30, 'black': 40}
    
    try:                                        # ← was missing
        if item not in order:
            raise Notthere('given item is not there')
        if not isinstance(cups, int):
            raise TypeError('use only nums')
        
        total = order[item] * cups              # ← typo fixed: iteams → item
        print(f"num of cups {cups} total {total}")
    
    except Notthere as e:                       # ← except needs exception type
        print('error', e)
    except TypeError as e:                      # ← separate TypeError catch
        print('error', e)
    
    finally:                                    # ← must be inside def
        print('thx for visiting')


bill('masala', 4)
bill('masala', 'one')