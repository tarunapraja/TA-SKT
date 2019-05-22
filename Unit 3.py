from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

server = SimpleXMLRPCServer(("0.0.0.0", 5558))

def Emergency_Calls(namaLapor, alamatLapor) :
 client_Pusat = xmlrpc.client.ServerProxy("http://127.0.0.1:5555")
 notif = client_Pusat.laporan(3, namaLapor, alamatLapor)
 if notif == "Laporan diterima":
  return "Berita Tersampaikan"
 else :
  return "Berita Tidak terkirim"

def Notif(namaLapor, alamatLapor) :
 print("Terdapat laporan kebakaran atas nama ",namaLapor," dengan alamat ",alamatLapor)
 return 1

server.register_function(Emergency_Calls, "Emergency_Calls")
server.register_function(Notif, "Notif")
server.serve_forever()