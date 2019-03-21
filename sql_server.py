
import pyodbc 
import sys
host = ""
port = ""

database = ""
username = ""
password = ""

args = sys.argv[1:]
if (len(args)==0):
        print("SQL Server Remote By Kevin Agusto\nsql_server -h or --help")
        sys.exit(0)
for i in range(len(args)):
        try:
                if (args[i]=="--help" or args[i]=="-h"):
                        print("""
                        SQL Server Remote By Kevin Agusto
                        
                        -p port
                        -s server host
                        -d data base name (default empty)
                        -u username
                        -pw password
                        
                        """)
                        sys.exit(0)
                if (args[i]=="-p" or args[i] =="--port"):
                        port = args[i+1]
                        i+=2
                
                if (args[i]=="-s" or args[i] =="--server"):
                        host = args[i+1]
                        i+=2
        
                if (args[i]=="-d" or args[i] =="--database"):
                        database = args[i+1]
                        i+=2        
                if (args[i]=="-u" or args[i] =="--username"):
                        username = args[i+1]
                        i+=2        
        
                if (args[i]=="-pw" or args[i] =="--password"):
                        password = args[i+1]
                        i+=2 
        except IndexError:
                break

if (host==""):
        print("Server Host Cannot Empty")
        sys.exit(0)

if (port==""):
        print("Port Cannot Empty")
        sys.exit(0)

if (username==""):
        print("Username Cannot Empty")
        sys.exit(0)
        
        
server = '%s,%s'%(host, port)        
                
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()
#cursor.execute("""
#select * from sys.databases WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');
#""") 

def Run(order):    
        try:
                data_base = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD='+ password)
        except:
                print("database connection error")
                sys.exit(0)
                
        cur = data_base.cursor()
        if (database==""):
                cur.execute("use %s"%(database))
        try:
                cur.execute(order)

                hasil = []
                for i in cur.fetchall():
                        hasil.append(i)
                #hasil.sort()
                data_base.commit()
                data_base.close()
                return hasil
        except pyodbc.ProgrammingError as error:
                return [error]        
while True:        
        try:
                masuk = input("SQL> ")
                if (masuk==""):
                        print("Please type input")
                        continue
                if masuk=="exit":
                        print("Bye - Kevin Agusto")
                        break
                for i in Run(masuk):
                        print (i)
        except KeyboardInterrupt:
                print("Bye...")
                sys.exit(0)
