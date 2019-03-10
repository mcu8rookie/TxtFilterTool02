#DataFilterGui01.py


from tkinter import *
##from tkinter.filedialog import askdirectory
##from tkinter.filedialog import askopenfilename
from tkinter import filedialog



if 0:
    RoutineControlVariable = int(input("Please enter RoutineControlVariable value? RCV = "))
else:
    RoutineControlVariable = 1


if __name__ == "__main__":
    print("RoutineControlVariable = "+str(RoutineControlVariable))
    if RoutineControlVariable == 0:
        #tkinter._test()
        pass
    elif RoutineControlVariable == 1:

        DefaultInputFileName = ""
        DefaultOutputFileName = ""

        RealInputFileName = ""
        RealOutputFileName = ""
        
        root = Tk()
        root.wm_title("DataFilterGui01b.py by lilu:emailaddress.")
        #root.wm_minsize(500,500)

        ColumnSpanNbr = 30

        #Step0:
        StartRow = 0
        StartCol = 0
        Setp0_Label0 = Label(root,text = "Step0:    软件简介。")
        Setp0_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
        Setp0_Label1 = Label(root,text = "        这是一个文本类文件处理工具，主要用于对指定的文本文件做指定的文本操作，可选的操作请注意下面的说明。如果有疑问請联系标题栏地址。")
        Setp0_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

        #Step1:
        step1_selectfilename = StringVar()
        def Step1_Button1_function():
            step1_filename=filedialog.askopenfilename()
            step1_selectfilename.set(step1_filename)
            print("filedialog.askopenfilename",end=":  ")
            print(step1_selectfilename.get())
            Step1_Entry0_String.set(step1_selectfilename.get())
        
        StartRow = 2
        StartCol = 0
        Step1_Label0 = Label(root,text = "Step1:    选择待处理文件。")
        Step1_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
        Step1_Label1 = Label(root,text = "        请在下面的输入待处理文件完整文件名。                    (或者使用按键选择文件)")
        Step1_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

        
        Step1_Entry0_String = StringVar()
        Step1_Entry0 = Entry(root,width = 100,textvariable = Step1_Entry0_String)
        Step1_Entry0_String.set(DefaultInputFileName)
        Step1_Entry0.grid(row = StartRow + 2,column = StartCol + 1,columnspan = ColumnSpanNbr,sticky = W)
        
        Step1_Button1_OpenFileName = Button(root,text = "选择文件",command = Step1_Button1_function)
        Step1_Button1_OpenFileName.grid(row = StartRow + 1,column = StartCol + 8,sticky = W)
        

        #Step2:
        StartRow = 5
        StartCol = 0
        Step2_Label0 = Label(root,text = "Step2:    选择对应的操作动作。")
        Step2_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
        
        Step2_Label1 = Label(root,text = "        选行  。將有包含指定的字符串的文本行留下，其他行都滤除。")
        Step2_Label1.grid(row = StartRow + 1,columnspan = ColumnSpanNbr,sticky = W)
        Step2_Label2 = Label(root,text = "        删行  。將有包含指定的字符串的文本行删除，其他行都留下。")
        Step2_Label2.grid(row = StartRow + 2,columnspan = ColumnSpanNbr,sticky = W)
        Step2_Label3 = Label(root,text = "        截出0。对包含指定的字符串的文本行操作，指定字符串之后的文本留下，之前的都删除（0表示指定字符串也删除）。")
        Step2_Label3.grid(row = StartRow + 3,columnspan = ColumnSpanNbr,sticky = W)
        Step2_Label4 = Label(root,text = "        截出1。对包含指定的字符串的文本行操作，指定字符串之后的文本留下，之前的都删除（1表示指定字符串不删除）。")
        Step2_Label4.grid(row = StartRow + 4,columnspan = ColumnSpanNbr,sticky = W)
        Step2_Label5 = Label(root,text = "        截断0。对包含指定的字符串的文本行操作，指定字符串之后的文本删除，之前的都留下（0表示指定字符串也删除）。")
        Step2_Label5.grid(row = StartRow + 5,columnspan = ColumnSpanNbr,sticky = W)
        Step2_Label6 = Label(root,text = "        截断1。对包含指定的字符串的文本行操作，指定字符串之后的文本删除，之前的都留下（1表示指定字符串不删除）。")
        Step2_Label6.grid(row = StartRow + 6,columnspan = ColumnSpanNbr,sticky = W)

        

        RadioGroup = IntVar()
        RadioGroup.set(0)

        def RadioButtonFunction():
            print("RadioGroup = "+str(RadioGroup.get()))

        Step2_RadioButton1 = Radiobutton(root,variable = RadioGroup,text = "选行",value = 0,command = RadioButtonFunction)
        Step2_RadioButton1.grid(row = StartRow + 7,column = StartCol+ 1,columnspan = 1,sticky = W)
        Step2_RadioButton2 = Radiobutton(root,variable = RadioGroup,text = "删行",value = 1,command = RadioButtonFunction)
        Step2_RadioButton2.grid(row = StartRow + 7,column = 2,columnspan = 1,sticky = W)
        Step2_RadioButton3 = Radiobutton(root,variable = RadioGroup,text = "截出0",value = 2,command = RadioButtonFunction)
        Step2_RadioButton3.grid(row = StartRow + 7,column = 3,columnspan = 1,sticky = W)
        Step2_RadioButton4 = Radiobutton(root,variable = RadioGroup,text = "截出1",value = 3,command = RadioButtonFunction)
        Step2_RadioButton4.grid(row = StartRow + 7,column = 4,columnspan = 1,sticky = W)
        Step2_RadioButton5 = Radiobutton(root,variable = RadioGroup,text = "截断0",value = 4,command = RadioButtonFunction)
        Step2_RadioButton5.grid(row = StartRow + 7,column = 5,columnspan = 1,sticky = W)
        Step2_RadioButton6 = Radiobutton(root,variable = RadioGroup,text = "截断1",value = 5,command = RadioButtonFunction)
        Step2_RadioButton6.grid(row = StartRow + 7,column = 6,columnspan = 1,sticky = W)

        #Step3:
        StartRow = 13
        StartCol = 0
        Setp3_Label0 = Label(root,text = "Step3:    关键字。")
        Setp3_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
        Setp3_Label1 = Label(root,text = "        请在下面输入对应的关键字,以空格分割过个关键字。")
        Setp3_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

        Step3_Key1_Entry0_String = StringVar()
        Step3_Key1_Entry0 = Entry(root,width = 100,textvariable = Step3_Key1_Entry0_String)
        Step3_Key1_Entry0_String.set("")
        Step3_Key1_Entry0.grid(row = StartRow + 2,column = StartCol + 1,columnspan = ColumnSpanNbr,sticky = W)
        
        #Step4:
        step4_selectfilename = StringVar()
        def Step4_Button1_function():
            step4_filename=filedialog.askopenfilename()
            step4_selectfilename.set(step4_filename)
            print("filedialog.askopenfilename",end=":  ")
            print(step4_selectfilename.get())
            Step4_Entry0_String.set(step4_selectfilename.get())
            
        StartRow = 16
        StartCol = 0
        Setp4_Label0 = Label(root,text = "Step4:    输出文件。")
        Setp4_Label0.grid(row = StartRow + 0,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)
        
        Setp4_Label1 = Label(root,text = "        处理结果將保存到下面的文件里。                               (或者使用按键选择文件)")
        Setp4_Label1.grid(row = StartRow + 1,column = StartCol + 0,columnspan = ColumnSpanNbr,sticky = W)

        Step4_Entry0_String = StringVar()
        Step4_Entry0 = Entry(root,width = 100,textvariable = Step4_Entry0_String)
        Step4_Entry0_String.set(DefaultOutputFileName)
        Step4_Entry0.grid(row = StartRow + 2,column = StartCol + 1,columnspan = ColumnSpanNbr,sticky = W)

        Step4_Button_OpenFileName = Button(root,text = "选择文件",command = Step4_Button1_function)
        Step4_Button_OpenFileName.grid(row = StartRow + 1,column = StartCol + 8,sticky = W)

        #Step5:
        StartRow = 19
        StartCol = 0
        Step5_Label0 = Label(root,text = "Step5:    运行。")
        Step5_Label0.grid(row = StartRow + 0,column = 0,columnspan = ColumnSpanNbr,sticky = W)
        Step5_Label1 = Label(root,text = "        如果上面的操作都完成了，就可以点击运行按键启动处理过程了。")
        Step5_Label1.grid(row = StartRow + 1,column = 0,columnspan = ColumnSpanNbr,sticky = W)

        def Step5_Button1_Function():
            import os
            print("Run Step3_Button1_Function().")
            
            RealInputFileName = Step1_Entry0_String.get()
            print("Step1:InputFileName = "+RealInputFileName)
            OperatorFlag = RadioGroup.get()
            print("Step2:RadioGroup = "+str(OperatorFlag))
            RealOutputFileName = Step4_Entry0_String.get()
            print("Step3:OutputFileName = "+RealOutputFileName)
            

            #check step1 setup check inputfilename.
            ErrorFlag = 0
            RealInputFileNameTmp = RealInputFileName
            InputFileNameString = ""
            if(os.path.isdir(RealInputFileNameTmp) == True):
                Step6_Label1["text"] = str("        输入文件名错误。（这是路径）")
                ErrorFlag = 12
            elif(os.path.isfile(RealInputFileNameTmp) == True):
                InputFileNameString = os.path.splitext(RealInputFileNameTmp)
                for i in range(len(InputFileNameString)):
                    print(type(InputFileNameString[i]))
                    print(InputFileNameString[i]);
                if(InputFileNameString[1].lower() != ".txt" and InputFileNameString[1].lower() != ".log"):
                    Step6_Label1["text"] = str("        输入文件名扩展名错误。（只支持.txt or .log）")
                    ErrorFlag = 13
                else:
                    if(os.path.exists(RealInputFileNameTmp) != True):
                        Step6_Label1["text"] = str("        输入文件不存在。（没有对应文件）")
                        ErrorFlag = 14
                    else:
                        ErrorFlag = 0
                        Step6_Label1["text"] = str("        ")
                    pass
            else:
                Step6_Label1["text"] = str("        输入文件名错误。")
                ErrorFlag = 11
            print("Check Step1 = "+str(ErrorFlag))
            
            #Step2 check operator flag
            if(ErrorFlag != 0):
                pass
            else:
                if(RadioGroup.get() < 0 or RadioGroup.get() > 5):
                    print("Error:Operator = "+ str(RadioGroup.get()))
                    ErrorFlag = 21
                else:
                    Step6_Label1["text"] = str("        ")
                    pass
            print("Check Step2 = "+str(ErrorFlag))

            #Step3
            if(ErrorFlag != 0):
                pass
            else:
                
                RealOutputFileNameTmp = RealOutputFileName
                OutputFileNameString = ""
                if(RealOutputFileNameTmp == ""):
                    # if had not input outputfilename. auto created default fileanme.
                    RealOutputFileName = InputFileNameString[0]+"__out"+InputFileNameString[1]
                    RealOutputFileNameTmp = RealOutputFileName
                    Step4_Entry0_String.set(RealOutputFileNameTmp)
                    print(RealOutputFileName)
                    pass
                else:
                    pass

        
                        
                if(os.path.isfile(RealOutputFileNameTmp) == True):
                    #if there are exist file. then ok.
                    
                    OutputFileNameString = os.path.splitext(RealOutputFileNameTmp)
                    for i in range(len(OutputFileNameString)):
                        print(type(OutputFileNameString[i]))
                        print(OutputFileNameString[i])
                    if(RealOutputFileNameTmp == RealInputFileNameTmp):
                        print("RealOutputFileNameTmp == RealInputFileNameTmp")
                        Step6_Label1["text"] = str("        输出文件名不能和输入文件名同名。")
                        ErrorFlag = 32
                    else:
                        print("There are exist same file, so will clear than use it.")
                    pass
                else:
                    try:
                        open(RealOutputFileNameTmp,"w").close()
                        #os.remove(RealOutputFileNameTmp)
                        
                    except:
                        Step6_Label1["text"] = str("        输出文件命名错误。")
                        print("        输出文件命名错误。")
                        ErrorFlag = 31
                    finally:
                        pass
                    #Step4_Label2["text"] = str("        输出文件名错误。")
                    #ErrorFlag = 31
                
            print("Check Step3 = "+str(ErrorFlag))

            #check keyword
            KeyList = []
            if(ErrorFlag != 0):
                pass
            else:
                pass
                KeyString = Step3_Key1_Entry0_String.get()

                KeyList = KeyString.split()
                        
                if(len(KeyList)>0):
                    print(KeyList)
                    pass
                else:
                    Step6_Label1["text"] = str("        关键字输入出错。")
                    print("        关键字输入出错。")
                    ErrorFlag = 41
            print("Check Step4 = "+str(ErrorFlag))


            #process arguments and call process
            #RealInputFileName
            #RealOutputFileName
            #KeyList
            
            if(ErrorFlag != 0):
                pass
            else:
                KeyList = list(set(KeyList))
                print(KeyList)

                batcmdline = "DataFilterProc01.py -f "
                batcmdline += str(RadioGroup.get())
                batcmdline += " -k "
                for i in range(len(KeyList)):
                    batcmdline += KeyList[i]
                    batcmdline += " "
                batcmdline += "-i "+RealInputFileName+" -o "+RealOutputFileName
                print(batcmdline)


                OutputFileNameString = os.path.splitext(RealOutputFileNameTmp)
                print(OutputFileNameString)
                
                batfilename = OutputFileNameString[0]+".bat"
                print(batfilename)
                
                try:
                    batfile = open(batfilename,"w")
                    print("debug1")
                    batfile.write(batcmdline)
                    print("debug2")
                    batfile.close()
                    print("debug3")
                    #os.system(batfilename)
                    Step6_Label1["text"] = "Run OK!"
                    #Step6_Label2["text"] = batcmdline
                    Step6_Label2.delete(1.0,END)
                    print("debug5")
                    Step6_Label2.insert(1.0,batcmdline)
                    print("debug6")
                    cmdout = os.popen(batfilename)

                    #cmdout = os.system(batfilename)
                    
                    print(type(cmdout.read()))
                    print(cmdout.read())
                    
                except:
                    print("Creat batfile error")
                    pass
                finally:
                    os.remove(batfilename)
                    print("Step3_Button1_Function() end.\n")
                    pass
            #setup ok
            
        Step5_Button1 = Button(root,text = "运行",width = 20,command = Step5_Button1_Function)
        Step5_Button1.grid(row = StartRow + 2,column = 3,columnspan = 2,sticky = W)


        #Step6:

        StartRow = 22
        StartCol = 0
        Step6_Label0 = Label(root,text = "Step6:    可能输出一些状态。")
        Step6_Label0.grid(row = StartRow + 0,column = 0,columnspan = ColumnSpanNbr,sticky = W)
        Step6_Label1 = Label(root,text = "        Step0_OK;")
        Step6_Label1.grid(row = StartRow + 1,column = 0,columnspan = ColumnSpanNbr,sticky = W)
        
        #Step6_Label2 = Label(root,text = "        ")
##        Step6_Label2 = Text(root,width = 100,height = 2)
##        Step6_Label2.grid(row = StartRow + 2,column = 0,columnspan = ColumnSpanNbr,sticky = W)
##        

        Step6_Label2 = Text(root,width = 100,height = 2)
        Step6_Label2.grid(row = StartRow + 2,column = 0,columnspan = ColumnSpanNbr,sticky = W)
        Step6_Label2.insert(1.0,"CMDLINE:")
        
        root.mainloop()
    

        
