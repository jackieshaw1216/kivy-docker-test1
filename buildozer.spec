[app]

# (str) Title of your application
title = Your App Title

# (str) Package name
package.name = yourappname

# (str) Package domain (com.example.yourapp)
package.domain = com.example.yourapp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (relative to source.dir)
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (list) Version requirements (python3, kivy, etc.)
requirements = python3,kivy

# (str) Presplash file (image)
# presplash.filename = %(source.dir)s/presplash.png

# (str) Icon file
# icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version (recommend 25b or 26c)
android.ndk = 25b

# (str) Android Gradle plugin version (match with gradle version)
android.gradle_plugin_version = 7.4.2

# (str) Gradle version (must match plugin)
android.gradle_version = 7.4.2

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (str) Gradle repository (optional, use mirror if needed)
android.gradle_repository = https://mirrors.cloud.tencent.com/gradle/

# (bool) Enable or disable the Android debug mode
android.debug = True

# (list) Android logcat filters to log
android.logcat_filters = *:S python:D

# (str) Android NDK directory (if you want to force a specific path)
# android.ndk_path = 

# (str) Android SDK directory (if you want to force a specific path)
# android.sdk_path = 

# (list) Java classes to add to the project
# android.add_src =

# (list) Java jar files to add
# android.add_jar =

# (list) AAR files to add
# android.add_aar =

# (list) Javascript files to add
# android.add_javascript =

# (list) Metadata files to add
# android.add_metadata =

# (list) Activity classes to add
# android.add_activity =

# (list) Android service classes to add
# android.add_service =

# (list) Android broadcast receiver classes to add
# android.add_broadcast_receiver =

# (list) Android intent filters for the main activity
# android.intent_filters =

# (str) Meta-data to add to the application
# android.meta_data =

# (str) Target Android ABI (armeabi-v7a, arm64-v8a, x86, x86_64)
android.archs = armeabi-v7a, arm64-v8a

# (bool) Enable or disable the use of the Android SDK's build-tools
android.use_build_tools = True

# (bool) Sign the APK (debug keystore will be used if False)
android.sign = False

# (str) Keystore path (if signing)
# android.keystore =

# (str) Keystore alias (if signing)
# android.keystore_alias =

# (str) Keystore password (if signing)
# android.keystore_password =

# (str) Key password (if signing)
# android.key_password =

# (bool) Enable or disable the use of the AndroidX libraries
android.use_androidx = True

# (bool) Enable or disable the use of the legacy support library
android.use_support_library = False

# (str) Python for Android branch
p4a.branch = master

# (str) Python for Android directory (if you want to use a local version)
# p4a.source_dir =

# (str) Python for android extra arguments
p4a.extra_args = --debug

# (bool) Enable or disable the splash screen
# splash.enabled = False

# (str) Splash screen image
# splash.image =

# (str) Splash screen scaling
# splash.scale =

# (str) Splash screen color
# splash.color =

# (list) Services to start automatically
# services =

# (list) Permissions that are not standard Android permissions but are used
# android.extra_permissions =

# (str) Fullscreen mode (immersive)
# android.immersive_mode = False

# (str) Window background color (hex)
# android.window_background_color = #000000

# (str) Screen resolution (e.g., small, normal, large)
# android.screen_resolution = normal

# (list) Supported devices (e.g., phone, television)
# android.device_features =

# (list) Android UI options
# android.ui_options =

# (str) Android log level (e.g., info, debug, error)
# android.log_level = info

# (int) NDK API level (minimum supported Android version)
android.ndk_api = 21

# (bool) Enable or disable the use of the legacy Apache HTTP client
android.use_legacy_apache_http = False

# (str) Android RTC (Real Time Clock) permission
# android.rtc = False

# (list) Android libraries to include (e.g., 'x86', 'armeabi-v7a')
# android.add_libs =

# (list) Android assets to include
# android.add_assets =

# (str) Python architecture (e.g., 'armeabi-v7a', 'arm64-v8a')
# android.python_arch =

# (bool) Enable or disable the use of the Android SDK's platform tools
android.use_platform_tools = True

# (bool) Enable or disable the use of the Android SDK's cmake
android.use_cmake = False

# (str) CMake version (if used)
# android.cmake_version =

# (str) Android packaging mode (e.g., 'aab', 'apk')
android.package_mode = debug

# (bool) Enable or disable the use of the Android SDK's build-tools 30+
android.use_build_tools_30 = True

# (str) Android debugger (e.g., 'pdb', 'pydevd')
# android.debugger =

# (bool) Enable or disable the use of the Android SDK's emulator
# android.use_emulator = False

# (str) Emulator system image (if used)
# android.emulator_image =

# (str) Emulator ABI (if used)
# android.emulator_abi =

# (str) Emulator skin (if used)
# android.emulator_skin =

# (list) Emulator extra args
# android.emulator_extra_args =

# (bool) Enable or disable the use of the Android SDK's fastboot
# android.use_fastboot = False

# (str) Fastboot device (if used)
# android.fastboot_device =

# (list) Fastboot extra args
# android.fastboot_extra_args =

# (str) Android ADB device (if used)
# android.adb_device =

# (list) ADB extra args
# android.adb_extra_args =

# (str) Android SDK manager extra args
# android.sdk_manager_extra_args =

# (str) NDK extra args
# android.ndk_extra_args =

# (str) Gradle extra args
# android.gradle_extra_args =

# (str) Android manifest file (if you want to provide your own)
# android.manifest_file =

# (str) Android manifest template (if you want to customize)
# android.manifest_template =

# (list) Android meta-data for the application
# android.meta_data =

# (list) Android intent filters for activities
# android.intent_filters =

# (list) Android libraries (e.g., 'x86', 'armeabi-v7a')
# android.libs =

# (str) Android p4a requirements
# p4a.requirements = python3,kivy

# (str) Python for Android bootstrap (sdl2, webview, service_only)
p4a.bootstrap = sdl2

# (str) Python for Android dist name
# p4a.dist_name =

# (str) Python for Android dist directory
# p4a.dist_dir =

# (bool) Enable or disable the use of the Android SDK's local maven repository
# android.use_local_maven_repo = False

# (str) Local maven repository path
# android.local_maven_repo =

# (bool) Enable or disable the use of the Android SDK's google maven repository
# android.use_google_maven_repo = True

# (str) Android NDK version to use (overrides android.ndk)
# android.ndk_version =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to buildozer's global directory (where it caches packages)
# buildozer_dir = ~/.buildozer

# (bool) WARNING: do not share the APK with others until you read about signing
# buildozer.allow_unsafe_apk = False

# (list) Patterns to exclude from the project directory (gitignore syntax)
buildozer.exclude_dirs = .git, .github, __pycache__, bin, .buildozer

# (list) Patterns to exclude from the source directory (gitignore syntax)
buildozer.exclude_patterns = .gitignore, .pyc, .pyo, *.py[cod]

# (bool) WARNING: This may lead to unwanted side effects
# buildozer.force = False
