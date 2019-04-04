#coding=utf-8
#PixartLogParseProc01.py

import os
import sys
import xlrd
import xlwt

PPG_Channel_nbr = 3
MEMS_Channel_nbr = 3


InputFileName = "log1.log"
OutputFileName = "log1_out.xls"
InputFile = None

KeyList = ["Frame Count,","Time,","PPG,","MEMS,"]
KeyLen = [12,5,4,5]
keystatus = 0
key1tmp1 = 0
key1tmp2 = 0
key2tmp1 = 0
key3tmp1 = 0
key2tmp1 = 0

FrameCount = 0
Time = 0
PPG_nbr1 = 0
PPG_nbr2 = 0
ppgstr1 = ""
ppgstr2 = []
PPG_RawData = []
MEMS_nbr1 = 0
memsstr1 = ""
memsstr2 = []
MEMS_RawData = []


Frame_nbr = 0
Tatol_nbr = 0
Excel_State = 0


global row_nbr
row_nbr = 0


RoutineControlVariable = 0.1
RoutineControlDebug = 2

StartUp_By_Cmd = 1

Globel_Error_Code = 0

if __name__ == '__main__':
    Excel_State = 0
    print("RoutineControlVariable = " + str(RoutineControlVariable))

    if StartUp_By_Cmd == 1:
        InputFileName = ""
        OutputFileName = ""
        PPG_Channel_nbr = 0
        MEMS_Channel_nbr = 0
        
        for i in range(len(sys.argv)):
            print("Parameter"+str(i),end=": ")
            print(sys.argv[i])

        ##检查參數数量。
        if len(sys.argv) < 9:
            print("Abnormal:parameter is less than expect")
            Globel_Error_Code = 1

        
        ##检查參數符号。
        if str(sys.argv[1]) != "-c" or str(sys.argv[3]) != "-g" or str(sys.argv[5]) != "-i" or str(sys.argv[7]) != "-o":
            print("Abnormal:some parameter error,parameter1/3/5/7 -> -c/-g/-i/-o")
            Globel_Error_Code = 1
        ##检查參數设置。
        if int(sys.argv[2])<1 or int(sys.argv[2])>5 or int(sys.argv[4])<1 or int(sys.argv[4])>4:
            print("Abnormal:some parameter error,")
            Globel_Error_Code = 1
        else:
            PPG_Channel_nbr = int(sys.argv[2])
            MEMS_Channel_nbr = int(sys.argv[4])
            
        if os.path.isfile(sys.argv[6]) == True:
            print("Normal:Input is a file.")
            InputFileName = sys.argv[6]
            pass
        else:
            print("Abnormal:Input is not a file.")
            Globel_Error_Code = 2
        if os.path.isdir(sys.argv[8]) == True:
            print("Normal:Output is a path.")
            
            pass
        else:
            if os.path.exists(sys.argv[8]) == True:
                print("Normal:Output path is exist.")
            else:
                print("Normal:Output path is not exist,now create it.")
                os.makedirs(sys.argv[8])
            pass
        OutputFileName = sys.argv[8]+"/tmp_out.xls"
        if Globel_Error_Code == 0:
            pass
        else:
            print("Globel_Error_Code = "+str(Globel_Error_Code))
            sys.exit(0)
        pass
    else:
        pass

    ##print("sys.exit(0)")
    ##sys.exit(0)

    #check inputfile

    inputline = ""
    inputlinelen = 0
    inputlinenbr = 0
    
    try:
        InputFile = open(InputFileName,'r')
        print("open file ok.")
        pass
    except:
        Globel_Error_Code = 1
        InputFile.close()
        pass
    finally:
        pass
        

    if Globel_Error_Code != 0:
        print("Globel_Error_Code = "+str(Globel_Error_Code))
    
    InputFile = open(InputFileName,'r')
    inputline = InputFile.readline()
    inputlinelen = len(inputline)
    inputlinenbr+=1
    if RoutineControlDebug == 1:
        print("inputlinenbr = "+str(inputlinenbr),end = "\t")
        print(inputline)
    workbook = xlwt.Workbook(encoding = "ascii")
    sheet1 = workbook.add_sheet(u"ppg_analsys",cell_overwrite_ok = True)
    while inputlinelen > 0:
        if inputlinenbr != 1:
            if KeyList[0] == inputline[0:KeyLen[0]]:
                key1tmp1 = int(inputline[KeyLen[0]:].replace(" ",""))
                FrameCount = key1tmp1
                keystatus = 1
                if RoutineControlDebug == 2:
                    print("FrameCount = "+str(key1tmp1),end = "\t")
            elif KeyList[1] == inputline[0:KeyLen[1]]:
                key2tmp1 = int(inputline[KeyLen[1]:].replace(" ",""))
                Time = key2tmp1
                keystatus = 2
                if RoutineControlDebug == 2:
                    print("Time = "+str(key2tmp1),end = "\t")
            elif KeyList[2] == inputline[0:KeyLen[2]]:
                ppgstr1 = inputline[KeyLen[2]:].replace(" ","")
                #print(ppgstr1)
                ppgstr2 = ppgstr1.split(",")
                #print(ppgstr2)
                PPG_nbr1 = int(ppgstr2[0])
                PPG_nbr2 = int(ppgstr2[1])
                PPG_RawData = ppgstr2[2:]
                if PPG_RawData[len(PPG_RawData)-1] == "\n" or PPG_RawData[len(PPG_RawData)-1] == "\r\n":
                    PPG_RawData = PPG_RawData[:len(PPG_RawData)-1]
                #print(len(PPG_RawData))
                #print(PPG_RawData)
