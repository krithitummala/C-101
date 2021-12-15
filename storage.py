import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)
    
def main():
    access_token = 'lapQfi6LQGMAAAAAAAAAAXz3_OTfC6NxJ70TNaWBkW0FA-WFypXFq1sh-RNg5zg4'
    transferData = TransferData(access_token)

    file_to = input("Enter the file destination")
    file_from = input("Enter the file path for tranfer")
    transferData.upload_file(file_from, file_to)

main()