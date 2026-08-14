[app]

title = My Calculator
package.name = mycalculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.archs = arm64-v8a
android.api = 35
android.minapi = 24

[buildozer]

log_level = 2
warn_on_root = 1
