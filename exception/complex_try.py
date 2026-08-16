def coffer_ser(flav):
    try:
        print(f'preparing {flav}')
        if flav == "unknow":
          raise ValueError ('we did know the flav')
    except ValueError as e:
        print('error',e)
    else:
        print('thx')
    finally:
        print('next...')

coffer_ser('unknow')
coffer_ser('black coffee')
    