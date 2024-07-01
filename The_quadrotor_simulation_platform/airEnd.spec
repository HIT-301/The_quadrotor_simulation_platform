# -*- mode: python ; coding: utf-8 -*-


# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['airEnd.py'],
    pathex=[],
    binaries=[],
    datas=[('./static','static')],
    hiddenimports=['pymysql', 'gevent', 'geventwebsocket', 'gevent.ssl', 'gevent.builtins', 'engineio.async_drivers.threading'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='airEnd',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
