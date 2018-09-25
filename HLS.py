#!/usr/bin/env python
import os,time,copy,sys


url="http://video.cc.com/cctv-1.m3u8"
down_file_patch="/root/zv/mhls/test"
last_date={}
down_file_patch = "./"
sleep_t=1
remove = 1


def change_file_to_map(file_name):
    file_map=[]
    fd=open(file_name,"r")
    date={}
    while True:
        try:
            msg = fd.readline()
            if msg == "":
                break
        except:
            break


        if "EXTINF" in msg:
            date["time"] = msg.split(":")[1].split(",")[0]
        elif msg.split("\n")[0].split(".")[-1] == "ts" and date.has_key("time"):
            date["file"] = msg.split("\n")[0]
            file_map.append(date)
            date = {}


    return file_map


def wget_file_function(url,file_name):
    cmd = 'wget %s -t 5 -T 30 -O %s'%(url,file_name)
    if os.system(cmd):
        print("wget file error commend is :",cmd)
        return 1
    else:
        print("wget successed cmd is:",cmd)
        return 0


def mix_new_old_list(new_list,old_list):
    global last_date
    #print "[mix_new_old_list] old:",old_list
    if last_date != {}:
        try:
            number = new_list.index(last_date)
        except:
            number = -1
    else:
        number = -1


    #print "[mix_new_old_list] last date: ",last_date,"\nfull date",new_list,"\nadd ",new_list[int(number)+1:len(new_list)]
    old_list.extend(new_list[int(number)+1:len(new_list)])
    #print "[mix_new_old_list] new list:",old_list
    return old_list


def com_list(old,new):
    if len(old) != len(new):
        return 1


    for x in range(0,len(old)):
        if old[x] != new[x]:
            return 1


    return 0


def main():
    global last_date
    global sleep_t
    global url
    global down_file_patch
    global remove
    if len(sys.argv) < 2:
        print ('''usage:
    python hls-get.py [url] [down_patch] [sleep] [rename]
    url: the hls stream url
    down_patch: where save the down file. note: end must without "/". eg:/dev/null, default value: ./
    sleep: if m3u8 not update, program sleep some seconds, default 1.
    rename:
          1: rename ts name,default value
          0: don't rename ts name
        ''')
        return 1
    else:
        url = sys.argv[1]
        if len(sys.argv) > 2:
            down_file_patch = sys.argv[2]
        if len(sys.argv) > 3:
            sleep_t = int(sys.argv[3])
        if len(sys.argv) > 4:
            remove = int(sys.argv[4])


    down_url=os.path.dirname(url)
    stream_name = os.path.basename(url)
    old_m3u8_list = []
    m3u8_list = []
    while True:
        m3u8_file = ""
        m3u8_file = "%s/tmp.m3u8"%(down_file_patch)
        wget_file_function(url,m3u8_file)
        new_m3u8_list = change_file_to_map(m3u8_file)


        if com_list(old_m3u8_list,new_m3u8_list):
            m3u8_list = mix_new_old_list(new_m3u8_list,m3u8_list)
            old_m3u8_list = copy.deepcopy(new_m3u8_list)
            new_file = "%s/%s.%s"%(down_file_patch,stream_name,time.strftime('%Y%m%d%H%M%S'))
            cmd = "mv %s %s"%(m3u8_file,new_file)
            os.system(cmd)
        else:
            cmd = "rm -rf %s"%(m3u8_file)
            os.system(cmd)


        if len(m3u8_list) == 0:
            time.sleep(sleep_t)
            continue


        date = m3u8_list[0]
        url_name="%s/%s"%(down_url,date["file"])
        if remove == 1:
            down_file_name = "%s/%s.%s.ts"%(down_file_patch,date["file"],time.strftime('%Y%m%d%H%M%S'))
        else:
            down_file_name = "%s/%s"%(down_file_patch,date["file"])


        if wget_file_function(url_name,down_file_name):
            continue
        if  len(m3u8_list) != 0:
            last_date = copy.deepcopy(m3u8_list[len(m3u8_list)-1])
        del m3u8_list[0]




main()