import os


temp_folder = os.environ['TEMP']
windows_temp_folder = os.environ['windir'] + '\\Temp'
appdata_folder = os.environ['USERPROFILE'] + '\\AppData\\Local\\Temp'
java_temp_folder = os.environ['USERPROFILE'] + \
    '\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\6.0'
opera_gx_cache_folder = os.environ['USERPROFILE'] + \
    '\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\Cache'
brave_cache_folder = os.environ['USERPROFILE'] + \
    '\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache'
edge_cache_folder = os.environ['USERPROFILE'] + \
    '\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache'
firefox_cache_folder = os.environ['USERPROFILE'] + \
    '\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\<profile>\\cache2\\entries'
chrome_cache_folder = os.environ['USERPROFILE'] + \
    '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'

# Array of folders to clean
folders_to_clean = [
    temp_folder,
    windows_temp_folder,
    appdata_folder,
    java_temp_folder,
    opera_gx_cache_folder,
    brave_cache_folder,
    edge_cache_folder,
    firefox_cache_folder,
    chrome_cache_folder,
]
