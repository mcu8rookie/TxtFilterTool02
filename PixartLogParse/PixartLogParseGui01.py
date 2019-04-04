#PixartLogParse:

import os
from tkinter import *
from tkinter import filedialog

if 0:
    RoutineControlVariable = int(input("Please entr RoutineControlVariable value? RCV = "))

else:
    RoutineControlVariable = 1

if __name__ == "__main__":
    print("RoutineControlVariable = " + str(RoutineControlVariable))
    if RoutineControlVariable == 0:
        pass
    elif RoutineControlVariable == 1:
        pass
    else:
        pass

    
    

    root = Tk()
    root.wm_title("PXI data frame analyze tool v0.01.by Author Name.")
    root.geometry("800x500")

    

    #Portion0
    #软件简介
    RowSpanNbr = 1
    ColumnSpanNbr = 40
    EntryWidth = 100
    
    StartRow = 0
    StartCol = 0

    Portion0_Label0 = Label(root,text = "Portion_0:    软件简介：")
    Portion0_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

    Portion0_Label1 = Label(root,text = "        这是一个分析PXI原始数据格式文件的工具，对符合PXI格式的文件进行分析，主要是整理数据及画波形。")
    Portion0_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
    
    # Portion1
    #选择待处理文件
    StartRow = StartRow + 2
    StartCol = StartCol + 0


    Portion1_Button0_StringVar = StringVar()
    Portion1_Entry0_StringVar = StringVar()

    def Portion1_Button0_Function():
        Portion1_Button0_filedialog = filedialog.askopenfilename()
        print(Portion1_Button0_filedialog)
        Portion1_Entry0_StringVar.set(Portion1_Button0_filedialog)
    
    Portion1_Label0 = Label(root,text = "Portion_1:    指定待处理文件：")
    Portion1_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

    Portion1_Label1 = Label(root,text = "        请输入待处理文件名。")
    Portion1_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr//4,sticky = W)
    Portion1_Label2 = Label(root,text = "（或者使用按键选择文件）")
    Portion1_Label2.grid(row = StartRow + 1,column = StartCol + ColumnSpanNbr//4,columnspan = ColumnSpanNbr//4,sticky = W)

    Portion1_Button0 = Button(root,text = "选择文件",command = Portion1_Button0_Function)
    Portion1_Button0.grid(row = StartRow + 1,column = StartCol + ColumnSpanNbr//4+ColumnSpanNbr//4,columnspan = ColumnSpanNbr//4,sticky =W)

    Portion1_Entry0 = Entry(root,width = EntryWidth,textvariable = Portion1_Entry0_StringVar)
    Portion1_Entry0.grid(row = StartRow + 2,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
    
    
    #Portion2
    #选择PPG通道数
    #

    StartRow = StartRow + 3
    StartCol = StartCol + 0

    Portion2_Label0 = Label(root,text = "Portion_2:    选择PPG数据通道数。")
    Portion2_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

    Portion2_RadioButtons_Group = IntVar()
    Portion2_RadioButtons_Group.set(0)

    Portion2_RadioButton_ColumnNbr = 5

    def Portion2_RadioButtons_Function():
        print(str(Portion2_RadioButtons_Group.get()))
        
    Portion2_RadioButton1 = Radiobutton(root,variable = Portion2_RadioButtons_Group,text = "1通道",value = 1,command = Portion2_RadioButtons_Function)
    Portion2_RadioButton1.grid(row = StartRow+1,column = StartCol + 0*Portion2_RadioButton_ColumnNbr,sticky = W)
    Portion2_RadioButton2 = Radiobutton(root,variable = Portion2_RadioButtons_Group,text = "2通道",value = 2,command = Portion2_RadioButtons_Function)
    Portion2_RadioButton2.grid(row = StartRow+1,column = StartCol + 1*Portion2_RadioButton_ColumnNbr,sticky = W)
    Portion2_RadioButton3 = Radiobutton(root,variable = Portion2_RadioButtons_Group,text = "3通道",value = 3,command = Portion2_RadioButtons_Function)
    Portion2_RadioButton3.grid(row = StartRow+1,column = StartCol + 2*Portion2_RadioButton_ColumnNbr,sticky = W)
    Portion2_RadioButton4 = Radiobutton(root,variable = Portion2_RadioButtons_Group,text = "4通道",value = 4,command = Portion2_RadioButtons_Function)
    Portion2_RadioButton4.grid(row = StartRow+1,column = StartCol + 3*Portion2_RadioButton_ColumnNbr,sticky = W)
    Portion2_RadioButton5 = Radiobutton(root,variable = Portion2_RadioButtons_Group,text = "5通道",value = 5,command = Portion2_RadioButtons_Function)
    Portion2_RadioButton5.grid(row = StartRow+1,column = StartCol + 4*Portion2_RadioButton_ColumnNbr,sticky = W)
    
    #Portion3:
    #选择Gsensor量程// 0:2G, 1:4G, 2:8G, 3:16G

    StartRow = StartRow + 2
    StartCol = StartCol + 0

    Portion3_Label0 = Label(root,text = "Portion_3:    选择Gsensor量程。")
    Portion3_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

    Portion3_RadioButtons_Group = IntVar()
    Portion3_RadioButtons_Group.set(0)
    Portion3_RadioButton_ColumnNbr = 5
    def Portion3_RadioButtons_Function():
        print(str(Portion3_RadioButtons_Group.get()))
    Portion3_RadioButton1 = Radiobutton(root,variable = Portion3_RadioButtons_Group,text = "±2G",value = 1,command = Portion3_RadioButtons_Function)
    Portion3_RadioButton1.grid(row = StartRow+1,column = StartCol + 0*Portion3_RadioButton_ColumnNbr,sticky = W)
    Portion3_RadioButton2 = Radiobutton(root,variable = Portion3_RadioButtons_Group,text = "±4G",value = 2,command = Portion3_RadioButtons_Function)
    Portion3_RadioButton2.grid(row = StartRow+1,column = StartCol + 1*Portion3_RadioButton_ColumnNbr,sticky = W)
    Portion3_RadioButton3 = Radiobutton(root,variable = Portion3_RadioButtons_Group,text = "±8G",value = 3,command = Portion3_RadioButtons_Function)
    Portion3_RadioButton3.grid(row = StartRow+1,column = StartCol + 2*Portion3_RadioButton_ColumnNbr,sticky = W)
    Portion3_RadioButton4 = Radiobutton(root,variable = Portion3_RadioButtons_Group,text = "±16G",value = 4,command = Portion3_RadioButtons_Function)
    Portion3_RadioButton4.grid(row = StartRow+1,column = StartCol + 3*Portion3_RadioButton_ColumnNbr,sticky = W)
    
    #Portion4:
    #选择输出文件夹，注意是应该选择文件夹，输出将会新建一个文件夹，之后将三个文件放在对应的文件夹里面，
    #可以不选择
    StartRow = StartRow + 2
    StartCol = StartCol + 0

    Portion4_Button0_StringVar = StringVar()
    Portion4_Entry0_StringVar = StringVar()

    def Portion4_Button0_Function():
        Portion4_Button0_directory = filedialog.askdirectory()
        print(Portion4_Button0_directory)
        Portion4_Entry0_StringVar.set(Portion4_Button0_directory)
        print()
        
    
    Portion4_Label0 = Label(root,text = "Portion_4:        指定输出文件位置。")
    Portion4_Label0.grid(row = StartRow + 0,column = StartCol+0,columnspan = ColumnSpanNbr,sticky = W)
    Portion4_Label0a = Label(root,text = "（输出将是一个文件夹,里面包含几个分析后的输出文件。）")
    Portion4_Label0a.grid(row = StartRow + 0,column = StartCol + ColumnSpanNbr//4,columnspan = ColumnSpanNbr//2,sticky = W)
    Portion4_Label1 = Label(root,text = "        数据处理结果將放在下面位置。")
    Portion4_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr//4,stick = W)
    Portion4_Label2 = Label(root,text = "（或者使用按键选择位置）")
    Portion4_Label2.grid(row = StartRow + 1,column = StartCol + ColumnSpanNbr//4,columnspan = ColumnSpanNbr//4,sticky = W)

    Portion4_Button0 = Button(root,text = "选择位置",command = Portion4_Button0_Function)
    Portion4_Button0.grid(row = StartRow+1,column = StartCol + ColumnSpanNbr//4 + ColumnSpanNbr//4,columnspan = ColumnSpanNbr//4,sticky = W)
    
    Portion4_Entry0 = Entry(root,width = EntryWidth,textvariable = Portion4_Entry0_StringVar)
    Portion4_Entry0.grid(row = StartRow + 2,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
    

    #Portion5:
    #运行及结果。
    StartRow = StartRow + 3
    StartCol = StartCol + 0
    def Portion5_Button0_Function():
        errorflag = 0
        print("Run_Button:")
        #CMD 
##        DataFilterProc01.py
##        -f 0
##        -k a
##        -i D:/PersonalFile/PyProjs/XinxingPythonCode/DataFilter/2019-3-1_14-00.txt
##        -o D:/PersonalFile/PyProjs/XinxingPythonCode/DataFilter/2019-3-1_14-00__out.txt
##        PixartLogParseProc01.py
##        -c n
##        -g m
##        -i inputfile.txt
##        -o outputfolder
        
        CmdLineString = ""
        ParseScriptCmd = "PixartLogParseProc01.py"
        Parameter_PPGChannel = "-c "+str(Portion2_RadioButtons_Group.get())
        Parameter_GsensorRange = "-g "+str(Portion3_RadioButtons_Group.get())
        Parameter_Input = "-i " + Portion1_Entry0_StringVar.get()
        Parameter_Output = "-o " + Portion4_Entry0_StringVar.get()
        #CmdLineString = ParseScriptCmd + " " +Parameter_PPGChannel + " " + Parameter_GsensorRange + " " + Parameter_Input + " " + Parameter_Output
        
        print(ParseScriptCmd)
        print(Parameter_PPGChannel)
        print(Parameter_GsensorRange)
        print(Parameter_Input)
        print(Parameter_Output)
        print(CmdLineString)

        if Portion2_RadioButtons_Group.get()<1 or Portion2_RadioButtons_Group.get()>5:
            Portion6_Text0.delete(0.0,END)
            Portion6_Text0.insert(0.0,"选择PPG数据通道异常")
            errorflag = 1
            
        if Portion3_RadioButtons_Group.get()<1 or Portion3_RadioButtons_Group.get()>4:
            Portion6_Text0.delete(0.0,END)
            Portion6_Text0.insert(0.0,"选择Gsensor量程异常")
            errorflag = 2
            
        infile = Portion1_Entry0_StringVar.get()
        infilebasename = ""
        if os.path.isdir(infile) == True:
            Portion6_Text0.delete(0.0,END)
            Portion6_Text0.insert(0.0,"输入文件异常,输入了路径吧")
            errorflag = 3
        elif os.path.isfile(infile) == True:
            inputtuple = os.path.splitext(infile)
            
            print(type(inputtuple))
            print(inputtuple)
            print(type(inputtuple[1].upper()))
            if inputtuple[1].lower() != ".txt" and inputtuple[1].lower() != ".log":
                Portion6_Text0.delete(0.0,END)
                Portion6_Text0.insert(0.0,"输入文件异常，文件类型错误吧")
                errorflag = 4
        else:
            Portion6_Text0.delete(0.0,END)
            Portion6_Text0.insert(0.0,"输入文件异常")
            errorflag = 5

        outfolder = Portion4_Entry0_StringVar.get()
        outfile = ""
        if os.path.isdir(outfolder) != True:
            Portion6_Text0.delete(0.0,END)
            Portion6_Text0.insert(0.0,"输出路径异常，不是正确的路径吧")
            errorflag = 6
            pass
        else:
            tmp = ""
            tmp = os.path.basename(Portion1_Entry0_StringVar.get())
            print(tmp)
            print(tmp[:tmp.find(".")])
            outfile = outfolder + "/"+ tmp[:tmp.find(".")]
            print(outfile)
            
        
        if errorflag == 0:
            print()
            ##print(CmdLineString)
            CmdLineString = ParseScriptCmd + " " +Parameter_PPGChannel + " " + Parameter_GsensorRange + " " + Parameter_Input + " " + "-o" + " " + outfile

            Portion6_Text0.delete(0.0,END)
            Portion6_Text0.insert(0.0,CmdLineString)
                                             
            os.system(CmdLineString)
            
            pass
        else:
            pass
    Portion5_Label0 = Label(root,text = "Portion_5:        运行。")
    Portion5_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
    Portion5_Label1 = Label(root,text = "（如果上面的设置都正确，则可以运行处理数据了。）")
    Portion5_Label1.grid(row = StartRow + 0,column = StartCol + ColumnSpanNbr//4,columnspan = ColumnSpanNbr//2,sticky = W)
    
    Portion5_Button0 = Button(root,text = "运行",width = 20,command = Portion5_Button0_Function)
    Portion5_Button0.grid(row = StartRow + 1,column = StartCol + ColumnSpanNbr//4,columnspan = ColumnSpanNbr//4,sticky = W)

    ##准备执行的命令格式
    ## command.py -ch chn -gs -i in.txt -o out.txt

    #Portion6:
    StartRow = StartRow + 2
    StartCol = StartCol + 0

    Portion6_Label0 = Label(root,text = "Portion_6:        可能输出一些状态。")
    Portion6_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr//2,sticky = W)

    Portion6_Text0 = Text(root,width = 100,height = 2)
    Portion6_Text0.grid(row = StartRow,column = StartCol,columnspan = ColumnSpanNbr)
    Portion6_Text0.insert(0.0,"CommandLine")
    







    root.mainloop()
    

