# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\JoseCarlosAlvarez\\Documents\\Fall2019\\DigImageProcessing\\FInal-MedImg\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\JoseCarlosAlvarez\\Documents\\Fall2019\\DigImageProcessing\\FInal-MedImg\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\josecarlosalvarez\\documents\\fall2019\\digimageprocessing\\project-final\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\JoseCarlosAlvarez\\Documents\\Fall2019\\DigImageProcessing\\FInal-MedImg\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Medical Imaging Final-Project',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\JoseCarlosAlvarez\\Documents\\Fall2019\\DigImageProcessing\\FInal-MedImg\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='Medical Imaging Final-Project')