##                for i in range(len(PPG_RawData)):
##                    print("lt["+str(i)+"]="+PPG_RawData[i])
                keystatus = 3
                if RoutineControlDebug == 2:
                    print("PPG_nbr1 = "+str(PPG_nbr1),end = "\t")
                    print("PPG_nbr2 = "+str(PPG_nbr2),end = "\t")
                    print("len(PPG_RawData) = "+str(len(PPG_RawData)),end = "\t")
                    #print(PPG_RawData)
                if len(PPG_RawData) == (PPG_nbr2):
                    pass
                else:
                    Globel_Error_Code = 2
                    print("Globel_Error_Code1 = "+str(Globel_Error_Code))
                    #print("len(PPG_RawData) != (PPG_nbr2*PPG_Channel_nbr)")
            elif KeyList[3] == inputline[0:KeyLen[3]]:
                memsstr1 = inputline[KeyLen[3]:].replace(" ","")
                memsstr2 = memsstr1.split(",")
                MEMS_nbr1 = int(memsstr2[0])
                MEMS_RawData = memsstr2[1:]
                #if MEMS_RawData[len(MEMS_RawData)-1] == "\n" or MEMS_RawData[len(MEMS_RawData)-1] == "\r\n":# or MEMS_RawData[len(MEMS_RawData)-1] == "":
                if MEMS_RawData[len(MEMS_RawData)-1] == "\n" or MEMS_RawData[len(MEMS_RawData)-1] == "\r\n" or MEMS_RawData[len(MEMS_RawData)-1] == "":
                    MEMS_RawData = MEMS_RawData[:len(MEMS_RawData)-1]
                keystatus = 4
                if RoutineControlDebug == 2:
                    print("MEMS_nbr1 = "+str(MEMS_nbr1),end = "\t\n")
                    #print(len(MEMS_RawData))
                    #print(MEMS_RawData)
                
                if len(MEMS_RawData) == (MEMS_nbr1*MEMS_Channel_nbr):
                    pass
                else:
                    Globel_Error_Code = 2
                    print("Globel_Error_Code2 = "+str(Globel_Error_Code))
                    print("len(MEMS_RawData) != (MEMS_nbr2*MEMS_Channel_nbr)")
                    print("len(MEMS_RawData) = "+str(len(MEMS_RawData)))
                    print("(MEMS_nbr2*MEMS_Channel_nbr) = "+str((MEMS_nbr1*MEMS_Channel_nbr)))
                    print(MEMS_nbr1)
                    print(MEMS_Channel_nbr)
                    print(MEMS_RawData)
        
            if(keystatus == 4):
                keystatus = 0
##                #row_nbr = 0
                if Globel_Error_Code == 0:
                    #print header
                    if Excel_State == 0:
                        
                        Excel_State = 1
                        row0 = ["Frame Count","Data Count","Touch Flag","Time","PPG 0","PPG 1","PPG 2","HR","SG","RET"]
                        #print(row0)
                        for i in range(len(row0)):
                            sheet1.write(0,i,row0[i])
                        row_nbr+=1

                    #write ppg data
                    tmp = PPG_nbr2//PPG_Channel_nbr
                    for i in range(PPG_nbr2//PPG_Channel_nbr):
                        sheet1.write(row_nbr+i,0,FrameCount)
                    for i in range(PPG_nbr2//PPG_Channel_nbr):
                        sheet1.write(row_nbr+i,1,i)
                    for i in range(tmp):
                        sheet1.write(row_nbr+i,2,PPG_nbr1)
                    for i in range(tmp):
                        sheet1.write(row_nbr+i,3,Time/tmp)
                    for i in range(tmp):
                        sheet1.write(row_nbr+i,4,int(PPG_RawData[i*3]))
                        sheet1.write(row_nbr+i,5,int(PPG_RawData[i*3+1]))
                        sheet1.write(row_nbr+i,6,int(PPG_RawData[i*3+2]))
                        
                    row_nbr += (PPG_nbr2//PPG_Channel_nbr)
                else:
                    print("Globel_Error_Code"+str(Globel_Error_Code))
        else:
            if "PPG CH#" == inputline[0:7]:
                pass
        inputline = InputFile.readline()
        inputlinelen = len(inputline)
        inputlinenbr+=1
        if RoutineControlDebug == 3:
            #print("inputlinenbr = "+str(inputlinenbr),end = "\t")
            #print(inputline)
            pass
    print("out of while")


    workbook.save(OutputFileName)














