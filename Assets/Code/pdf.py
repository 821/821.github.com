#coding: gbk
#ʹ�� Python 3
import http.client,urllib.request,os,re
#�@ȡ���N����
def GetAll(ZXLink):
	Domain=re.findall(r'http://([^/]+)/.+',ZXLink)[0] # ����
	URI=re.findall(r'http://[^/]+(/.+)',ZXLink)[0] # URI
	Response = urllib.request.urlopen(ZXLink)
	Web = str(Response.read())
	Response.close()
	PDFLink = re.findall(r'<a href="([^<]+)" target="_blank" >PDF</a>', Web)[0] # PDF �Č��H朽�
	ssNo = re.findall(r'ssNo = "(\d{8})"', Web)[0] # ����̖
	jpgRange = re.findall(r'jpgRange = "(\d+-\d+)"', Web)[0] # 퓴a
	return (PDFLink, Name, ssNo, jpgRange)
#���d
def DownPDF(Link, Page):
	urllib.request.urlretrieve(Link, Path+Page+".pdf")

for a in range(1,100):
	ZX=input("ZX link: ")
	PDFLink, Name, ssNo, jpgRange = GetAll(ZX)
	Path="F:\\"+ssNo+"\\"
	os.makedirs(Path, exist_ok=True)
	DownPDF(PDFLink,jpgRange)