# -*- mode: python ; coding: utf-8 -*-

from PyQt5 import QtCore
import os

block_cipher = None

# Chemin vers les plugins Qt (ex: platforms)
qt_plugins_path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath)

a = Analysis(
    ['Kha_Task.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icon.ico', '.'),
        ('background.png', '.'),
        (os.path.join(qt_plugins_path, 'platforms'), 'PyQt5/Qt/plugins/platforms'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Kha_Task',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
)

app = BUNDLE(
    exe,
    name='Kha_Task.app',
    icon='icon.ico',
    bundle_identifier='com.yourcompany.todoapp',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSUIElement': 'False',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
    },
)
