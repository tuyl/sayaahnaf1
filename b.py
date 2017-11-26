# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="Elo09hrSuKTDcOXu8L83.ui4iewdkcsL+LbOtFNA/eW.ul6eXzv2fyWoniZ6ATetCT0G06CXOE2p4xL2f/zSZQM=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="El9vMwqsUaAhtNdn1vp0.L35okPRiB0SeAjVsPXm88a.C0QR/WXPkd0zaWULrO9vUj/MDVLuSRU7dlhjh1J11yw=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Elih9SvhEcSLfL05MjVa.aEeWIyG9x1dOMYBZ+uJtwG.0n8DTUG4fibujXdzOD8mxIuecLigbW+T793SiwR54vU=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="Elq9833kwOsSLvmXoax1.MLIwTV+u+0irFfkeAKSISq.sgK4Ew8WIfcRyN8dnzyqaqRwoKWLuIfBYFMuuk4tNco=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="ElYNpTuTkbhuzpkFh5jf.LVY1O9KFYX7cncSONiS93W./8OG5QpsZALGnFG0fE9B54MWJFTTgYfB/Q0R7OvpfN8=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="Elih9SvhEcSLfL05MjVa.aEeWIyG9x1dOMYBZ+uJtwG.0n8DTUG4fibujXdzOD8mxIuecLigbW+T793SiwR54vU=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="El9vMwqsUaAhtNdn1vp0.L35okPRiB0SeAjVsPXm88a.C0QR/WXPkd0zaWULrO9vUj/MDVLuSRU7dlhjh1J11yw=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token='Elk20UTTXp1bk0CePdm4.6UjaexCfHLKdviFmQ5sP5a.xYZoV/7kkCBT3oFsZFwsVfWNIcYpUZaQTc0ogI1YzqQ=')
ki8.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

album = None
image_path = 'tmp/tmp.jpg'

