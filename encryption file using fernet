#import the fernet class from cryptography
from cryptography.fernet import Fernet

def encrypt_file(input_file,output_file,key_file):
    try:
        #generate a random encryption key
        key = Fernet.generate_key()
        #open the key file in binary mode
        with open(key_file,"wb") as kf:
            #write the encryption key into the key file
            kf.write(key)
            #create  a fernet object using the generated key
            # library that is used to perform symmetric encryption
            cipher = Fernet(key)
            #encrypt the file
            with open(input_file,"rb") as f:
                data = f.read()
              #encrypt the file using the cipher object  
            encrypted_data = cipher.encrypt(data)

            #open the output_file
            with open(output_file,"wb") as ef:
                #write the encrypted data to the output file
                ef.write(encrypted_data)
            print(f"Encryption completed  and file saved as {output_file} ")
    except FileNotFoundError:
        print("Error : input file not found Maybe spelling mistake")
    except PermissionError:
        print("Permission Denied")
    except Exception as e:
        print("something went wrong ",e)
with open("user_data.txt" ,"w") as f:
    f.write("Sensitive Data -- \n ")
    f.write("Username : user@123 \n")
    f.write("Password : admin@1122 \n")
    f.write("email : email@example.com \n")
    f.write("Data")
encrypt_file("user_data.txt","user_data_enccrypted.txt","secret.key")
