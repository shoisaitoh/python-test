# メールアドレスのリストと、フォルダ名とfolder_idのリストをもとに、
# Boxのコラボレータを一括で付与するスクリプト

from box_auth import Box
from boxsdk.object.collaboration import CollaborationRole
import csv

config_file = 'config/hogehoge_comfig.json'
cert_pem_file = 'config/cert.pem'

box = Box(config_file, cert_pem_file)
# ここで認証
auth, client, access_token = box.authorize()

#####
# メールアドレスリストの形式は、
# '1,"testtest1@test.com"'
# '2,"testtest2@test.com"'
# '3,"testtes3@test.com"'
maillist_csv = './data/mailaddress_list.csv'

# フォルダ名リストの一覧は、
# id, folder_name, folder_id(Box), object_type
# '1, 1, xxxxxxxxxxxx, Folder'
folder_list_csv = './data/folder_list.csv'
#####


def main():
    with open(maillist_csv, 'r') as ml:
        ml_reader = csv.reader(ml)
        with open(folder_list_csv) as fl:
            fl_reader = csv.reader(fl)

            # フォルダ番号とフォルダID(URLの後ろのやつ)の辞書をつくる
            # cf. https://www.delftstack.com/ja/howto/python/python-csv-to-dictionary/
            dict_from_csv = {
                rows[1].strip(): int(rows[2])
                for rows in fl_reader
            }
            # print(dict_from_csv)
            for m in ml_reader:
                id = str(m[0]).zfill(3)
                mailaddress = m[1]
                fldr_id = dict_from_csv[id]

                email_of_invitee = mailaddress.strip("'")

                print(f"collabo: {id}, {email_of_invitee}, {fldr_id}")

                # 今回はコラボレーションを「編集者」にしているが、
                # 例えば「ビューアー」で良いのなら、CollaborationRole.VIEWERにする
                collaboration = client.folder(
                    folder_id=fldr_id).collaborate_with_login(
                        email_of_invitee, CollaborationRole.EDITOR)

                collaborator = collaboration.accessible_by
                item = collaboration.item
                c_name = collaborator.name if collaborator.name else "no name"
                if collaboration.status == 'accepted':
                    has_accepted = 'has'
                else:
                    'has not'
                print(
                    ((f'{c_name} {has_accepted} ',
                      f'accepted the collaboration to folder "{item.name}"')))


if __name__ == '__main__':
    main()
