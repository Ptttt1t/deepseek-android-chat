# buildozer.spec file for DeepSeek Android Chat App

[app]
title = DeepSeek Chat App
package.name = deepseekchatapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,kv,txt,md
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
# Ensure network access
android.permissions = INTERNET

[buildozer]
log_level = 2