helpMessage ="""======[C滩虆潭岽徧蔡吿夺磵滩虆潭岽嵦蔡吿夺磤滩虆潭纱滩虆潭岽吿蔡吿禲======
馃敮 銆孒elp銆�
馃敮 銆孠ick:mid銆�
馃敮 銆孏etid @Tag銆�
馃敮 銆孖nvite:mid銆�
馃敮 銆孧e銆�
馃敮 銆孧ybot銆�
馃敮 銆孋ancel銆�
馃敮 銆孫url銆�
馃敮 銆孋url銆�
馃敮 銆孖nvite:gcreator銆�
馃敮 銆孧ybio銆�
馃敮 銆孏etinfo @Tag銆�
馃敮 銆孏etinfo銆�
馃敮 銆孲peed銆�
馃敮 銆孴L:text銆�
馃敮 銆孉llbio:text銆�
馃敮 銆孏n text銆�
馃敮 銆孨ame1-10:text銆�
馃敮 銆孧ybio:text銆�
馃敮 銆孧yname:text銆�
馃敮 銆孊locklist銆�
馃敮 銆孏cancel1-10銆�
馃敮 銆孋ontact:on/off銆�
馃敮 銆孭rotect:on/off銆�
馃敮 銆孮r:on/off銆�
馃敮 銆孖nv:on/off銆�
馃敮 銆孋ancel:on/off銆�
馃敮 銆孞am:on/off銆�
馃敮 銆孞oin:on/off銆�
馃敮 銆孡eave:on/off銆�
馃敮 銆孲hare:on/off銆�
馃敮 銆孉dd:on/off銆�
馃敮 銆孲et銆�
馃敮 銆孡urking銆�
馃敮 銆孏creator銆�
馃敮 銆孏roups銆�
馃敮 銆孧check銆�
馃敮 銆孲pam add:text銆�
馃敮 銆孲pam cek銆�
馃敮 銆孲pam:number銆�
馃敮 銆孶rl銆�
馃敮 銆孋lock:text銆�
馃敮 銆孨k @銆�
馃敮 銆孏ift @銆�
馃敮 銆孊anned @銆�
馃敮 銆孶nbanned @銆�
馃敮 銆孊an:銆�
馃敮 銆孶nban:銆�
馃敮 銆孊anned銆�
馃敮 銆孶nbanned銆�
馃敮 銆孊anlist銆�
馃敮 銆孋ium1-10銆�
馃敮 銆孠ill銆�
--- Copy@
--- Backup
--- Add mimic@
--- Del mimic@
--- Mimic On/Off
--- Mimic list

"""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid
Fmid = ki6.getProfile().mid
Gmid = ki7.getProfile().mid
Hmid = ki8.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid]
admin = ["u511a4cb0643b3a03bc1b29af39b0f3a8"]
admsa = "u511a4cb0643b3a03bc1b29af39b0f3a8"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"""THX FOR ADD :
        鈽� K蛡蜑虗蛼虂蛝蜅蛨抬踏瘫蛶瘫踏虨汰I蜎蜖虖虄蛫虊蹋袒虧虡蛵痰 T炭虇虖虂虘蛠泰蜄蛶坦太蛨S虖虌蛣炭蛼踏滩摊蛥踏坦滩滩虡U蜆虜炭蛺叹叹台碳滩毯蹋态潭N處虥叹蜑蜆蛣蹋滩廷汰虧蜏滩虧酞台潭E虂虗蛝蜆虝虝炭蛶瘫廷毯虦  B虥虤虗虃虁蛡虖蜖獭蛨蜔號毯蜄虣虧泰虨檀O蜆虋虘叹叹蛫虄泰蹋蛥滩蹋獭虦蜏谈T C虃虌虃蛬虤蛺蜎蛻虜虤蛿虩太贪坍毯虩抬胎痰O炭虂蜖虝蛦虝毯虪蛥贪坛抬谭 N虙虝虂虗虘蛼蛠蜄虦袒蛥贪蛵坍碳潭T虝虅虃蜅虋蛣摊抬挞瘫蜁虪蜋踏虣R蛯虉蛦虇虥虣泰瘫虠摊潭O虥虤虗虃虁蛡虖蜖獭蛨蜔號毯蜄虣虧泰虨檀L蜆虋虘叹叹蛫虄泰蹋蛥滩蹋獭虦蜏谈  鈽�

   馃洝 http://line.me/ti/p/~ahnaffauzanr
""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"魛皞魛皞魛皞魛皞魛爜魛爜魛爜魛偝魪靠魛皞魛皞魛皞魛皞'聛聧蓱瞻詹蓱茠 ",
    "cName2":"螤螖覓",
    "cName3":"螤螖覓",
    "cName4":"螤螖覓",
    "cName5":"螤螖覓",
    "cName6":"螤螖覓",
    "cName7":"螤螖覓",
    "cName8":"螤螖覓",
    "blacklist":{},
    "wblacklist":True,
    "dblacklist":True,
    "Deffend kicker":True, 
    "ProtectQR":True,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True,
    
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
setTime = {}
setTime = wait2['setTime']

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","锛�","銈点儐銉�:","銈点儐銉�:","銈点儐銉╋細","銈点儐銉╋細"]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n銉�" + Name
                wait2['ROM'][op.param1][op.param2] = "銉�" + Name
        else:
            pass
    except:
        pass
        
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))


        if op.type == 11:
            if op.param2 not in Bots:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Please don't play qr")
            print "Update group"        
        #------Open QR Kick start------#
        if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 not in admin:
		    pass
		elif wait["ProtectQR"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        #------Open QR Kick finish-----#
        
        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
               	 if op.param2 not in admin:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#
        
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = ki2.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        Ti = ki2.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = ki3.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        Ti = ki3.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ki4.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki4.updateGroup(X)
                        Ti = ki4.reissueGroupTicket(op.param1)
                
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = ki5.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki5.updateGroup(X)
                        Ti = ki5.reissueGroupTicket(op.param1)
                        
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ki6.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        ki6.updateGroup(X)
                        Ti = ki6.reissueGroupTicket(op.param1)
                        
                if op.param3 in Fmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        
                if op.param3 in Gmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    ki2.acceptGroupInvitation(op.param1)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    ki3.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"

            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    ki4.acceptGroupInvitation(op.param1)
            else:
            	print "auto join is off"

            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    ki5.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"	
                    
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    ki6.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off" 
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    ki7.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
            else:  
                if cancelinvite["autoCancel"] == True:
                     try:
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "invite canceled"
                     except:
                        try:
                            print "Retry canceling invitation"
                            X = random.choice(KAC).getGroup(op.param1)
                            gInviMids = [contact.mid for contact in X.invitee]
                            random.choice(KAC).cancelGroupInvitation(op.param1, gInviMids)
                            print gInviMids + "invite canceled"
                        except:
                            print "Bot can't cancel the invitation"
                            pass


        if op.type == 17:
	        if op.param2 not in Bots:
		    if op.param2 in Bots:
		        pass
	        if wait["Deffend kicker"] == True:
		    if wait["blacklist"][op.param2] == True:
		       try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    cl.updateGroup(G)
#	    		random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		       except:
#	    		pass
			    try:
			        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			        G = random.choice(KAC).getGroup(op.param1)
			        G.preventJoinByTicket = True
			        random.choice(KAC).updateGroup(G)
#	    		    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			    except:
			        pass
		    elif op.param2 not in admin + Bots:
		        random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	        else:
		    pass

        if op.type == 19:
            if op.param2 in Bots:
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nTERCYDUCK :v\n馃槺馃槺馃槺")
            print "MEMBER HAS KICKOUT FROM THE GROUP"

		
	if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kc.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)                        
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = kr.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        kr.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        
                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = kr.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket) 
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)            
            except:
                pass
              
        if op.type == 19:
            if op.param3 in admin:
                try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                except:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1,admin)
                    except:
                        print ("kicker kicked")

        if op.type == 19:
            if wait["Deffend kicker"] == True:
                if op.param2 not in Bots:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    except:
                        print "sukses"
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group銆乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                           
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                            
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki2.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                       
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                          
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                            
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki4.updateGroup(G)
                    Ticket = ki4.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                            
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki6.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki6.updateGroup(X)
                    Ti = ki6.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki5.updateGroup(G)
                    Ticket = ki5.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                    	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                            
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki7.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki7.updateGroup(X)
                    Ti = ki7.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki6.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki6.updateGroup(G)
                    Ticket = ki6.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True            
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                    	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                        
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])                            
                        except:
                            print ("client銇岃勾銈婅鍒秓r銈般儷銉笺儣銇瓨鍦ㄣ仐銇亜鐐恒�乗n["+op.param1+"]\n銇甛n["+op.param2+"]\n銈掕勾銈嬩簨銇屻仹銇嶃伨銇涖倱銇с仐銇熴�俓n銉栥儵銉冦偗銉偣銉堛伀杩藉姞銇椼伨銇欍��")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki6.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki7.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki7.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki7.updateGroup(G)
                    Ticket = ki7.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
       
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
                            
           #------Cancel User Kick start------#
        if op.type == 32:
            if wait ["Protectguest"] == True:
                if op.param2 not in Bots:
                    if op.param2 not in admin:	
                        cl.kickoutFromGroup(op.param1,[op.param2])
           #-----Cancel User Kick Finish------#
           
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        ki3.sendText(msg.to,"deleted")
                        ki4.sendText(msg.to,"deleted")
                        ki5.sendText(msg.to,"deleted")
                        ki6.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
                        ki4.sendText(msg.to,"It is not in the black list")
                        ki5.sendText(msg.to,"It is not in the black list")
                        ki6.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        ki2.sendText(msg.to,"already")
                        ki3.sendText(msg.to,"already")
                        ki4.sendText(msg.to,"already")
                        ki5.sendText(msg.to,"already")
                        ki6.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        ki2.sendText(msg.to,"aded")
                        ki3.sendText(msg.to,"aded")
                        ki4.sendText(msg.to,"aded")
                        ki5.sendText(msg.to,"aded")
                        ki6.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        ki2.sendText(msg.to,"deleted")
                        ki3.sendText(msg.to,"deleted")
                        ki4.sendText(msg.to,"deleted")
                        ki5.sendText(msg.to,"deleted")
                        ki6.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        ki2.sendText(msg.to,"It is not in the black list")
                        ki3.sendText(msg.to,"It is not in the black list")
                        ki4.sendText(msg.to,"It is not in the black list")
                        ki5.sendText(msg.to,"It is not in the black list")
                        ki6.sendText(msg.to,"It is not in the black list")
               elif "Ginfo" == msg.text:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': ginfo.creator.mid}
                    cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                    cl.sendMessage(msg)         
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL芒鈥犫�橽n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
            	if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,helpMessage)
                    else:
                        cl.sendText(msg.to,helpt)
            elif msg.text in ["SetGroup"]:
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,Setgroup)
                    else:
                        cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Bot1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Bot2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Bot3 gn ","")
                    ki3.updateGroup(X)
                else:
                    ki3.sendText(msg.to,"It can't be used besides the group.")
            elif"mid" in msg.text:
            	mmid = msg.text.replace("mid","")
                msg.contentType = 13
                msg.contentMetaData = {"mid" : mmid} 
                cl.sendMessage(msg) 
            elif "Kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Kick ","")
                    cl.kickoutFromGroup(msg.to,[midd])
            elif "Bot1 kick " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Bot1 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Bot2 kick " in msg.text:
                midd = msg.text.replace("Bot2 kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "Bot3 kick " in msg.text:
                midd = msg.text.replace("Bot3 kick ","")
                ki3.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
            	if msg.from_ in admin:
                    midd = msg.text.replace("Invite ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
            elif "Bot1 " in msg.text:
                midd = msg.text.replace("Bot1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Bot2 invite " in msg.text:
                midd = msg.text.replace("Bot2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "Bot3 invite " in msg.text:
                midd = msg.text.replace("Bot3 invite ","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"魝魛唻down魪靠魝魛唻down魪靠魝魛唻down魪靠魝魛唻down魪靠魝魛唻down魪靠魝魛唻down魪靠魝魛唻down魪靠")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"魝魛唺up魪靠魝魛唺up魪靠魝魛唺up魪靠魝魛唺up魪靠魝魛唺up魪靠魝魛唺up魪靠魝魛唺up魪靠")              
            elif msg.text in ["Me"]:
            	if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
            elif msg.text in ["Ki2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Ki3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
            elif msg.text in ["忙鈥炩�好Ｂ伮Ｆ掆�斆Ｆ捖ｂ�毬济Ｆ捖趁Ｆ捤�","Gift"]:
            	if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    cl.sendMessage(msg)
            elif msg.text in ["忙鈥炩�好Ｂ伮Ｆ掆�斆Ｆ捖ｂ�毬济Ｆ捖趁Ｆ捤�","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["忙鈥炩�好Ｂ伮Ｆ掆�斆Ｆ捖ｂ�毬济Ｆ捖趁Ｆ捤�","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ki2.sendMessage(msg)
            elif msg.text in ["忙鈥炩�好Ｂ伮Ｆ掆�斆Ｆ捖ｂ�毬济Ｆ捖趁Ｆ捤�","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["忙鈥炩�好Ｂ伮Ｆ掆�斆Ｆ捖ｂ�毬济Ｆ捖趁Ｆ捤�","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            cl.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"No one is inviting")
                            else:
                                cl.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        G = ki3.getGroup(msg.to)
                        if G.invitee is not None:
                            gInviMids = [contact.mid for contact in G.invitee]
                            ki3.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                ki3.sendText(msg.to,"No one is inviting")
                            else:
                                ki3.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open","Link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Done")
                        else:
                            cl.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 ourl","Bot1 link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done ")
                        else:
                            ki.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 ourl","Bot2 link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki2.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki2.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Done ")
                        else:
                            ki2.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 ourl","Bot3 link on"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki3.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki3.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Done ")
                        else:
                            ki3.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki3.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Close","Link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Done")
                        else:
                            cl.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can not be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 curl","Bot1 link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done ")
                        else:
                            ki.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 curl","Bot2 link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki2.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki2.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Done Chivas")
                        else:
                            ki2.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki2.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 curl","Bot3 link off"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        X = ki3.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki3.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Done ")
                        else:
                            ki3.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki3.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki3.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		replace=msg.text.lower().replace("jointicket ")
		if replace == "on":
			wait["atjointicket"]=True
		elif replace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            invitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Bmid)
                ki2.sendText(msg.to,Bmid)
                ki3.sendText(msg.to,Cmid)
                ki4.sendText(msg.to,Dmid)
                ki5.sendText(msg.to,Emid)
                ki6.sendText(msg.to,Fmid)
            elif "Mid" == msg.text:
                ki.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Bot2 mid" == msg.text:
                ki2.sendText(msg.to,Bmid)
            elif "Bot3 mid" == msg.text:
                ki3.sendText(msg.to,Cmid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot1 rename "]:
                string = msg.text.replace("Bot1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki2.getProfile()
                    profile_B.displayName = string
                    ki2.updateProfile(profile_B)
                    ki2.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Deff on","deffend on"]:
              if msg.from_ in admin:
                if wait["Deffend kicker"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Aktif")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Deffend kicker"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Aktif")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Deff Off","deffend off"]:
              if msg.from_ in admin:
                if wait["Deffend kicker"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Deffend kicker"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Aktif")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Aktif")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Protect Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr protect on","Qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Nyala")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Nyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr protect off","Qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protecct QR Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["茅鈧Ｃ德∶モ�λ�:茫鈥毬Ｆ捖�","K on","Contact on","茅隆炉莽陇潞茂录拧茅鈥撯��"]:
            	if msg.from_ in admin:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["茅鈧Ｃ德∶モ�λ�:茫鈥毬Ｆ掆��","K off","Contact off","茅隆炉莽陇潞茂录拧茅鈥斉�"]:
            	if msg.from_ in admin:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done ")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["猫鈥÷モ�光�⒚ヂ忊�毭ヅ� :茫鈥毬Ｆ捖�","Join on","Auto join:on","猫鈥÷モ�光�⒚ヂ徠捗ヅ� 茂录拧茅鈥撯��"]:
            	if msg.from_ in admin:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["猫鈥÷モ�光�⒚ヂ忊�毭ヅ� :茫鈥毬Ｆ掆��","Join off","Auto join:off","猫鈥÷モ�光�⒚ヂ徠捗ヅ� 茂录拧茅鈥斉�"]:
            	if msg.from_ in admin:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
            	if msg.from_ in admin:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                            wait["autoCancel"]["on"] = False
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                            else:
                                cl.sendText(msg.to,"氓鈥β趁ぢ衡�犆┾�氣偓猫炉路忙鈥光�櫭宦澝ｂ偓鈥毭β伱︹�斅睹ヂ尖偓猫炉路忙艗鈥∶ヂ∶ぢ郝好︹�⒙懊ヂ忊�樏┾偓聛")
                        else:
                            num =  int(strnum)
                            wait["autoCancel"]["on"] = True
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                            else:
                                cl.sendText(msg.to,strnum + "盲陆驴盲潞潞盲禄楼盲赂鈥姑♀�灻ヂ奥徝烩�灻р�澛ㄢ�÷ヅ犅┾�氣偓猫炉路忙鈥光�櫭宦�")
                    except:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Value is wrong")
                        else:
                            cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["氓录路氓藛露猫鈥÷モ�光�⒚┾偓鈧モ�÷�:茫鈥毬Ｆ捖�","Leave on","Auto leave:on","氓录路氓藛露猫鈥÷モ�光�⒚┾偓鈧モ�÷好寂∶┾�撯��"]:
            	if msg.from_ in admin:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆ヂ尖偓茫鈧��")
            elif msg.text in ["氓录路氓藛露猫鈥÷モ�光�⒚┾偓鈧モ�÷�:茫鈥毬Ｆ掆��","Leave off","Auto leave:off","氓录路氓藛露猫鈥÷モ�光�⒚┾偓鈧モ�÷好寂∶┾�斉�"]:
            	if msg.from_ in admin:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["氓鈥β泵ε撯��:茫鈥毬Ｆ捖�","Share on","Share on"]:
            	if msg.from_ in admin:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆ヂ尖偓茫鈧��")
            elif msg.text in ["氓鈥β泵ε撯��:茫鈥毬Ｆ掆��","Share off","Share off"]:
            	if msg.from_ in admin:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆モ�β趁︹�撀ｂ偓鈥�")
                            
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)                
                            
            elif msg.text in ["GL"]:
                cl.updateGroups()
                arg = msg.split(' ')
                if sender.id in myfriend:
                    if arg[1] == 'group':
                        listG = []
                        gr = cl.groups
                        for x in range(len(gr)):
                            listG.append(gr[x].name)
                            pass
                        listG.sort();
                        jo = '\n[*] '.join(str(l) for l in listG)
                    cl.sendText("[%s]\n %s" % (receiver.name, jo))
                else: 
                    cl.sendText("Mau lompat eaa")
                
            elif msg.text in ["Set View"]:
                md = ""
                if wait["Deffend kicker"] == True: md+=" Deffend kicker : on\n"
                else: md+=" Deffend kicker : off\n"
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect Qr      : on\n"
                else: md+=" Protect Qr   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)      
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"莽鈥郝该モ�犈捗β猜∶ヅ撀ｂ偓鈥�")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "盲禄楼盲赂鈥姑λ溌ヂ姑甭∶♀�灻р�郝该モ�犈�"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"莽鈥郝该モ�犈捗β猜∶ヅ撀ｂ偓鈥�")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "盲禄楼盲赂鈥姑λ溌ヂ姑甭∶♀�灻р�郝该モ�犈�"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "氓藛 茅鈩⒙っぢ衡�犆ぢ衡�姑♀�灻р�郝该モ�犈捗ｂ偓鈥�")
            elif msg.text in ["Group id","莽戮陇莽碌鈥灻モ�β╥d"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"忙鈥光�櫭宦澝ぢ衡�犆モ�β┢捖♀�灻┾�氣偓猫炉路茫鈧��")
            elif "album remove芒鈥犫��" in msg.text:
                gid = msg.text.replace("album remove芒鈥犫��","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "氓藛 茅鈩⒙っぢ衡�犆ぢ衡�姑♀�灻р�郝该モ�犈捗ｂ偓鈥�")
            elif msg.text in ["猫鈥÷モ�光�⒚柯矫ヅ� :茫鈥毬Ｆ捖�","Add on","Auto add:on","猫鈥÷モ�光�⒚柯矫ヅ� 茂录拧茅鈥撯��"]:
            	if msg.from_ in admin:
                    if wait["autoAdd"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆ヂ尖偓茫鈧��")
            elif msg.text in ["猫鈥÷モ�光�⒚柯矫ヅ� :茫鈥毬Ｆ掆��","Add off","Auto add:off","猫鈥÷モ�光�⒚柯矫ヅ� 茂录拧茅鈥斉�"]:
            	if msg.from_ in admin:
                    if wait["autoAdd"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoAdd"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆モ�β趁︹�撀ｂ偓鈥�")
            elif "Message change: " in msg.text:
            	if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message change: ","")
                    cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
            	if msg.from_ in admin:
                    wait["message"] = msg.text.replace("Message add: ","")
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message changed")
                    else:
                        cl.sendText(msg.to,"done茫鈧��")
            elif msg.text in ["Message","猫鈥÷モ�光�⒚柯矫ヅ� 氓鈥⒙徝モ偓鈩⒚久⒙好�"]:
            	if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                    else:
                        cl.sendText(msg.to,"The automatic appending information is set as follows茫鈧�歕n\n" + wait["message"])
            elif "Comment:" in msg.text:
            	if msg.from_ in admin:
                    c = msg.text.replace("Comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"message changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
            	if msg.from_ in admin:
                    c = msg.text.replace("Add comment:","")
                    if c in [""," ","\n",None]:
                        cl.sendText(msg.to,"String that can not be changed")
                    else:
                        wait["comment"] = c
                        cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["茫鈥毬趁Ｆ捖∶Ｆ捖趁Ｆ捤�:茫鈥毬Ｆ捖�","Comment on","Comment:on","猫鈥÷モ�光�⒚┞︹�撁� 聛莽鈥⑩劉猫篓鈧寂∶┾�撯��"]:
            	if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already on")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆ヂ尖偓茫鈧��")
            elif msg.text in ["茫鈥毬趁Ｆ捖∶Ｆ捖趁Ｆ捤�:茫鈥毬Ｆ掆��","Comment off","Comment:off","猫鈥÷モ�光�⒚┞︹�撁� 聛莽鈥⑩劉猫篓鈧寂∶┾�斉�"]:
            	if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"猫娄聛盲潞鈥犆モ�β趁︹�撀ｂ偓鈥�")
            elif msg.text in ["Comment","莽鈥⑩劉猫篓鈧⒙好�"]:
            	if msg.from_ in admin:
                    cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["url"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Can't be used outside the group")
                        else:
                            cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki2.updateGroup(x)
                    gurl = ki2.reissueGroupTicket(msg.to)
                    ki2.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki3.updateGroup(x)
                    gurl = ki3.reissueGroupTicket(msg.to)
                    ki3.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Clock on"]:
            	if msg.from_ in admin:
                    if wait["clock"] == True:
                        cl.sendText(msg.to,"already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Clock off"]:
            	if msg.from_ in admin:
                    if wait["clock"] == False:
                        cl.sendText(msg.to,"already off")
                    else:
                        wait["clock"] = False
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
            	if msg.from_ in admin:
                    n = msg.text.replace("Change clock ","")
                    if len(n.decode("utf-8")) > 13:
                        cl.sendText(msg.to,"changed")
                    else:
                        wait["cName"] = n
                        cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
            	if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"(%H:%M)")
                        profile = cl.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Clock Updated")
                    else:
                        cl.sendText(msg.to,"Please turn on the name clock")
                       
            elif msg.text == "Set":
                    cl.sendText(msg.to, "I have set a read point 鈾猏n銆宼es銆岻 will show you who I have read 鈾�")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "sukses"
            elif msg.text == "Lurking":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal 鈾猏n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "suksessss"
                    else:                    
                        cl.sendText(msg.to, "An already read point has not been set.\n銆宻et銆峺ou can send 鈾� read point will be created 鈾�")

#-----------------------------------------------
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

#-----------------------------------------------
            elif msg.text in ["Backup","backup"]:
                    try:
                        cl.updateDisplayPicture(backup.pictureStatus)
                        cl.updateProfile(backup)
                        cl.sendText(msg.to, "Backup done")
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                        
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[Copy] OK"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Success Copy profile ~")
                            except Exception as e:
                    
             #------------------------------------------------

#=================================Mimic talk==========================
            
            mimic = {
    "status":False,
    "target":{}
}

elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
    text = msg.text
    if text is not None:
        jendral.sendText(msg.to,text)
    else:
        if msg.contentType == 7:
            msg.contentType = 7
            msg.text = None
            msg.contentMetadata = {
                                 "STKID": "6",
                                 "STKPKGID": "1",
                                 "STKVER": "100" }
            jendral.sendMessage(msg)
        elif msg.contentType == 13:
            msg.contentType = 13
            msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            jendral.sendMessage(msg)
elif "Mimic:" in msg.text:
    if msg.from_ in admin:
        cmd = msg.text.replace("Mimic:","")
        if cmd == "on":
            if mimic["status"] == False:
                mimic["status"] = True
                jendral.sendText(msg.to,"Mimic on")
            else:
                jendral.sendText(msg.to,"Mimic already on")
        elif cmd == "off":
            if mimic["status"] == True:
                mimic["status"] = False
                jendral.sendText(msg.to,"Mimic off")
            else:
                jendral.sendText(msg.to,"Mimic already off")
        elif "add:" in cmd:
            target0 = msg.text.replace("Mimic:add:","")
            target1 = target0.lstrip()
            target2 = target1.replace("@","")
            target3 = target2.rstrip()
            _name = target3
            gInfo = jendral.getGroup(msg.to)
            targets = []
            for a in gInfo.members:
                if _name == a.displayName:
                    targets.append(a.mid)
            if targets == []:
                jendral.sendText(msg.to,"No targets")
            else:
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        jendral.sendText(msg.to,"Success added target")
                        jendral.sendMessageWithMention(msg.to,target)
                        break
                    except:
                        jendral.sendText(msg.to,"Failed")
                        break
        elif "del:" in cmd:
            target0 = msg.text.replace("Mimic:del:","")
            target1 = target0.lstrip()
            target2 = target1.replace("@","")
            target3 = target2.rstrip()
            _name = target3
            gInfo = jendral.getGroup(msg.to)
            targets = []
            for a in gInfo.members:
                if _name == a.displayName:
                    targets.append(a.mid)
            if targets == []:
                jendral.sendText(msg.to,"No targets")
            else:
                for target in targets:
                    try:
                        del mimic["target"][target]
                        jendral.sendText(msg.to,"Success deleted target")
                        jendral.sendMessageWithMention(msg.to,target)
                        break
                    except:
                        jendral.sendText(msg.to,"Failed!")
                        break
        elif cmd == "list":
            if mimic["target"] == {}:
                jendral.sendText(msg.to,"No target")
            else:
                lst = "<<Lit Target>>"
                total = len(mimic["target"])
                for a in mimic["target"]:
                    if mimic["target"][a] == True:
                        stat = "On"
                    else:
                        stat = "Off"
                    lst += "\n->" + jendral.getContact(a).displayName + " | " + stat
                jendral.sendText(msg.to,lst + "\nTotal:" + total)

                #=================================Add mimic==========================
            
            elif ("Add mimic " in msg.text):
          #      if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Haha")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
#=================================Del mimic==========================
            
            elif ("Del mimic " in msg.text):
           #     if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Ma'afin aku ya kak")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
#=================================List mimic status==========================
            
            elif msg.text in ["Mimic list"]:
          #      if msg.from_ in admin:
                    if mimic["target"] == {}:
                        cl.sendText(msg.to,"No target")
                    else:
                        lst = "|∆{List Mimic}∆|"
                        total = len(mimic["target"])
                        for a in mimic["target"]:
                            if mimic["target"][a] == True:
                                stat = "On"
                            else:
                                stat = "Off"
                            lst += "\n=》" + cl.getContact(a).displayName + " | " + stat
                        cl.sendText(msg.to,lst + "\nTotal: {" + total + "}")
#=================================Mimic status==========================
            
            elif "Mimic " in msg.text:
         #       if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic mode on")
                        else:
                            cl.sendText(msg.to,"Sudah on kak")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic mode off")
                        else:
                            cl.sendText(msg.to,"Sudah off kak")
#===================================Pluse==================


            elif msg.text in ["Alo"]:
            	    if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True

                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)

                        ki.updateGroup(G)

            elif msg.text in ["1 join"]:
              if msg.from_ in admin:
                  X = ki.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  ki.updateGroup(X)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["2 join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
            
            elif msg.text in ["3 join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki2.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["4 join"]:
              if msg.from_ in admin:
                  x =cl.getGroup(msg.to)
                  x.preventJoinByYicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki3.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
           #Fungsi Tag all ----+++++++++#
                  
            elif msg.text in ["Summon"]:
                group = cl.getGroup(msg.to)
                jw = [contact.mid for contact in group.members]
                cb = ""
	        cb2 = ""
                strt = int(0)
                akh = int(0)
                for rs in jw:
                    xname = cl.getContact(rs).displayName
                    xlen = int(len('x')+1)
                    akh = akh + xlen
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(rs)+"},"""
                    strt = strt + int(len('x')+3)
		    akh = akh + 2
		    cb2 += "@x \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text ="\n"+cb2 + "\n Total:" + str(len(jw)) + "Mention  \n"
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
                    
             #Finish----------+++++++++++++#

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Bot3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Pulang"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"魛渷魛嚁魪靠Bye Bye "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to) 
                    except:
                         pass
            elif msg.text in ["Bye 1"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.eaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["hus hus sana"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot1 @bye"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
            elif msg.text in ["Bot2 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bot3 @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif ("Bunuh " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)
            # ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("cyduck " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass        
            elif msg.text in ["Kill"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki3.sendText(msg.to,"hahahahaha")
                            ki4.sendText(msg.to,"masih mauko")
                            ki5.sendText(msg.to,"sundala nu")
                            ki6.sendText(msg.to,"kodong di kick")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
                                
            
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"􀜁􀇔􏿿Update Names👉 " + string + "👈")
            
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kr.getProfile()
                    profile.statusMessage = string
                    kr.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kx.getProfile()
                    profile.statusMessage = string
            
            
            elif msg.text in ["Backup","backup"]:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
                        
            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    print "[Copy] OK"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendMessage(msg.to, "Success Copy profile ~")
                            except Exception as e:
                               print e
                             
            elif "A1 Copy @" in msg.text:
                if msg.toType == 2:
                    print "[Copy] OK"
                    _name = msg.text.replace("A1 Copy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        ki.sendMessage(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendMessage(msg.to, "Success Copy profile ~")
                            except Exception as e:
                               print e
                               
            elif msg.text in ["gambar"]:
                try:
                    cl.sendImageWithURL(msg.to, "http://i0.kym-cdn.com/photos/images/original/001/109/640/212.jpg")
                except Exception as e:
                    sendMessage(msg.to, str(e))
                    
            elif "Ratakan" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Ratakan","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        ki.sendText(msg.to,"Siap")
                        ki2.sendText(msg.to,"Bersedia")
                        ki3.sendText(msg.to,"Ratakan :v")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            ki2.sendText(msg.to,"Not found.")
                            ki3.sendText(msg.to,"Not found.")
                        else:
                            for target in targets: 
                            	if not target in Bots:
                            	  	if not target in admin:
	                                    try:                                       
	                                        cl.kickoutFromGroup(msg.to,[target])
	                                        print (msg.to,[g.mid])
	                                    except:
	                                        ki.sendText(msg.to,"Rata Anjing")
	                                        ki2.sendText(msg.to,"hahahahaha")
	                                        ki3.sendText(msg.to,"Suck My Dick Sundala")
	    elif "Steal: " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal: ","")
                    Manis = cl.getContact(apil)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Avanya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User Tidak Memiliki Ava/Header")
                    else:
                        cl.sendText(msg.to,"Gambar Headernya")
                        cl.sendImageWithURL(msg.to,cover)      
              
            elif "Steal dp @" in msg.text:            
                   print "[Command]dp executing"
                   _name = msg.text.replace("Steal dp @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               print "[Command]dp executed"

            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                           targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                             try:
                                 klist=[cl,ki,ki2,ki3,ki4,ki5,ki6]
                                 kicker=random.choice(klist)
                                 kicker.kickoutFromGroup(msg.to,[target])
                                 print (msg.to,[g.mid])
                             except:
                                 ki2.sendText(msg.to,"Succes ")
                                 ki3.sendText(msg.to,"Fuck You")
                                 
            elif "beb " in msg.text:
            	if msg.from_ in admin:
                       nk0 = msg.text.replace("beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
            elif "Bl @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Bl @","")
                    _kicktarget = _name.rstrip(' ')
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _kicktarget == g.displayName:
                            targets.append(g.mid)
                            if targets == []:
                                cl.sendText(msg.to,"Not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        ki.sendText(msg.to,"Succes")
                                    except:
                                        cl.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Banned]ok"
                        _name = msg.text.replace("Banned @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found ")
                        else:
                            for target in targets:
                            	if not target in Bots:
                            	  	if not target in admin:
		                                try:
		                                    wait["blacklist"][target] = True
		                                    f=codecs.open('st2__b.json','w','utf-8')
		                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		                                    cl.sendText(msg.to,"Succes ")
		                                except:
		                                    cl.sendText(msg.to,"Error")
            elif ("blokir " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blocklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blocklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Block")
                   except:
                      pass
            elif "Unban @" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Unban]ok"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found ")
                        else:
                            for target in targets:
                            	if not target in Bots:
                            	  	if not target in admin:
		                                try:
		                                    del wait["blacklist"][target]
		                                    f=codecs.open('st2__b.json','w','utf-8')
		                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
		                                    cl.sendText(msg.to,"Succes ")
		                                except:
		                                	cl.sendText(msg.to,"Succes ")

#-----------------------------------------------
            elif msg.text in ["Test"]:
            	ki.sendText(msg.to,"Ok  魛▉魛劵double thumbs up魪靠")
                ki2.sendText(msg.to,"Ok  魛▉魛劵double thumbs up魪靠")
                ki3.sendText(msg.to,"Ok  魛▉魛劵double thumbs up魪靠")
                ki4.sendText(msg.to,"Ok  魛▉魛劵double thumbs up魪靠")
                ki5.sendText(msg.to,"Ok  魛▉魛劵double thumbs up魪靠")
                ki6.sendText(msg.to,"Ok  魛▉魛劵double thumbs up魪靠")
#-----------------------------------------------
            elif "Bc " in msg.text:
	        bctxt = msg.text.replace("Bc ","")
		ki.sendText(msg.to,(bctxt))
		ki2.sendText(msg.to,(bctxt))
		ki3.sendText(msg.to,(bctxt))
		ki4.sendText(msg.to,(bctxt))
		ki5.sendText(msg.to,(bctxt))
		ki6.sendText(msg.to,(bctxt))
#-----------------------------------------------
            #Kirim Spam Ke Kontak Target

            elif "Contact bc " in msg.text:
               if msg.from_ in admin:
                  bctxt = msg.text.replace("Contact bc ", "")
                  t = cl.getAllContactIds()
                  t = 1000
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1

            elif msg.text in ["say hi"]:
                ki.sendText(msg.to,"Hi buddy 魛渷魛厰Har Har魪靠")
                ki2.sendText(msg.to,"Hi buddy 魛渷魛厰Har Har魪靠")
                ki3.sendText(msg.to,"Hi buddy 魛渷魛厰Har Har魪靠")
                ki4.sendText(msg.to,"Hi buddy 魛渷魛厰Har Har魪靠")
                ki5.sendText(msg.to,"Hi buddy 魛渷魛厰Har Har魪靠")
                ki6.sendText(msg.to,"Hi buddy 魛渷魛厰Har Har魪靠")

#-----------------------------------------------

            elif msg.text in ["say hinata pekok"]:
                ki2.sendText(msg.to,"Hinata pekok 魛渷魛厰Har Har魪靠")
                ki3.sendText(msg.to,"Hinata pekok 魛渷魛厰Har Har魪靠")
                ki4.sendText(msg.to,"Hinata pekok 魛渷魛厰Har Har魪靠")
            elif msg.text in ["say Iphenk guanteng"]:
                ki2.sendText(msg.to,"Iphenk guanteng 魛渷魛厰Har Har魪靠")
                ki3.sendText(msg.to,"Iphenk guanteng 魛渷魛厰Har Har魪靠")
                ki4.sendText(msg.to,"Iphenk guanteng 魛渷魛厰Har Har魪靠")
            elif msg.text in ["say bobo ah","Bobo dulu ah"]:
                ki2.sendText(msg.to,"Have a nice dream  Har Har魪靠")
                ki3.sendText(msg.to,"Have a nice dream  Har Har魪靠")
                ki4.sendText(msg.to,"Have a nice dream  魛渷魛厰Har Har魪靠")
            elif msg.text in ["up"]:
                ki2.sendText(msg.to,"up")
                ki3.sendText(msg.to,"up")
                ki4.sendText(msg.to,"up")
#-----------------------------------------------
            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#-----------------------------------------------
            elif msg.text in ["Respon","respon"]:
            	ki.sendText(msg.to,"Ready")
                ki2.sendText(msg.to,"Ready")
                ki3.sendText(msg.to,"Ready")
                ki4.sendText(msg.to,"Ready")
                ki5.sendText(msg.to,"Ready")
                ki6.sendText(msg.to,"Ready")
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + "魛渷魛厰魪靠"
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "魛渷魛厰魪靠"
                ki2.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "魛渷魛厰魪靠"
                ki3.sendText(msg.to, text)
                profile = ku.getProfile()
                text = profile.displayName + "魛渷魛厰魪靠"
                ki4.sendText(msg.to, text)
                profile = kr.getProfile()
                text = profile.displayName + "魛渷魛厰魪靠"
                ki5.sendText(msg.to, text)
                profile = kx.getProfile()
                text = profile.displayName + "魛渷魛厰魪靠"
                ki6.sendText(msg.to, text)
#-----------------------------------------------
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                  #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#------------------------------------------------            elif msg.text in ["List group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[~]%s\n" % (cl.getGroup(i).name +str (len (cl.getGroup(i).members)))
                    cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))


            elif msg.text in ["Sp","Speed","speed"]:
            	if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "Progress...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
                    ki6.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Banned"]:
            	if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unbanned"]:
            	if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Cek banned"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill banned"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"There was no blacklist user")
                        ki2.sendText(msg.to,"There was no blacklist user")
                        ki3.sendText(msg.to,"There was no blacklist user")
                        ki4.sendText(msg.to,"There was no blacklist user")
                        ki5.sendText(msg.to,"There was no blacklist user")
                        ki6.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki2.kickoutFromGroup(msg.to,[jj])
                        ki3.kickoutFromGroup(msg.to,[jj])
                        ki4.kickoutFromGroup(msg.to,[jj])
                        ki5.kickoutFromGroup(msg.to,[jj])
                        ki6.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki2.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki3.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki4.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki5.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    ki6.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(msg.to,[_mid])
                        cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
            	if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
            elif "album芒鈥犫��" in msg.text:
                try:
                    albumtags = msg.text.replace("album芒鈥犫��","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakec芒鈥犫��" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakec芒鈥犫��","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass

            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"

            elif "Ar Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Ar Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     print "[Command]Stalk executed - success"

            elif "Ar stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Ar stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - success"

            elif "Ar img" in msg.text:
                path = "a.png"
                try:
                    cl.sendImage(msg.to, path)
                except:
                    cl.sendText(msg.to, "Failed to upload image")        

            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in Bots:
                        pass
                    else:
                        print "No Action"

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n銉�" + Name
                        wait2['ROM'][op.param1][op.param2] = "銉�" + Name
                else:
                    cl.sendText
            except:
                pass                
                        
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = ki2.getProfile()
                profile3.displayName = wait["cName3"]
                ki2.updateProfile(profile3)

                profile3 = ki3.getProfile()
                profile3.displayName = wait["cName3"]
                ki3.updateProfile(profile3)

                profile3 = ki4.getProfile()
                profile3.displayName = wait["cName3"]
                ki4.updateProfile(profile3)

                profile3 = ki5.getProfile()
                profile3.displayName = wait["cName3"]
                ki5.updateProfile(profile3)
                
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile4 = ki6.getProfile()
                profile4.displayName = wait["cName4"] + nowT
                ki6.updateProfile(profile4)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
