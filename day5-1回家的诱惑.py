dict={"地球":
          {"中国":   {"北京":  {"昌平":  {"流沙河":{"老牛湾":"汉科软"}}}},
           "m78星云":{"光之城":{"光之陆": {"光之塔":{"78": "特例家"  }}}}
           }
      }
aa=input("请输入您的地址")      #     地球         \
if aa in dict.keys():
   bb=input("请输入您的地址")    #     中国   m78星云       \
   if bb in  dict[aa].keys() :
        cc = input("请输入您的地址")  #         北京      光之城  \
        if cc in dict[aa][bb].keys():#keys的
            dd = input("请输入您的地址")  #        昌平       光之陆 \
            if dd in dict[aa][bb][cc].keys():  # keys的
                ee = input("请输入您的地址")  #       流沙河     光之塔 \
                if ee in dict[aa][bb][cc][dd].keys():  # keys的
                    ff = input("请输入您的地址")  #      老牛湾      78 \
                    if ff in dict[aa][bb][cc][dd][ee].keys():  # keys的
                        gg = input("请输入您的地址")  #      汉科软     特例家   \
                        if gg in dict[aa][bb][cc][dd][ee][ff]:
                            print("ok")