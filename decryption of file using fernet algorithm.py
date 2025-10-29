from cryptography.fernet import Fernet

def decrypt_file(encrypted_file,output_file,key_file):
    try:
        with open(key_file,"rb") as kf:
            #write the encryption key into the key file
            key = kf.read()
            cipher = Fernet(key)
            #encrypt the file
            with open(encrypted_file,"rb") as ef:
                encrypted_data = ef.read()
              #encrypt the file using the cipher object  
            decrypted_data = cipher.decrypt(encrypted_data)

            #open the output_file
            with open(output_file,"wb") as ef:
                #write the encrypted data to the output file
                ef.write(decrypted_data)
            print(f"decryption completed  and file saved as {output_file} ")
    except FileNotFoundError:
        print("Error : input file not found Maybe spelling mistake")
    except PermissionError:
        print("Permission Denied")
    except Exception as e:
        print("something went wrong ",e)
      decrypt_file("user_data_enccrypted.txt","plain.txt","secret.key")
