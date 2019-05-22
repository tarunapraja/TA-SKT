# import library xmlrpc server
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


# Buat instance xml rpc server
server = SimpleXMLRPCServer( ("0.0.0.0", 5555) )
unit1 = xmlrpc.client.ServerProxy("http://127.0.0.1:5556")
unit2 = xmlrpc.client.ServerProxy("http://127.0.0.1:5557")
unit3 = xmlrpc.client.ServerProxy("http://127.0.0.1:5558")

# Definisikan fungsi untuk melakukan pendataan laporan
def laporan(server, namaLapor, alamatLapor):
 print("Terdapat laporan kebakaran atas nama ",namaLapor," dengan alamat ",alamatLapor)
 
# Broadcast
 if server == 1 :
  RUnit2 = unit2.Notif(namaLapor, alamatLapor)
  RUnit3 = unit3.Notif(namaLapor, alamatLapor)
 elif server == 2 :
  RUnit1 = unit1.Notif(namaLapor, alamatLapor)
  RUnit3 = unit3.Notif(namaLapor, alamatLapor)
 elif server == 3 :
  RUnit1 = unit1.Notif(namaLapor, alamatLapor)
  RUnit2 = unit2.Notif(namaLapor, alamatLapor)

 print("Laporan berhasil disampaikan ke seluruh unit")
 return "Laporan diterima"
 
# Register fungsinya
server.register_function(laporan, "laporan")

# Jalankan servernya
server.serve_forever()
