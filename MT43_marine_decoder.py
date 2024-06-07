# -*- coding: utf-8 -*-
"""
Matching tables for MT43 Marine type message (Dc = 14)

@author: Allystar Technology Co. Limited
"""

matchingtable_mt43_marine_Dw = {
    0: "海上警報解除",
    10: "海上着氷警報",
    11: "海上濃霧警報",
    12: "海上うねり警報",
    20: "海上風警報",
    21: "海上強風警報",
    22: "海上暴風警報",
    23: "海上台風警報",
    31: "その他の警報等情報要素_海上警報",
}

matchingtable_mt43_marine_Pl = {
    1000: "日本海北部及びオホーツク海南部",
    1010: "サハリン東方海上",
    1020: "サハリン西方海上",
    1030: "網走沖",
    1040: "宗谷海峡",
    1050: "北海道西方海上",
    1100: "北海道南方及び東方海上",
    1110: "北海道東方海上",
    1120: "釧路沖",
    1130: "日高沖",
    1140: "津軽海峡",
    1150: "檜山津軽沖",
    2000: "三陸沖",
    2010: "三陸沖東部",
    2020: "三陸沖西部",
    3000: "関東海域",
    3010: "関東海域北部",
    3020: "関東海域南部",
    3100: "日本海中部",
    3110: "沿海州南部沖",
    3120: "秋田沖",
    3130: "佐渡沖",
    3140: "能登沖",
    3200: "東海海域",
    3210: "東海海域東部",
    3220: "東海海域西部",
    3230: "東海海域南部",
    4000: "四国沖及び瀬戸内海",
    4010: "瀬戸内海",
    4020: "四国沖北部",
    4030: "四国沖南部",
    4100: "日本海西部",
    4110: "日本海北西部",
    4120: "山陰沖東部及び若狭湾付近",
    4130: "山陰沖西部",
    5000: "対馬海峡",
    5100: "九州西方海上",
    5110: "済州島西海上",
    5120: "長崎西海上",
    5130: "女島南西海上",
    5200: "九州南方海上及び日向灘",
    5210: "日向灘",
    5220: "鹿児島海域",
    5230: "奄美海域",
    6000: "沖縄海域",
    6010: "東シナ海南部",
    6020: "沖縄東方海上",
    6030: "沖縄南方海上",
    10000: "その他の地方海上予報区",
}

def match_mt43_marine_Dw(Dw):
    return matchingtable_mt43_marine_Dw.get(Dw, "警報等情報要素_海上警報(コード番号：NN)")

def match_mt43_marine_Pl(Pl):
    return matchingtable_mt43_marine_Pl.get(Pl, "地方海上予報区(コード番号：NNNN)")

def mt43_marine_dec(binary_message):
    
    AtMo = int(binary_message[0:4],2)
    AtD = int(binary_message[4:9],2)
    AtH = int(binary_message[9:14],2)
    AtMi = int(binary_message[14:20],2)
    It = int(binary_message[20:22], 2)
    Dw = [0]*8
    Pl = [0]*8
    for i in range(0,8):
        Dw[i] = int(binary_message[32+i*19:37+i*19],2)
        Pl[i] = int(binary_message[37+i*19:51+i*19],2)
    #print(Dw)
    #print(Pl)
    #Generate the message
    message_header = "防災気象情報(海上)\n海上警報が発表されました。\n\n"
    message_header += "発表時刻："+str(AtMo)+"月"+str(AtD)+"日"+str(AtH)+"時"+str(AtMi)+"分\n\n"
    message = ""
    for i in range(0,8):
        if not(Dw[i] == 0 and Pl[i] == 0):
            message+=message_header
            message+="警報等情報要素："+match_mt43_marine_Dw(Dw[i])+"\n"
            message+=match_mt43_marine_Pl(Pl[i])+"\n"
            message += "------\n"

    return message
    