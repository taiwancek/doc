FORMAT: 1A
HOST: https://cloud.altptech.com

# Altrump Cloud

欢迎使用 **Altrump Cloud** API
 
## 版本紀錄
 <table style="width:100%">
  <thead>
  <tr>
    <th>ver.</th>
    <th>modify</th>
    <th>created</th>
  </tr>
    </thead>
  <tr>
    <td>1</td>
    <td>註冊、登入、key上傳、key下載 API實作</td>
    <td>2018/1/2</td>
  </tr>

  <tr>
    <td>2</td>
    <td>* 新增錯誤碼 <br> * 修正登入密碼判斷錯誤</td>
    <td>2018/1/10</td>
  </tr>
    <tr>
    <td >3</td>
    <td>忘記密碼頁面與API實作</td>
    <td>2018/1/11</td>
  </tr>
    </tr>
    <tr>
    <td >4</td>
    <td>
    * 新增角色功能<br>
    * 新增新版註冊(v2)與登入(v2) API<br>
    * 實作User Section所有API
    </td>
    <td>2018/2/21</td>
  </tr>

</table> 

<style>
thead{
      background-color:#808080;
      color:#fff;
}
td {
   background-color:#fff;
}
</style>
# 常用指令
<!-- include(./cmd.md) -->

# 常用工具
<!-- include(./tools.md) -->



# 物件架構
<img src="./resouces/obj_structure.png" height="600px" title="obj structure">

## MQTT行為定義
<img src="./resouces/mqtt_flow.png" width="100%" title="MQTT FLOW">

```
範例：

#裝置開關
Topic:/應用程式UUID/訊息群組UUID/cmd
Message Data: {device_udid:'', device_key:'', action:'open/close', by_id:'user_id/device_id'}

Topic: /應用程式UUID/訊息群組UUID/notify
Message Data: {action:'open/close', result:'true/false', channel:'local/ble/wifi', 'msg':'false tip', name:'' }

#裝置命名
Topic: /應用程式UUID/訊息群組UUID/cmd
Message Data: {device_udid:'', device_key:'', action:'rename',value:'name', by_id:'user_id/device_id'}

Topic: /應用程式UUID/訊息群組UUID/notify
Message Data:  {action:'rename', result:'true/false', 'msg':'false tip', name:'' }
```

* 加密
  1. SSL/TLS(TCP/IP)
  2. AES(Message data)

<!-- ## Table Schema
<img src="./resouces/db_schema.png" width="100%" title="db schema"> -->


