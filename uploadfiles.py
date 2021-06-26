import os
import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root,filename)
            
        
        relative_path=os.path.relpath(local_path,file_from)
        dropbox_path=os.path.join(file_to,relative_path)

        f=open(file_from,'rb')
        dbx.files.upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
        
def main():
    access_token='WMznpqg0jXYAAAAAAAAAAWUyabfd0s7wfL7zeUBVD5VjcTXI7QLJI65HPSvDAMQ9'
    transferdata=TransferData(access_token)

    file_from=input("Enter a file path to transfer=")
    # to give path for dropbox give  /foldername/filename
    file_to=input("Enter the file path to upload the file to the dropbox")

    transferdata.upload_file(file_from,file_to)
    print("file has been moved")

main()

