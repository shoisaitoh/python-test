from boxsdk import JWTAuth, Client
import json
import glob
import os
import datetime


class Box:
    # 入力情報の初期化
    def __init__(self, config_file, cert_pem_file):
        self.config_file = config_file
        self.cert_pem_file = cert_pem_file
        self.tt = datetime.datetime.now().strftime('%Y_%m%d_%H%M_%S')
        self.log_file = 'log/log_{}.txt'.format(self.tt)

    # 認証
    def authorize(self):
        json_data = open(self.config_file, 'r')
        box_config = json.load(json_data)

        auth = self.set_auth(box_config)

        access_token = self.get_access_token(auth)

        client = self.get_service_account_client(auth)

        return auth, client, access_token

    # 認証情報をconfigから読み込み
    def set_auth(self, box_config):
        auth = JWTAuth(
            client_id=box_config['boxAppSettings']['clientID'],
            client_secret=box_config['boxAppSettings']['clientSecret'],
            enterprise_id=box_config['enterpriseID'],
            jwt_key_id=box_config['boxAppSettings']['appAuth']['publicKeyID'],
            rsa_private_key_file_sys_path=self.cert_pem_file,
            rsa_private_key_passphrase=box_config['boxAppSettings']['appAuth']
            ['passphrase'],
        )

        return auth

    def get_access_token(self, auth):
        access_token = auth.authenticate_instance()
        return access_token

    def get_service_account_client(self, auth):
        service_account_client = Client(auth)
        return service_account_client

    def get_service_account_id(self, client):
        service_account = client.user().get()
        return service_account.id

    def set_target_folder(self, client, target_folder_id):
        target_folder = client.folder(
            folder_id=target_folder_id)  # なぜかエラーが返らないので注意
        return target_folder

    def upload_file(self, folder, file):
        try:
            file_uploaded = folder.upload(file, preflight_check=True)
            print("create file:", file_uploaded)
            return file_uploaded
        except Exception:
            print("File copy error.")
            print("  parent_folder:", folder)
            print("  fileth:", file)
            print("  continue")
            with open(self.log_file, 'a') as f:
                f.write("File copy error.\n")
                f.write("    parent_folder: {}\n".format(folder))
                f.write("    filepath: {}\n".format(file))
            return None

    def create_subfolder_inside_target(self, client, folder_id,
                                       subfolder_name):
        try:
            subfolder = client.folder(folder_id).create_subfolder(
                subfolder_name)
            print("create folder:", subfolder)
            return subfolder
        except Exception:
            with open(self.log_file, 'a') as f:
                f.write("Directory creation error: {} / {}\n".format(
                    folder_id, subfolder_name))
            return None

    def copy_folders_and_files(self, client, filelist, path, parent_folder):
        for filepath in filelist:
            base_name = os.path.basename(filepath)

            if os.path.exists(filepath) & os.path.isdir(filepath):
                subfolder_root = self.create_subfolder_inside_target(
                    client, parent_folder.id, base_name)

                new_path = path.replace('*', '{}/*'.format(base_name))
                filelist = glob.glob(new_path)

                if len(filelist) > 0:
                    self.copy_folders_and_files(client, filelist, new_path,
                                                subfolder_root)

            elif os.path.exists(filepath) & os.path.isfile(filepath):
                self.upload_file(parent_folder, filepath)

            else:
                print("not a folder/file")
                with open(self.log_file, 'a') as f:
                    f.write("No file error.\n")
                    f.write("    parent_folder: {}\n".format(parent_folder))
                    f.write("    filepath: {}\n".format(filepath))

    def file_search(self, client, query_str, limit_count, file_ext):
        items = client.search().query(query='"{}"'.format(query_str),
                                      limit=limit_count,
                                      file_extensions=file_ext,
                                      type='folder')
        for item in items:
            print(item)


if __name__ == '__main__':
    config_json = 'config/hogehoge_config.json'
    cert_pem = 'config/cert.pem'
    box = Box(f'{config_json}', f'{cert_pem}')

    auth, client, access_token = box.authorize()
