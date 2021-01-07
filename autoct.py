#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
File:autoct.py
Author:T
Description:キャプチャ自動ツール
-----------------------------------------------
〔変更履歴〕
2020/09/26 T 新規作成
"""
import pyautogui
import pathlib

def mkdir(dir_path):
    """
    ディレクトリが存在しない場合作成
    Parameters
    ----------
    dir_path : WindowsPath
        対象のパス
    """
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
def get_change_orgpath(basis_path,bfname='',afname='',bfdir='',afdir=''):
    """
    パス名変更関数
    Parameters
    ----------
    basis_path : WindowsPath
        対象のパス
    bfname : String
        ファイル名(変更前)
    afname : String
        ファイル名(変更後)
    bfdir : String
        ディレクトリ名(変更前)
    afdir : String
        ディレクトリ名(変更後)
    Returns
    -------
    orgpath : WindowsPath
        対象のパス(変更後)
    """
    pname = str(basis_path.name).replace(bfname,afname)# 1.ファイル名変更
    pdir = str(basis_path.parent).replace(bfdir, afdir)# 2.ディレクトリ変更
    orgpath = pathlib.Path(pdir).joinpath(pname)# 3.パスの作成
    return orgpath
try:
    while True:
        print('保存したいファイル名を入力してください (Ctrl+C : 終了)')
        fname = input('>> ')
        fname_dir=pathlib.Path('dir/' + fname)
        mkdir(fname_dir)
        for i in range(3):
            print(3-i)
            pyautogui.sleep(1) # 1秒停止
        print("Capture OK")
        pyautogui.screenshot('dir/' + fname + '/Chrome.png')
except KeyboardInterrupt:
    print('\n終了')

