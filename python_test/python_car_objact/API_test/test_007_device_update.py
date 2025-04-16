import unittest
import requests
import json
import yaml

from ddt import ddt, file_data
from time import sleep

"""修改设备信息"""
@ddt()
class Test_Api_car_aotu(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.eea_id=[]
        cls.device_id=106
        cls.contacts_id=[]
        cls.device_audio_id=[]
        cls.share_id=[]
        cls.alert_id=[]


    def req_param(self,key1=None,values1=None,key2=None,values2=None,key3=None,values3=None):
        params={"token":"96669577BFB4BFDD48C354305484385E",key1: values1,key2: values2,key3: values3}
        return params
    def admin_param(self,key1=None,values1=None,key2=None,values2=None,key3=None,values3=None):
        params={"token":"238620",key1: values1,key2: values2,key3: values3}
        return params

    def req_mode(self,url,Type,param=None,data=None):
        header={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Content-Type":"application/json; charset=utf-8"
                }
        if Type == "get":
            result = requests.get(url=url,params=param,data=json.dumps(data),headers=header)
            return result.json()
        elif Type =="post":
            result = requests.post(url=url,params=param,data=json.dumps(data),headers=header)

            return result.json()
        elif Type =="del":
            result = requests.delete(url=url,params=param,data=json.dumps(data),headers=header)
            return result.json()
        elif Type == "put":
            result = requests.put(url=url,params=param,data=json.dumps(data),headers=header)
            return result.json()
        else:
            print("缺失请求类型/为空")

    @file_data("../API_datas/devm_finddevices.yaml")
    def test_001_find_device_list(self, url, Type,data,statusMsg):
        u"""后台管理-查询设备列表"""
        param=self.admin_param()
        respons=self.req_mode(url,Type,param,data)
        self.assertEqual(respons["statusMsg"], statusMsg)
        sleep(1)


    @file_data("../API_datas/devm_deviceUser.yaml")
    def test_002_devm_deviceUser(self, url, Type,statusMsg):
        u"""查看绑定人员"""
        param = self.admin_param(key1="deviceId",values1=self.device_id)
        respons=self.req_mode(url,Type,param)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(1)

    # @file_data("../API_datas/devm_unbing_device.yaml")
    # def test_003_devm_unbing_device(self, url, Type,data,statusMsg):
    # """后台解绑设备"""
    #
    #     print(url)
    #     print(Type)
    #     print(data)
    #     # print(url)
    #     param = self.admin_param()
    #     respons=self.req_mode(url,param,Type,data)
    #     # print(data)
    #     self.assertEqual(respons['statusMsg'],statusMsg)
    #     # print(respons)

    @file_data("../API_datas/devm_reValid.yaml")
    def test_004_devm_reValid(self, url,Type,param,data,statusMsg):
        u"""后台管理-重新入库"""
        respons=self.req_mode(url,Type,param,data)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)
        sleep(1)



    @file_data("../API_datas/device_findbyuserid.yaml")
    def test_005_device_findbyuserid(self, url,Type,statusMsg):
        u"""查询用户设备列表"""
        param = self.req_param()
        respons=self.req_mode(url,Type,param)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)
        sleep(1)


    @file_data("../API_datas/device_unbing.yaml")
    @unittest.skip("!!!!")
    def test_006_find_device_list(self, url,Type,statusMsg):
        u"""解绑设备"""
        data={"idList":[107]}
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        # self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)


    @file_data("../API_datas/device_updata.yaml")
    def test_009_device_updata(self, url,Type,data,statusMsg):
        u"""修改设备信息详情  需要绑定设备"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)
        sleep(1)

    #
    # @file_data("../API_datas/device_updata.yaml")
    # def test_008_device_updata(self, url,Type,param,data,statusMsg):
    #     respons=self.req_mode(url,Type,param,data)
    #     self.assertEqual(respons['statusMsg'],statusMsg)
    #     print(respons)

    @file_data("../API_datas/device_bing.yaml")
    def test_007_device_bing(self, url,Type,data,statusMsg):
        u"""绑定设备"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)
        sleep(1)


    @file_data("../API_datas/device_getLocatio.yaml")
    def test_010_device_getLocatio(self, url,Type,statusMsg):
        u"""目前只写了设备开机状态下获取位置"""
        param=self.req_param(key1='id',values1=106)
        respons=self.req_mode(url,Type,param,)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)

    @file_data("../API_datas/device_getdevice_info.yaml")
    def test_011_device_get_deviceinfo(self, url,Type,statusMsg):
        u"""查看设备信息，查询ID=106的设备"""
        param=self.req_param(key1='id',values1=106)
        respons=self.req_mode(url,Type,param,)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)

    @file_data("../API_datas/device_getdevicebyimei.yaml")
    def test_012_device_get_devicebyimei(self, url,Type,statusMsg):
        u"""查看设备信息imei，"""
        param=self.req_param(key1='imei',values1="94E686016B1C")
        respons=self.req_mode(url,Type,param,)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)

    @file_data("../API_datas/device_findbyid.yaml")
    def test_013_device_findbyid(self, url,Type,statusMsg):
        u"""查看单个设备详情信息"""
        param=self.req_param(key1='id',values1="106")
        respons=self.req_mode(url,Type,param,)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)

    @file_data("../API_datas/device_softwareupdata.yaml")
    def test_014_device_get_softwareupdata(self, url,Type,statusMsg):
        u"""调用固件更新"""
        param=self.req_param(key1='id',values1="106")
        respons=self.req_mode(url,Type,param,)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)


    @file_data("../API_datas/eealoc_addorupdata_add.yaml")
    def test_015_eealoc_addorupdata_add(self, url,Type,data,statusMsg):
        u"""添加围栏,状态分别是：进/出不下发关机，进入围栏下发关机，出围栏不关机"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        self.assertEqual(respons['statusMsg'],statusMsg)
        print(respons)
        sleep(2)


    @file_data("../API_datas/eealoc_geteealist.yaml")
    def test_016_eealoc_addorupdata(self, url,Type,statusMsg):
        u"""查询用户名下电子围栏列表,上个接口添加三个围栏，此接口断言查询状态和围栏个数"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,)
        eeanumber=len(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        self.assertEqual(eeanumber,3)
        rp_data=respons["data"]
        for i in rp_data:
            self.eea_id.append(i["id"])

        print(self.eea_id)
        sleep(2)

    @file_data("../API_datas/eealoc_addorupdata_updata.yaml")
    @unittest.skip("!!!!!")
    def test_017_eealoc_addorupdata_updata(self,url,Type,data,statusMsg):
        u"""更新围栏信息"""
        self.updata_yaml()
        param=self.req_param()
        print(url)
        print(Type)
        print(data)
        respons=self.req_mode(str(url),Type,param,data)
        self.assertEqual(respons['statusMsg'],statusMsg)


    @file_data("../API_datas/user_findbyid.yaml")
    def test_018_user_findbyid(self,url,Type,statusMsg):
        u"""查询用户信息"""
        param=self.req_param()
        respons=self.req_mode(str(url),Type,param,)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)

    @file_data("../API_datas/eealoc_multi_eeadevice.yaml")
    def test_019_eealoc_multieeadevice(self,url,Type,statusMsg):
        u"""批量给围栏添加设备"""
        param=self.req_param(key1="eeaIds",values1=self.eea_id,key2="deviceIds",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)

    @file_data("../API_datas/eealoc_deviceList.yaml")
    def test_020_eealoc_deviceslist(self,url,Type,statusMsg):
        u"""获取可添加至围栏的设备列表"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)

    @file_data("../API_datas/eeaLoc_getDeviceEeaList.yaml")
    def test_021_eealoc_getdeviceeealist(self,url,Type,statusMsg):
        u"""查询某个设备的围栏"""
        param=self.req_param(key1="deviceId",values1=self.device_id,key2="isAll",values2="false")
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)

    @file_data("../API_datas/eealoc_adddevicetoeealocs.yaml")
    def test_022_eealoc_adddevicetoeealocs(self,url,Type,statusMsg):
        """设备批量添加用户名下已有围栏"""
        param=self.req_param(key1="eeaLocs",values1=self.eea_id,key2="device_id",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)

    @file_data("../API_datas/eealoc_updataenable.yaml")
    def test_023_eealoc_updataenable(self,url,Type,statusMsg):
        u"""修改围栏启用状态"""
        param=self.req_param(key1="ids",values1=self.eea_id,key2="enable",values2="false")
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)

    @file_data("../API_datas/eeaLoc_gerEeainfo.yaml")
    def test_024_eealoc_geteeainfo(self,url,Type,statusMsg):
        """查询围栏详情"""
        param=self.req_param(key1="eeaId",values1=self.eea_id[0])
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(2)


    @file_data("../API_datas/eealoc_deleteeea.yaml")
    def test_026_eealoc_deleteeea    (self,url,Type,statusMsg):
        """删除围栏"""
        param=self.req_param(key1="ids",values1=self.eea_id[0],key2="device_id",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(1)
        param=self.req_param(key1="ids",values1=self.eea_id[1],key2="device_id",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(1)

        param=self.req_param(key1="ids",values1=self.eea_id[2],key2="device_id",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(1)

    @file_data("../API_datas/eealoc_removedevicetoeealocs.yaml")
    def test_025_eealoc_removedevicetoeealocs(self,url,Type,statusMsg):
        """设备批量移除围栏"""
        param=self.req_param(key1="eeaLocs",values1=self.eea_id[1:-1],key2="device_id",values2=self.device_id)
        print(self.eea_id[1:-1])
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)


    @file_data("../API_datas/contacts_data/contacts_add.yaml")
    def test_027_contacts_add(self,url,Type,data,statusMsg):
        """添加警报联系人"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(1)

    @file_data("../API_datas/contacts_data/contacts_findbiuserid.yaml")
    def test_028_contacts_findbyuserid(self,url,Type,statusMsg):
        """查询警报联系人"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,)

        contacts=respons["data"][0]["id"]
        self.contacts_id.append(contacts)
        print(self.contacts_id)
        self.assertEqual(respons['statusMsg'],statusMsg)
        sleep(1)

    # @file_data("../API_datas/contacts_data/contacts_findbiuserid.yaml")
    # @ddt([{"id": self.contacts_id,"userId": 15,"name":"岐王","mobilePhone":18665868717}])
    # def test_0029_contacts_add(self,url,Type,statusMsg):
    #     """更新警报警报联系人"""
    #     param=self.req_param()
    #     respons=self.req_mode(url,Type,param,)
    #     self.contacts_id=respons["data"][0]["id"]
    #     self.assertEqual(respons['statusMsg'],statusMsg)


    @file_data("../API_datas/contacts_data/contacts_delete.yaml")
    def test_030_contacts_delete(self,url,Type,statusMsg):
        """删除联系人"""
        param=self.req_param(key1="id",values1=self.contacts_id[0])

        respons=self.req_mode(url,Type,param)
        print(respons)

        print(self.contacts_id)
        self.assertEqual(respons['statusMsg'],statusMsg)

    @file_data("../API_datas/location_his_data/location_findevicelist.yaml")
    def test_031_location_finddevicelist(self,url,Type,data,statusMsg):
        """历史轨迹"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        self.assertEqual(respons['statusMsg'],statusMsg)


    @file_data("../API_datas/audio_beginaudio.yaml")
    def test_032_audio_beginaudio(self,url,Type,statusMsg):
        """下发录音"""
        param=self.req_param(key1="time",values1=30,key2="deviceId",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['statusMsg'],statusMsg)

    @file_data("../API_datas/audio_getdevice_audio_status.yaml")
    def test_033_audio_getaudiostatus(self,url,Type):
        """查询某个设备录音状态"""
        param=self.req_param(key2="deviceId",values2=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons['status'],1)


    @file_data("../API_datas/audio_getDevice_AudioList.yaml")
    def test_034_audio_getdevice_audiolist(self,url,Type,statusMsg):
        """查询设备录音列表"""
        param=self.req_param(key1="deviceId",values1=self.device_id,key2="pageNo",values2=1,key3="pageSize",values3=1)
        respons=self.req_mode(url,Type,param,)
        datas=respons["data"]["list"][0]["id"]
        self.device_audio_id.append(datas)
        self.assertEqual(respons["statusMsg"],statusMsg)

    @file_data("../API_datas/audio_removeDevice_Audios.yaml")
    def test_035_audio_remocedevice_audio(self,url,Type,statusMsg):
        """删除录音"""
        param=self.req_param(key1="device_id",values1=self.device_id,key2="audios",values2=self.device_audio_id)
        respons=self.req_mode(url,Type,param,)
        self.assertEqual(respons["statusMsg"],statusMsg)

    @file_data("../API_datas/share_data/share_inbittation.yaml")
    def test_036_share_invitation(self,url,Type,data,statusMsg):
        """发送邀请共享"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        print(respons)
        self.assertEqual(respons["statusMsg"],statusMsg)

    @file_data("../API_datas/share_data/share_invitationlist.yaml")
    def test_037_share_invitationlist(self,url,Type,statusMsg):
        """获取发送邀请信息列表"""
        param=self.req_param(key1="deviceId",values1=self.device_id)
        respons=self.req_mode(url,Type,param,)
        self.share_id.append(respons["data"][0]["id"])
        print(respons)
        self.assertEqual(respons["statusMsg"],statusMsg)

    @file_data("../API_datas/share_data/share_cancellnvtation.yaml")
    def test_038_share_cangellnvitation(self,url,Type,statusMsg):
        """移除共享"""
        param=self.req_param(key1="id",values1=self.share_id[0])
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons["statusMsg"],statusMsg)

    @file_data("../API_datas/share_data/share_invitedlist.yaml")
    def test_039_share_invitedlist(self,url,Type,statusMsg):
        """被邀请接口没有写"""
        """获取受邀请设备列表"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons["statusMsg"],statusMsg)

    @file_data("../API_datas/ad_carousel_data/ad_carousel.yaml")
    def test_040_ad_carousel(self,url,Type,):
        """轮播图片广告获取"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,)
        data=respons["data"][0]["imgPath"]
        self.assertIsNotNone(data)

    @file_data("../API_datas/devicesetingdata/deviceSetting_changeTrackMode.yaml")
    def test_041_changetrackmode(self,url,Type,data):
        """进入精准定位"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        data=respons["statusMsg"]
        self.assertIsNotNone(data)

    @file_data("../API_datas/devicesetingdata/deviceSetting_addOrUpdate.yaml")
    def test_042_deviceSetting_addOrUpdate(self,url,Type,data):
        """配置硬件模式"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        print(respons)
        data=respons["statusMsg"]
        self.assertIsNotNone(data)

    @file_data("../API_datas/devicesetingdata/deviceSetting_findByDeviceId.yaml")
    def test_043_deviceSetting_deviceSetting_findByDeviceId(self,url,Type,statusMsg):
        """查看硬件配置"""
        param=self.req_param(key1="deviceId",values1=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons["statusMsg"], statusMsg)

    @file_data("../API_datas/devicesetingdata/deviceSetting_findSleepTimeById.yaml")
    def test_044_deviceSetting_deviceSetting_findByDeviceId(self,url,Type,statusMsg):
        """查看设备下次唤醒时间"""
        param=self.req_param(key1="id",values1=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons["statusMsg"], statusMsg)

    @file_data("../API_datas/devicesetingdata/deviceSetting_remainingHoursOfUse.yaml")
    def test_045_deviceSetting_deviceSetting_remainingHoursOfUse(self,url,Type,statusMsg):
        """查看设备下次唤醒时间"""
        param=self.req_param(key1="deviceId",values1=self.device_id)
        respons=self.req_mode(url,Type,param,)
        print(respons)
        self.assertEqual(respons["statusMsg"], statusMsg)



    @file_data("../API_datas/alert_datas/alert_findList.yaml")
    def test_046_lert_findList(self,url,Type,data,statusMsg):
        """查询警报列表"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        # print(respons["data"]["list"][0]["rawData"])
        self.share_id.append(respons["data"]["list"][0]["rawData"])
        print(self.share_id)
        self.assertEqual(respons["statusMsg"], statusMsg)


    @file_data("../API_datas/alert_datas/alert_delete.yaml")
    def test_047_lert_findList(self,url,Type,statusMsg):
        """删除警报"""
        data={"removeIds":self.share_id[1]}
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        print(respons)
        self.assertEqual(respons["statusMsg"], statusMsg)



    @file_data("../API_datas/AlertFlag_data/user_updateAlertFlag.yaml")
    def test_048_user_updateAlertFlag(self,url,Type,data,statusMsg):
        """更改用户警报开关"""

        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        print(respons)
        self.assertEqual(respons["statusMsg"], statusMsg)

    @file_data("../API_datas/AlertFlag_data/user_sms_updata.yaml")
    def test_049_user_sms_updata(self,url,Type,data,statusMsg):
        """更改用户短信开关"""
        param=self.req_param()
        respons=self.req_mode(url,Type,param,data)
        print(respons)
        self.assertEqual(respons["statusMsg"], statusMsg)


if __name__ == '__main__':
    unittest.main()

