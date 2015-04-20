## APK parse

   reference [androguard][androguard-url].

   
[androguard-url]: https://github.com/androguard/androguard

## Example:

```

    apkf = APK("myfile.apk")
    apkf = APK(read("myfile.apk"), raw=True)
```

### package

Return the name of the package

```

    >>> apkf.package
    com.android.vending

    >>> apkf.get_package()
    com.android.vending
```

### file_md5

Return the file md5 of the apk

```

    >>> apkf.file_md5
    40bdd920a3a3d2acf432e3c5b485eb11
```

### cert_md5

Return the cert md5 of the apk

```

    >>> apkf.cert_md5
    cde9f6208d672b54b1dacc0b7029f5eb
```

### file_size

Return the apk file size

```

    >>> apkf.file_size
    11194863
```

### androidversion

Return the apk version

```

    >>> apkf.androidversion
    {'Code': u'80341200', 'Name': u'5.4.12'}
```

### get_androidversion_code()

Return the android version code

```

    >>> apkf.get_androidversion_code()
    80341200
```

### get_androidversion_name()

Return the android version name

```

    >>> apkf.get_androidversion_name()
    5.4.12
```


### get_min_sdk_version()

Return the android:minSdkVersion attribute

```

    >>> apkf.get_min_sdk_version()
    9
```


### get_target_sdk_version()

Return the android:targetSdkVersion attribute

```

    >>> apkf.get_target_sdk_version()
    21
```

### get_libraries()

Return the android:name attributes for libraries

```

    >>> apkf.get_libraries()
    []
```

### get_files()

Return the files inside the APK

```

    >>> apkf.get_files()
    [u'AndroidManifest.xml', u'assets/keys/dcb-pin-encrypt-v1/1',...]
```

### get_files_types()

Return the files inside the APK with their associated types (by using python-magic)
Please `pip install python-magic`

```
    >>> apkf.get_files_types()
    {u'res/layout/play_card_bundle_item_small.xml': "Android's binary XML",...}
```


### get_main_activity()

Return the name of the main activity

```

    >>> apkf.get_main_activity()
    com.android.vending.AssetBrowserActivity
```

### get_activities()

Return the android:name attribute of all activities

```

    >>> apkf.get_activities()
    ['com.android.vending.AssetBrowserActivity', ...]
```

### get_services()

Return the android:name attribute of all services

```

    >>> apkf.get_services()
    ['com.android.vending.GCMIntentService', ...]
```

### get_receivers()

Return the android:name attribute of all receivers

```

    >>> apkf.get_receivers()
    ['com.google.android.gcm.GCMBroadcastReceiver', ...]
```


### get_providers()

Return the android:name attribute of all providers

```

    >>> apkf.get_providers()
    ['com.google.android.finsky.providers.RecentSuggestionsProvider', ...]
```

### get_permissions()

Return permissions

```

    >>> apkf.get_permissions()
    ['com.android.vending.permission.C2D_MESSAGE', ...]
```

### show()

Return FILES, PERMISSIONS, MAIN ACTIVITY...

```

    >>> apkf.show()
    FILES: ...
```

### parse_icon()

Parse ICON of the apk, storage on icon_path

```

    >>> apkf.parse_icon(icon_path='/tmp')
    ...
```

### cert_text

```

    >>> apkf.cert_text
    Certificate:
    Data:Version: 3 (0x2)
    ...

```