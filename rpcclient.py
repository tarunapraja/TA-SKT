import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:5556")

hasil = client.Emergency_Calls("Taruna Praja", "Malang")

print(hasil)