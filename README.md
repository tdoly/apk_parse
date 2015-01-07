## 解析APK

   选取[androguard][https://github.com/androguard/androguard]中部分对apk分析的代码进行修改,满足自己使用的需求.


```python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from apk import APK
    
    
    def test():
        apk_path = "/home/tdoly/topitme.apk"
        apkf = APK(apk_path)
        print apkf.cert_text
        print apkf.file_md5
        print apkf.cert_md5
        print apkf.file_size
        print apkf.androidversion
        print apkf.get_min_sdk_version()
        print apkf.package
    
    if __name__ == "__main__":
        test()
    
```
