[app]

title = My Calculator

package.name = mycalculator

package.domain = org.mycalculator

source.dir = .

source.include_exts = py,kv,png,jpg,jpeg,atlas

source.exclude_dirs = .buildozer,bin,venv,.git

version = 1.0.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 34

android.minapi = 24

android.ndk = 28c

android.ndk_api = 24

android.archs = arm64-v8a

android.entrypoint = org.kivy.android.PythonActivity

android.permissions =

android.accept_sdk_license = True

android.debug_artifact = apk

log_level = 2


[buildozer]

log_level = 2

warn_on_root = 0
