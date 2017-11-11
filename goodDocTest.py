import csv
def sort_fn(a,b):
    return
if __name__ =='__main__':
    f = open('C:/Users/1G\Desktop/hospital_info.csv', 'r')
    data = csv.reader(f)
    head = list(map(str,f.readline().split(',')))
    findDate = input()
    for i in range(len(head)):   #일치하는 날짜 찾기
        if(head[i]==findDate):
            break
    list = []
    for line in data:  #원하는 날짜에 여는 병원 확인
        if(line[i]=="O"):
            list.append(line)
    f.close()

    list.sort(key=lambda tup:tup[1]) #가까운 순서로 정렬
    for i in range(len(list)):
        print(list[i][0]+"  ",end='')