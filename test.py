#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apk import APK


def test():
    apk_path = "/home/tdoly/com.android.vending_090150.apk"
    apkf = APK(apk_path)
    print apkf.cert_text
    print apkf.file_md5
    print apkf.cert_md5
    print apkf.file_size
    print apkf.androidversion
    print apkf.package
    print apkf.get_android_manifest_xml()
    print apkf.get_android_manifest_axml()
    print apkf.is_valid_APK()
    print apkf.get_filename()
    print apkf.get_package()
    print apkf.get_androidversion_code()
    print apkf.get_androidversion_name()
    print apkf.get_max_sdk_version()
    print apkf.get_min_sdk_version()
    print apkf.get_target_sdk_version()
    print apkf.get_libraries()
    print apkf.get_files()
    # pip install python-magic
    print apkf.get_files_types()
    # print apkf.get_dex()
    print apkf.get_main_activity()
    print apkf.get_activities()
    print apkf.get_services()
    print apkf.get_receivers()
    print apkf.get_providers()
    print apkf.get_permissions()

    # print apkf.show()
    # apkf.parse_icon(icon_path='/tmp')

if __name__ == "__main__":
    test()