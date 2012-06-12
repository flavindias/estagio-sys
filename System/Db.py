import MySQLdb

connection = MySQLdb.connect(host="db4free.net", db="estagiosys", user="desenvolvedor1", passwd="Acesso")
cursor = connection.cursor()
