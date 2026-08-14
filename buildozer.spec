[app]

title = My Calculator
package.name = mycalculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.api = 34
android.minapi = 24
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
