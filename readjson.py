import pymysql, os, json

# read JSON file which is in the next parent folder
file = "2017-10-10-0003Z.json"
json_data = open(file, encoding="utf8").read()
json_obj = json.loads(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = 'localhost', user = 'root', passwd = '', db = 'test')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    Id = validate_string(item.get("Id", None))
    Rcvr = validate_string(item.get("Rcvr", None))
    HasSig = validate_string(item.get("HasSig", None))
    Icao = validate_string(item.get("Icao", None))
    Bad = validate_string(item.get("Bad", None))
    Reg = validate_string(item.get("Reg", None))
    FSeen = validate_string(item.get("FSeen", None))
    TSecs = validate_string(item.get("TSecs", None))
    CMsgs = validate_string(item.get("CMsgs", None))
    Alt = validate_string(item.get("Alt", None))
    GAlt = validate_string(item.get("GAlt", None))
    AltT = validate_string(item.get("AltT", None))
    Tisb = validate_string(item.get("Tisb", None))
    Spd = validate_string(item.get("Spd", None))
    Trak = validate_string(item.get("Trak", None))
    TrkH = validate_string(item.get("TrkH", None))
    Type = validate_string(item.get("Type", None))
    Mdl = validate_string(item.get("Mdl", None))
    Man = validate_string(item.get("Man", None))
    CNum = validate_string(item.get("CNum", None))
    Op = validate_string(item.get("Op", None))
    OpIcao = validate_string(item.get("OpIcao", None))
    Sqk = validate_string(item.get("Sqk", None))
    Vsi = validate_string(item.get("Vsi", None))
    VsiT = validate_string(item.get("VsiT", None))
    WTC = validate_string(item.get("WTC", None))
    Species = validate_string(item.get("Species", None))
    Engines = validate_string(item.get("Engines", None))
    EngType = validate_string(item.get("EngType", None))
    EngMount = validate_string(item.get("EngMount", None))
    Mil = validate_string(item.get("Mil", None))
    Cou = validate_string(item.get("Cou", None))
    HasPic = validate_string(item.get("HasPic", None))
    Interested = validate_string(item.get("Interested", None))
    FlightsCount = validate_string(item.get("FlightsCount", None))
    Gnd = validate_string(item.get("Gnd", None))
    SpdTyp = validate_string(item.get("SpdTyp", None))
    CallSus = validate_string(item.get("CallSus", None))
    ResetTrail = validate_string(item.get("ResetTrail", None))
    TT = validate_string(item.get("TT", None))
    Trt = validate_string(item.get("Trt", None))
    Year = validate_string(item.get("Year", None))
    Cos = validate_string(item.get("Cos", None))



    cursor.execute("INSERT INTO testp (Id, Rcvr, HasSig, Icao, Bad, Reg, FSeen, TSecs, CMsgs, Alt, GAlt, AltT, Tisb, Spd, Trak, TrkH, Type, Mdl, Man, CNum, Op, OpIcao, Sqk, Vsi, VsiT, WTC, Species, Engines, EngType, EngMount, Mil, Cou, HasPic, Interested, FlightsCount, Gnd, SpdTyp, CallSus, ResetTrail, TT, Trt, Year, Cos) "
                   "VALUES (INSERT INTO testp (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (Id, Rcvr, HasSig, Icao, Bad, Reg, FSeen, TSecs, CMsgs, Alt, GAlt, AltT, Tisb, Spd, Trak, TrkH, Type, Mdl, Man, CNum, Op, OpIcao, Sqk, Vsi, VsiT, WTC, Species, Engines, EngType, EngMount, Mil, Cou, HasPic, Interested, FlightsCount, Gnd, SpdTyp, CallSus, ResetTrail, TT, Trt, Year, Cos))
con.commit()
con.close()