# 文獻
## APNS
* [APNS原理](https://blog.toright.com/posts/2806/ios-apns-%E8%A8%8A%E6%81%AF%E6%8E%A8%E6%92%A5-apple-push-notification-service-%E4%BB%8B%E7%B4%B9.html)
* [JSON格式](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html)
* 專案使用格式
```
    {
        "aps" : {
            "alert" : {
                "title" : "Game Request",
                "body" : "Bob wants to play poker",
                "action-loc-key" : "PLAY"
            },
            "badge" : 5
        },
        "acme1" : "bar",
        "acme2" : [ "bang",  "whiz" ]
    }
```

## FCM
* [Firebase 云消息传递服务器简介](https://firebase.google.com/docs/cloud-messaging/server?hl=zh-cn)  
* [Firebase 心得（Cloud Messaging）](http://jasonchiucc.github.io/2016/07/11/firebase-tutorial-cloud-messaging/)
* JSON格式  
  - Notification messages
  ```
   {
       "to" : "bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
       "notification" : {
       "body" : "great match!",            // 內容
       "title" : "Portugal vs. Denmark",   // 標題
       "icon" : "myicon"
      }
    }
  ```
  - Data messages
  ```
    {
      "to" : "bk3RNwTe3H0:CI2k_HHwgIpoDKCIZvvDMExUdFQ3P1...",
      "data" : {
          "Nick" : "Mario",
          "body" : "great match!",
          "Room" : "PortugalVSDenmark"
      },
    }
  ```
## Android Studio
* [如何使用 Firebase - 使用 Notification](http://givemepass.blogspot.tw/2017/07/firebase-notification.html)
* [如何使用 Firebase - 用 Android Studio 建立帳戶篇](http://givemepass.blogspot.tw/2017/03/firebase-android-studio.html)


## Server
* supervisor
 - [ubuntu上supervisor的使用和安装](https://my.oschina.net/u/2269208/blog/343936)
 - caddy.conf
 ```
  [program:caddy]
  command=/usr/local/bin/caddy  -conf="/etc/caddy/Caddyfile"
  ;directory=/var/log/caddy
  ;user=www-data
  ;environment=CADDYPATH=/etc/caddy/ssl
  user=root
  stdout_logfile=/var/log/supervisor/caddy.log
  stderr_logfile=/var/log/supervisor/caddy.log
  autostart=true
  autorestart=true
  ;startsecs=10
  ;stopwaitsecs=600
  ;startretries=3
 ```
 - supervisorRestart.sh
 ```
  #!/bin/bash

  sudo supervisorctl update
  sudo supervisorctl stop caddy
  sudo supervisorctl reread
  sudo supervisorctl add caddy
  sudo supervisorctl start caddy
 ```
## Golnag


## API文件工具
* [使用 API BluePrint 编写 RESTful 接口文档](http://devlu.me/2016/05/05/write-restful-api-doc-with-apiblueprint/)
* [API Blueprint Tutorial](https://apiblueprint.org/documentation/tutorial.html)
* [API Blueprint Language](https://github.com/apiaryio/api-blueprint/blob/master/API%20Blueprint%20Specification.md)

## IOT安全
* [MQTT安全篇](http://dataguild.org/?p=6866)
* [UUID package for Go language](https://github.com/satori/go.uuid)
* [JSON Web Token](https://yami.io/jwt/)
* [物聯網應用層通訊協定標準比較 CoAP vs MQTT ](http://blog.ittraining.com.tw/2016/12/coap-vs-mqtt.html)
* [Python 混淆](https://elmagnificogi.github.io/2017/12/01/Python-obfuscate/)
* [Python 加密](https://github.com/micropython/micropython/tree/master/mpy-cross)
* [Python 逆向工程](https://tool.lu/pyc/)
* [阿里云IOT](https://iot.aliyun.com/docs/suite/index.html)
* [物聯網BLE認證機制設計的挑戰以Gogoro Smart Scooter 為例](https://hitcon.org/2016/CMT/slide/day1-r0-a-1.pdf)
* [物聯網安全性最佳做法](https://docs.microsoft.com/zh-tw/azure/iot-suite/iot-security-best-practices)
* [AES vs SSL/TLS: Encryption for the internet of things ](https://www.electronicproducts.com/Computer_Peripherals/Communication_Peripherals/AES_vs_SSL_TLS_Encryption_for_the_internet_of_things.aspx)

## IOT規範與組織
* IoT網路安全聯盟(IoT Cybersecurity Alliance)
* [物聯網標準組織Thread Group](https://www.threadgroup.org/)
* [Google Nest 另闢物聯網陣營與 Intel、高通爭主導權](http://technews.tw/2014/07/16/google-nest-thread-group/)

## IOT開發平台
* [Android Things](https://developer.android.com/things/index.html)
* [Apple Home Kit](https://www.bnext.com.tw/article/44077/apple-homekit)
* [mbed](https://www.mbed.com/zh-cn/)
* [amebaiot](https://www.amebaiot.com/en/)


## 鎖業組織與新聞
* [台灣鎖業發展協會](http://www.lat.org.tw/html/introduction.php?PKey=1)
* [面對智能鎖客觀問題或許能讓智能家居走得更遠](http://www.lat.org.tw/html/news_detial.php?PCat=1&PKey=178#)
* [Apple Home Kit門鎖](https://www.apple.com/tw/ios/home/accessories/)

## 其他
* [你該掌握的30個最新IoT產業動向](https://www.ithome.com.tw/news/106530)

# Group 廣義推播定義
<!-- include(./push_define.md) -->

# Group 裝置推播定義
<!-- include(./push_define_for_device.md) -->

# Group Application
## Application [/api/application/create]
<!-- include(./application/create.md) -->
<!-- include(./application/update.md) -->
<!-- include(./application/list.md) -->
<!-- include(./application/get.md) -->
<!-- include(./application/delete.md) -->

# Group User
<!-- include(./user/register.md) -->
<!-- include(./user/register_v2.md) -->
<!-- include(./user/login_v2.md) -->
<!-- include(./user/login_third.md) -->
## User
<!-- include(./user/active.md) -->
<!-- include(./user/update.md) -->
<!-- include(./user/list.md) -->
<!-- include(./user/get.md) -->
<!-- include(./user/delete.md) -->
<!-- include(./user/bind.md) -->
<!-- include(./user/unbind.md) -->
## Role [/api/user/role]
<!-- include(./user/role/create.md) -->
<!-- include(./user/role/update.md) -->
<!-- include(./user/role/list.md) -->
<!-- include(./user/role/get.md) -->
<!-- include(./user/role/delete.md) -->
## Password [/api/password/request_reset]
<!-- include(./user/password/request_reset.md) -->
<!-- include(./user/password/reset.md) -->
<!-- include(./user/password/change.md) -->
<!-- include(./user/password/state.md) -->

# Group Friend
## Friend [/api/friend]
<!-- include(./friend/add.md) -->
<!-- include(./friend/list.md) -->
<!-- include(./friend/block.md) -->


#Group Phone
## Phone [/api/phone]
<!-- include(./phone/register.md) -->

#Group Firmware
## Firmware [/api/firmware]
<!-- include(./firmware/add.md) -->
<!-- include(./firmware/get.md) -->
<!-- include(./firmware/list.md) -->
<!-- include(./firmware/delete.md) -->
<!-- include(./firmware/release.md) -->
<!-- include(./firmware/code/list.md) -->

#Group Notification
## Notification [/api/push_noti]
<!-- include(./push_noti/application/list.md) -->
<!-- include(./push_noti/add.md) -->
<!-- include(./push_noti/list.md) -->
<!-- include(./push_noti/count.md) -->

# Group Store
## Store
<!-- include(./store/state.md) -->

# Group Message
## Message [/api/message/publish]
<!-- include(./message/publish.md) -->
<!-- include(./message/list.md) -->
<!-- include(./message/members.md) -->
## Group [/api/message/group/create]
<!-- include(./message/group/create.md) -->
<!-- include(./message/group/list.md) -->
<!-- include(./message/group/dissovle.md) -->
## Endpoint [/api/message/endpoint/join]
<!-- include(./message/endpoint/join.md) -->
<!-- include(./message/endpoint/exit.md) -->

# Group IOT Device
## Device [/api/device/register]
<!-- include(./device/register.md) -->
<!-- include(./device/list.md) -->
<!-- include(./device/get.md) -->
<!-- include(./device/update.md) --> 
<!-- include(./device/bind.md) -->
<!-- include(./device/unbind.md) -->
<!-- include(./device/enable.md) -->
<!-- include(./device/delete.md) -->
<!-- include(./device/ping.md) -->
<!-- include(./device/last_ping.md) -->
<!-- include(./device/push_device.md) -->
<!-- include(./device/push_phone.md) -->

<!-- ## Media [/api/device/media/create] -->
<!-- ainclude(./device/media/create.md) -->
<!-- ainclude(./device/media/delete.md) -->

# Group Fingerprint Key
## Key [/api/key/upload]
<!-- include(./fingerprint_key/upload.md) -->
<!-- include(./fingerprint_key/download.md) -->
