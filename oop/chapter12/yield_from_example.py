#!/usr/bin/python3
#coding:utf-8
#协程案例
final_result = {}

def salse_sum(pro_name):
    total = 0
    nums = []
    #不停的接受值
    while True:
        #
        x = yield
        print(pro_name +"销量",x)
        #当值为空的时候 跳出
        if not x:
            break
        total += x
        nums.append(x)
    return total,nums

def middle(key):
    while True:
        final_result[key] = yield from salse_sum(key)
        print(key + "销量统计完成！！")

def main():
    data_sets={
        "冰箱":[1200,1500,300],
        "电视":[2300,2300,2300],
        "手机":[9980,12030,23282]
    }
    for key,data_set in data_sets.items():
        print("start key" ,key)
        m = middle(key)
        #启动子生成器
        m.send(None)
        for value in data_set:
            #值 send 值接打入到 salse_sum
            print(value)
            m.send(value)
        #结束子生成器
        m.send(None)
        print("final_result: ",final_result)



if __name__ == "__main__":
    main()
