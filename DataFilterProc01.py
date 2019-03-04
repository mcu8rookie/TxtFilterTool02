#DataFilterProc01.py

import sys

ArgumentsControlVariable = 0    # 0 => arguments come from cmd.
                                # 1 => arguments come from codes.

RoutineControlVariable = 0
"""
OperatorFlag:
0 =》选行。
1 =》删行。
2 =》截出0。
3 =》截出1。
4 =》截断0。
5 =》截断1。
"""

OperatorFlag = 0
KeyList = ["a;skdjf","asdf","sdf","1234"]
InputFileName = "temp1.txt"
OutputFileName = "output.txt"

ErrorFlag = 0

if __name__ == "__main__":
        print("PytyonScript: "+str(sys.argv[0]))
        argvnbr = len(sys.argv)
        print(argvnbr)

##        for i in range(argvnbr):
##                print(sys.argv[i])
##                
        for i in range(len(sys.argv)):
                print("Argument["+str(i)+"]: "+sys.argv[i])
        if(ArgumentsControlVariable == 0):
        
                argvnbrtmp = 1
                OperatorFlag = 0
                KeyList = []
                InputFileName = ""
                OutputFileName = ""
                for i in range(argvnbrtmp,len(sys.argv)):
                        if(sys.argv[i] == "-f"):
                                OperatorFlag = int(sys.argv[i+1])
                                i+=2
                        elif(sys.argv[i] == "-k"):
                                for j in range(i+1,len(sys.argv)):
                                        #print("j = "+str(j))
                                        if(sys.argv[j] != "-i"):
                                                KeyList.append(sys.argv[j])
                                                #print(KeyList)
                                        else:
                                                i = j
                                                break
                        elif(sys.argv[i] == "-i"):
                                InputFileName = sys.argv[i+1]
                                #print(InputFileName)
                                i+=2
                                pass
                        elif(sys.argv[i] == "-o"):
                                OutputFileName = sys.argv[i+1]
                                i+=2
                                if(i == len(sys.argv)):
                                        print("Arguments process ok")
                                else:
                                        ErrorFlag = 11
                                        print("Arguments process error1.");
                
                        else:
                                pass
                else:
                        pass
        if(ErrorFlag != 0):
                print("ErrorFlag = "+str(ErrorFlag))
        else:
                print("Four pars")
                print(OperatorFlag)
                print(KeyList)
                print(InputFileName)
                print(OutputFileName)


        #process
        if(ErrorFlag == 0):
        
                try:
                        inputfile = open(InputFileName,"r")
                        outputfile = open(OutputFileName,"w")
                except:
                        inputfile.close()
                        outputfile.close()
                        ErrorFlag = 21
                        pass
                finally:
                        
                        pass

                ##
                ##process start
                def op_key_str(op=0,keylist=[],txt=""):
                    ErrorFlag = 0
                    txtlen = 0
                    keylen = 0
                    txtindex1 = 0
                    txtindex2 = 0
                    findflag = 0
                    
                    if(op<0 or op>5):
                            print("op_key_str() argument op error:op = "+str(op))
                            ErrorFlag = 11
                            return None
                    elif(len(keylist)<1):
                            print("op_key_str() argument keylist error:len(keylist) = "+str(len(keylist)))
                            ErrorFlag = 12
                            return None
                    elif(len(txt)<1):
                            print("op_key_str() argument txt error:len(txt) = "+str(len(txt)))
                            ErrorFlag = 13
                            return None
                    else:
                        
                        pass

                    if(ErrorFlag != 0):
                        pass
                    else:
                        
                        for strlt in keylist:
                            print(strlt)
                            txtlen = len(txt)
                            keylen = len(strlt)
                            txtindex1 = txt.find(strlt)
                            print(txt)
                            print(strlt)
                            print("txtindex1 = "+str(txtindex1))
                            if(txtindex1 != -1):
                                if(txtindex1 <= txtlen-keylen):
                                    findflag = 1
                                    break
                                    pass
                                else:
                                    print("check ok but beyond title length.")
                            else:
                                pass

                        if(findflag != 0):
                            if(op == 0):#选行
                                return txt
                                pass
                            elif(op == 1):#删行
                                return None
                                pass
                            elif(op == 2):#截出0
                                return txt[txtindex1+keylen:]
                                pass
                            elif(op == 3):#截出1
                                return txt[txtindex1:]
                                pass
                            elif(op == 4):#截断0
                                return txt[:txtindex1]+"\n"
                                pass
                            elif(op == 5):#截断1
                                return txt[:txtindex1+keylen]+"\n"
                                pass
                        else:
                            if(op == 0):#选行
                                return None
                                pass
                            elif(op == 1):#删行
                                return txt
                                pass
                            elif(op == 2):#截出0
                                return None
                                pass
                            elif(op == 3):#截出1
                                return None
                                pass
                            elif(op == 4):#截断0
                                return txt
                                pass
                            elif(op == 5):#截断1
                                return txt
                                pass
                            pass

                ##process end
                
                if(ErrorFlag == 0):
                        
                        linelen = 0
                        linenbr = 0
                        readednbr = 0
                        lineindex1= 0
                        lineindex2 = 0
                        linenew = ""
                        
                        linestr = inputfile.readline()
                        #outputfile.write(linestr)
                        print("Debug1:"+linestr)
                        linenew = op_key_str(OperatorFlag,KeyList,linestr)
                        if(linenew == None):
                                pass
                        else:
                                print("Debug2:"+linenew)
                                outputfile.write(linenew)
                        while(len(linestr) > 0):
                                linestr = inputfile.readline()
                                #outputfile.write(linestr)
                                print("Debug1:"+linestr)
                                linenew = op_key_str(OperatorFlag,KeyList,linestr)
                                if(linenew == None):
                                        pass
                                else:
                                        print("Debug2:"+linenew)
                                        outputfile.write(linenew)

                        inputfile.close()
                        outputfile.close()
                else:
                        print("ErrorFlag = "+str(ErrorFlag))
                        pass
        else:
                pass

        
        
