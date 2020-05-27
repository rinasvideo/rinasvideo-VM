
import winsound as ws
import tarfile
import xcode
import pyminizip
import os
import shutil
import subprocess
import time
import sys
import gc
import tempfile
import warnings
import glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))
basepath=os.getcwd()
tempdir=tempfile.TemporaryDirectory()
tempname=tempdir.name
os.makedirs("./inputpack", exist_ok=True)
warnings.simplefilter('ignore')
def unpack(tempname):
    print('')
    print(' パッケージのインストール中しばらくお待ちください')
    tempname1=tempname+"\\"+"pack"
    plaintext="rinasvideo"
    pass2=xcode.xencode(plaintext)
    name=".\\inputpack\\pack.dec"
    c=os.path.isfile(name)
    if c==1:
        pyminizip.uncompress(name.encode('cp932'),pass2,".\\",0)
        with tarfile.open('./pack.tar', 'r:*') as tar:
            tar.extractall(tempname1)
        os.remove('./pack.tar')
        ws.Beep(494,100)
        time.sleep(0.1)
        ws.Beep(494,100)
    else:
        print(' パッケージが見つかりませんでした。')
        ws.Beep(494,1000)
        time.sleep(0.1)
        ws.Beep(523,1000)
        time.sleep(5)
ver="0"
e=" rinasvideoソフトウェアランチャー(統合版)"
unpack(tempname)

while True:
    tempname1=tempname+"\\"+"pack\\"
    os.system('cls')
    print('')
    print(e)
    print('')
    print(' 0:ファイル暗号圧縮プログラム')
    print('')
    print(' 1:ファイル暗号解除プログラム')
    print('')
    print(' 2:バッテリー充電通知プログラム')
    print('')
    print(' 3:フォルダコピープログラム')
    print('')
    print(' 4:パッケージのインストール')
    print('')
    print(' 5:拡張プログラム')
    print('')
    print(' 6:プログラムの終了')
    print('')
    print(' 7:アプリケーション一覧')
    print('')
    a=input(' 上記のアプリケーションから選択してください　(0～) >> ')
    try:
        a=int(a)
    except ValueError:
        a=-3
    if a==7:
        os.system('cls')
        print('')
        tempfile1=tempname+"\\"+"pack/"+"app-pack/*"
        [print(i) for i in glob.glob(tempfile1)]
        #print(glob.glob(tempfile1))
        print('')
        print('これが現在のインストール済みパッケージです。')
        print('')
        input('メニューに戻るにはエンターキーを押してください')
        continue
    if a==6:
        print(' 終了処理中...')
        time.sleep(5)
        tempdir.cleanup()
        gc.collect()
        sys.exit()
    if a==4:
        unpack(tempname)
        a=-4
    if a==5:
        app1=input(' 拡張プログラム名　>> ')
        app=tempname1+"app-pack/"+app1
        c=os.path.isfile(app)
        if c==True:
            a==4
        else:
            a=-3
    print(' プログラムの起動中...')
    if a==3:
        c=os.path.isfile(tempname1+"app-pack/copy-file.exe")
        if c==True:
            app=tempname1+"app-pack/copy-file.exe"
        else:
            a=-3
    if a==0:
        c=os.path.isfile(tempname1+"app-pack/dec2.exe")
        if c==True:
            app=tempname1+"app-pack/dec2.exe"
        else:
            a=-3
    if a==1:
        c=os.path.isfile(tempname1+"app-pack/Decypher.exe")
        if c==True:
            ar=input(' 引数１　decファイルフルパス >> ')
            pas=input(' パスワード　>>')
            app=tempname1+"app-pack/Decypher.exe"+" "+ar+" "+pas
        else:
            a=-3
    if a==2:
        c=os.path.isfile(tempname1+"app-pack/sequencer.exe")
        if c==True:
            app=tempname1+"app-pack/sequencer.exe"
        else:
            a=-3
    if a!=-3 and a!=-4:
        try:
            os.system('cls')
            ps = subprocess.call(app)
        except KeyboardInterrupt:
            pass
        except OSError:
            e="有効なアプリケーションではありません。"
            a=-1
        else:
            a=""
            app=""
            c=0
            e=" rinasvideoソフトウェアランチャー(統合版)"
        continue
    if a==-3:
        e=' エラー！：アプリケーションが見つかりませんでした。\n パッケージを再インストールしてください'
    else:
        e=""