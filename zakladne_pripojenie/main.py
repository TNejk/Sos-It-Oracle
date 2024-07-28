import oracledb

username = 'ADMIN'
password = 'S0s-it-0racle'
tls_string = '(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.eu-frankfurt-1.oraclecloud.com))(connect_data=(service_name=g174432cd8ec6d2_basedatabase_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))'
cursor = None

def connect_to_database():
    print("Pripájam sa do databázy...")
    try:
        connection = oracledb.connect(user=username, password=password, dsn=tls_string)
        print('Pripojil som sa do databázy!')
        cursor = connection.cursor()
        return connection
    except oracledb.Error as error:
        print('Chyba v pripájaní do databázy:', error)
        return None

connect_to_database()