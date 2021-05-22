import sqlite3


class Simple_sql:
    '''this program used sqlite3 module
    for simple todo databace makeing
    '''
    def __init__(self,databace_name):
        '''ramamiters like : Simple_sql(databace_name = "my_databace.db")
        databace_name is given string value
        '''
        self.databace =sqlite3.connect(databace_name)
        

    def new_table(self,table_name,column_names):
        '''this method for create new table 
        paramiters : new_table(table_name = "my_table_name",column_names = ("id int","name text","midel_name text","last_name text"))
        table_name is given string value
        column_names is given string values in tupel like ("id int","name text","midel_name text","last_name text")
        id,name,midel_name,last_name is column names and int,text is type of values
        '''

        self.table_name = table_name
        self.column_names = str(column_names).replace("'","")
        self.new_table_command ="create table " + self.table_name + self.column_names
        self.databace.execute(self.new_table_command)

    def insert_row(self,table_name,data):
        '''this method for create new row 
        paramiters : insert_row(table_name = "my_table_name",data = ("1","saurabh","anil","wadekar"))
        table_name is given string value
        data is given string values in tupel like ("1","saurabh","anil","wadekar")
        '''
        self.table_info = self.databace.execute(f"PRAGMA table_info({table_name})")
        names = []
        for i in self.table_info:
            names.append(i[1])
        self.row_names = str(tuple(names)).replace("'","")
        self.insert_row_command = "insert into "+str(table_name)+" "+ self.row_names +" "+" values "+str(data).replace('"',"'")
        self.databace.execute(self.insert_row_command)
        self.databace.commit()
        
    def get_one(self,table_name):
        '''this method for get first row in tabele
        paramiters : get_one(table_name = "my_table_name")
        table_name is given string value
        '''
        get_all_command = f"select * from {table_name}"
        all_data = self.databace.execute(get_all_command).fetchone()
        return all_data
    
    def get_all(self,table_name):
        '''this method for get all row in tabele
        paramiters : get_all(table_name = "my_table_name")
        table_name is given string value
        '''
        get_all_command = f"select * from {table_name}"
        all_data = self.databace.execute(get_all_command).fetchall()
        return all_data

    def get_data(self,table_name,columns_names):
        '''this method for get specific columns data 
        paramiters : get_data(table_name = "my_table_name",columns_names = ("name","last_name"))
        table_name is given string value
        columns_names is given string values in tupel like ("name","last_name")
        '''
        get_data_command = f"select {str(columns_names)} from {table_name}".replace("'","").replace('"',"").replace(")","").replace("(","")
        get_data = self.databace.execute(get_data_command).fetchall()
        print(get_data_command)
        return get_data
    
    def delete_row(self,table_name,where_column):
        '''this method for delete specific row 
        paramiters : delete_row(table_name = "my_table_name",where_column = ("id","1"))
        table_name is given string value
        where_column is given string values in tupel like ("id","1")
        id is column name and 1 is id a row for delete specific row
        '''
        delete_command = f"delete from {table_name} where {str(where_column[0])} = {str(where_column[1])}"
        self.databace.execute(delete_command)
        self.databace.commit()
    
    def update(self,table_name,data,where_column):
        '''this method for update specific row 
        paramiters : update(table_name = "my_table_name",data = {"name":"rahul","last_name":"dravid"},where_column = ("id","1"))
        table_name is given string value
        data is given dictionary key is column name and value is value like {"name":"rahul","last_name":"dravid"}
        where_column is given string values in tupel like ("id","1")
        id is column name and 1 is id a row for update specific row
        '''
        command_str = ""
        keys = data
        for i in keys:
            command_str = command_str + str(i) + " = '"+str(data[i])+"'," 

        command_str_new = command_str[0:len(command_str)-1]
        command = f"update {table_name} set {command_str_new} where {where_column[0]} = {where_column[1]}"
        
        print(command)
        self.databace.execute(command)
        self.databace.commit()
        
    def find_rows(self,table_name,identity_column,value):
        self.find_command = f"select * from {str(table_name)} where {str(identy_column)}='{str(value)}'"
        self.find_data = self.databace.execute(self.find_command).fetchall()
        return self.find_data

    def exe(self,sql_command):
        '''this method for execute any SQL command
        sql_command is given string value like search_row("select * from my_table")
        string value is SQL command
        '''
        data = self.databace.execute(sql_command).fetchall()
        self.databace.commit()
        return data

    def replace_all(self,my_str,my_list,re_char):
        self.my_str = my_str
        self.my_list = my_list
        for i in self.my_list:
            self.my_str = self.my_str.replace(str(i),str(re_char))
        return self.my_str
        
    


        