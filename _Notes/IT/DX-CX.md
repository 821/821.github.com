---
layout: indexed
title: 讀秀超星電子書下載入門篇
date: '2012/11/15 00:52:00'
---
本文成型於 2012-11-15 ，最後修改於 2015-02-27 。

## 超星公司基本架構
本體當然是超星。
然後他開設了一個叫<a href="http://www.duxiu.com" rel="external">讀秀</a>的東西，類似 Google Scholar ，但沒那麼完善，祇有書做得比較好。讀秀主要是通過銷售授權的方式給各機構使用，一般人只能「試用」。於是又有了一個鏡像<a href="http://www.ccelib.com/" rel="external">長春網絡圖書館</a>。又有一種特殊機構專用的，叫大醫，都是醫生用，跟讀秀非常像。
超星和讀秀是超星公司的兩大主脈，由此衍生出很多支脈，比如超星在很多機構都有鏡像站，但是書籍清晰度不高，沒什麼價值。超星還在北美開了個分店，不過書不多。讀秀/指針也有很多分身，基本上就是替換了域名而已。
我們關注超星和讀秀就可以了。

## 什麼書可以下載到
超星不是萬能的，不可能什麼書都有。超星主要掃描什麼書？由於超星的主要購買者是大學和研究機構，散戶不多，所以超星主要掃描通常高校館藏裡會有的書。也就是說，會稍微偏重學術類一些。由於超星主要藉助國內高校的館藏，因此國內出版的書籍佔了絕大多數。基本上，你需要的國內學術書有九成以上能找到，而台灣、香港學術書，成功率不到三成。
對於超星未掃描，而購買了讀秀權限的機構又有實體書的，讀秀會製作一個鏈接。這種書我們叫「無試讀」，又諧音叫「五十度」。連同其他超星掃描並上傳了，但讀秀和超星都搜索不到的書，都叫「無試讀」。
無試讀的書祇有超級高手能下載。
我們能下載的書，祇有通過讀秀能搜索到，並且在有機構帳號的情況下，書籍名稱旁邊有「部分閱讀」或「包庫全文」再或「鏡像全文」的書。

## 下載到什麼東西
標準的超星格式是 pdg ，但下載到的書的文件夾裡，通常會有 `bookinfo.dat` 和 `bookcontent.dat` 兩個文件。前者給出書籍的版權信息，如書名、作者、出版社、年份等（經常有缺失，而且還有搞錯的），後者是書籤文件（錯誤往往比較多，有的還沒有）。
我們又把下載到的 pdg 分爲幾等：
第一等叫清晰版，分辨率爲 300dpi ，對於 32k 的書，他的圖像寬度總是在 1000 以上。清晰版有很多種加密格式，不過本文較多涉及的可以分爲四種。第一種叫作 04H ，就是彩圖，有時黑白的書也用這種格式，很浪費空間。第二種稱爲 00H ，是單純黑白的，沒有灰度，非常節約空間。第三種是高度加密格式，包括高密 pdg 和新出的 pdz ，用了適當工具後不會下載到高密 pdg ， pdz 是新東西，也很少見，不討論。第四種是 pdf ，這種不是標準的，而是具有超星特色的 pdf ，本人同樣不會下載，也不希望自己下載到的書變成這樣，不討論。
第二等叫大圖，分辨率爲 150dpi ，寬度 983 。他會把黑白的書變成灰度的，所以體積經常比較大，看起來卻灰濛濛的。以前大圖還會加水印， 2014 年 7 月開始取消了水印。大圖如果沒下對就會變成寬度更小的中圖和小圖。由於沒有討論價值，本文不討論中圖和小圖。
第三等叫快速版，分辨率爲 150dpi ，寬度——反正很小，字也不清楚，還經常好像缺了幾個筆劃一樣。一般出現在「鏡像全文」和一些不懂操作的低手那裡，沒有用處，不討論。
第四等叫文本。文件名是 n\_n.pdg 格式，本質是文本 pdf ，但經過加密。這是超星掃描後 OCR 成文本的書，錯字連篇，比快速版還沒用。
第五等是神祕的印前 pdg ，也就是出版社直接把小樣給了超星，超星轉成他的格式。這種格式文件命名規則和文本 pdg 一樣，但排版是正確的，而且很節約空間，而且特別清晰，但是可遇不可求，本「高手」就見過一次，效果非常好，是 9 開頭的號。
綜上，正確下載的情況下，我們一般會下載到未加密的清晰版、大圖、文本三種。其中對學術研究有用的是清晰版和大圖。由於大圖明顯劣於清晰版，所以最好還是下載清晰版。

## 下載了用什麼查看、檢查
雖然官方閱覽器可以看，但是不好用，懂行的都用 UnicornViewer 看，版本越高越好，但高版本沒有向社會公佈。
超星真的很過分，經常發生一頁祇下載了一半，或者乾脆某頁沒下載的情況，可以用 PdgThumbViewer 來檢查。
二者的開發者是同一個人。順便說一下，二者均可用於檢驗下載到的書籍屬於哪一等。

## 下載清晰版
說起來似乎非常簡單。你登入讀秀，搜索你要的書，看到了，然後點「包庫全文」，再點紅色超星 logo ，自動打開超星閱覽器，右鍵，下載，就好了。或者你打開超星包庫，搜索，點「閱覽器閱讀」，自動打開超星閱覽器，右鍵，下載，也好了。
滴滴——錯誤一，你看不到「包庫全文」字樣？說明你的機構沒有購買該書的權限，不能下載。你有兩個選擇：下大圖（後面會講）、換機構（後面也會講）。
滴滴——錯誤二，點了「包庫全文」，卻發現打開的書竟然是文本的？這是個技術難題，有高手能解決，本「高手」不能。
滴滴——錯誤三，下載後不能用 UnicornViewer 看。當然了，通過官方方式下載的，下載時閱覽器都會熱心的幫你加密一下。解決方法是：使用超星 4.0 ，並打上老鷹版 ssreader.exe 的補丁。（更新：老鷹已經失效。）
滴滴——錯誤四，封面、書名頁、版權頁去哪裡了？答案是超星包庫沒有，祇有讀秀上有 150dpi 的。
滴滴——錯誤五，其實書名頁是可以下載到清晰版的，就是用棒棒糖 CxCandy 。當超星裡正在閱讀某書的時候，點一下「全自動新建」，然後確定，下載，即可。
總結：一般而言，下載淸晰版用 CxCandy 抓一下信息，然後下載，是最好的。

## 下載自建庫淸晰版
現在，很多機構在購買了讀秀的基礎上，還用讀秀、超星框架製作了自建庫。這些自建庫的特點是，他們的頁面看起來很讀秀，但沒有「包庫全文」這類按鈕，不過仍然可以通過一些手段在超星中打開，進而獲得淸晰版。
以西安理工爲代表的，登入 VPN 後，在資源統一平臺或讀秀搜到書後點擊卽可找到眞實地址，下載需要全程使用 VPN 。
又如以寧波大學園區爲例，衹要自建庫內有，並且知道 ss 號，卽可獲得返回鏈。把返回鏈 decode 之後，替換 rd 値，卽可使用超星打開。之後的操作與一般淸晰版相同。
還有以貴州大學爲代表的，不用管 rd 値，但需要處理 IP ，下載需要全程使用 VPN 。由於文件的擴展名是 jpg 和 png 混合，無法使用 CxCandy ，於是我就寫了 Python 腳本來下載。
自建庫的淸晰版經常是發白的，但附屬頁也是淸晰版。

## 諮詢
沒有淸晰版下載時，就需要諮詢。點擊「圖書館文獻傳遞」，輸入郵箱、頁碼、驗證碼，就會在郵箱收到諮詢鏈接。
單個機構衹能諮詢到一小半，所以需要三個機構。現在讀秀的規定是一個星期內衹能諮詢一本書的 80% 。

## 下載 PDF
PDF 的下載沒什麼好說的，試讀頁和諮詢頁都有，直接點擊下載。

## 下載大圖
記住：這是退而求次的無奈選擇。
對於有「包庫全文」的書，還是比較容易換成大圖的。就是在點了「包庫全文」後進入的鏈接，把鏈接複製到專用工具裡，就行了。不過幾乎所有書籍都可以獲得大圖。方法就是，進入要下載的書籍的專頁後，點「圖書館文獻傳遞」，按要求輸入，然後郵箱會收到諮詢鏈接，處理方式同全文。諮詢有限制，需要多找幾個機構帳接力。
讀秀經常調整，能使用的工具總是變來變去，但萬變不離其宗，特別是如果僅需要大圖補版權頁、封面頁，在瀏覽器收藏夾加上這一段，然後在試讀頁點擊就可以顯示出來了。
讀秀經常調整，會造成很多工具失效，不過用 PycURL 配合 MD 則非常輕鬆，改版衹需非常細微的調節。

## 超星及讀秀體系書籍的特點
超星書籍下載下來，一般是「書名_ssid」這樣的一個文件夾，裏面有很多文件。這個 ssid 是一個八位數字，疑似從 10000001 開始，根據超星掃描的順序一個接着一個，所以看最新 ssid 的數値就能估計超星書籍的總量。但是，有事 ssid 會以 8 開頭——通常是套裝書。對於 8 開頭的書，如果使用 CxCandy 截獲同一套書中任意一本的報文，就能下載其餘。
文件夾內，有一個 BookInfo.dat 代表書籍信息，比如書名、作者、出版年份、出版社等，還可能有一個 BookContents.dat 是目錄文件。而書籍圖像文件，一律是六位的，擴展名爲 pdg 。其中，封面是形如 cov001.pdg 這樣的，書名頁形如 bok001.pdg ，前言形如 fow001.pdg ，目錄形如 !00001.pdg ，正文形如 000001.pdg ，附錄形如 att001.pdg ，封底形如 bac001.pdg 。

## 機構
每個機構出的錢不同，讀秀給予的權限也不同。有的讀秀帳號根本不能直接讀全文，這就要看他的超星的具體情況。
高檔機構包括但不限於同濟、華東理工、復旦、上交、華東師大、上海外國語、上海大學、上海師大、礦大、陝西師大、內蒙科大、北大、北大醫學部、清華、南開、江西財大、中南財經政法、大醫、北航、北理珠海、楡林學院、景德鎭陶瓷學院、浙江工業、寧波大學園區、貴州大學、西安理工、東北財經、江蘇師範、鄭州大學、安徽建築、廈門大學、長江師範、淮陰師範、延安幹部。
由於全庫實在太貴，各機構不可能買完，而且超星對各機構上架書籍的更新時間不一，就出現了「江山代有機構出，各領風騷一兩年」的現象。
比如，當年同濟、北理珠海、礦大、復旦、華東師範、上海大學等校均以書多聞名，奠定了現在網上超星 ss 號在 125 段之前的書籍基礎。
一段時間後，有人發現陝西師大與同濟等滬系高校有極高的互補性，書也較新，在 126-128 段的非常多。
後來江西財大異軍突起，接過 2012-2013 年度新書的棒子，包庫領跑 128-130 段。
2013 年後半段，自建庫的下載手段漸漸傳入千萬家，所以又出現了很多原來下載不到的書，號碼段分佈較散，但總體來講新號比舊號多。於是，擁有寧波大學園區和浙江工業的帳號炙手可熱。
2014 年又殺出華東理工這個程咬金，書又多又新，號稱 180 萬，幾乎覆蓋所有滬系學校的包庫，新書多，還不斷有上架。年末西安理工浮出水面，以編程等理工書籍爲特色，補充了很多以前下載不到的書。
2015 年貴州大學忽然大灑銀子，不分文理的上架了大量書籍，配合寧波園區和華東理工能下載到 95% 以上的漢學書籍。
一本書的下載地址，可以通過一下這段代碼找到。但可能獲取到的機構是「鏡像全文」的快速版。

## 後期處理
超星有的書，掃描質量不好恭維，發白、發暗、有麻點，怎麼辦？
最常見的辦法：先用 Pdg2Pic 轉成圖片，再用 ComicEnhancerPro 批量處理圖片，最後重命名爲 pdg ，或者用其他工具加密成 pdg 。現在 ComicEnhancerPro 可以自動糾斜和裁邊，挺好用了。
最懶的辦法： MagicBeauty 直接處理。
最好的辦法：別動，用高版本 UnicornViewer 開，並用他的圖像處理功能處理。
還有人對轉換成 pdf 情有獨鐘。用 Pdg2Pic 即可。

隨口扯一句非讀秀/超星的電子書，因爲這些書才是不規範、需要修正的。
首先是 Google Books 。如果你下載的是英文書，那沒大問題，但中文古籍卻經常「倒裝」——洋人往往不知道我天朝的傳統書籍跟他們是倒過來的。簡單， PDFPatcher 就可以。 PDFPatcher 還可以用於 PDF 拆頁，但是 Google 很不厚道的把一些頁面挖下幾個字再補上去，如果你拆頁成圖片，這些補丁就回不去了……
然後是網友自掃的書籍。一般來說，用 ComicEnhancerPro 就能收到比較好的效果，但對於一些比較變態的，就要用點特殊手段。PDF 倒是有海德堡插件和其他小軟件可以分頁，不過多數是假分頁，即，如果你真正導出圖片時，這些圖片還是沒分頁的。這時候用 ImageMagick 這個命令行操作的神軟更好。自掃經常碰上彩色的，非常佔空間，可以用 ComicEnhancerPro 或 ImageMagick 處理成單色。但有的掃描時書溝比較深，直接單色處理會使得靠近書溝的部分變成黑色的，還有如果用比較深色的筆做筆記，有時會蓋住字，單色的直接一團黑了。因此可能需要處理成灰度圖像，或者通過調整伽馬值、高亮、對比度、曲線等等多方面來達到滿意的效果。

### ImageMagick 實戰舉例
大圖批量去水印而不改變其他部分（原理是利用水印的顏色去除）：
mogrify -path newdir -fill white -opaque "rgb(238,238,238)" -colors 16 *.png
批量將其他格式轉爲最緊湊的 tif ：
mogrify -path newdir -compress group4 -format tif *.jpg
批量去白邊：
mogrify -path newdir -trim +repage *.tif
批量對半切開，切好的文件自動命名爲超星標準的六位數：
convert *.tif -crop 50%x100% +repage %06d.tif
批量對半切開並去白邊，但切開時左右都是 52% ，且各放一個文件夾：
mogrify -path a -gravity northwest -crop 52%x100% -trim +repage *.tif
mogrify -path b -gravity northeast -crop 52%x100% -trim +repage *.tif
批量放大一倍：
mogrify -path newdir -resize 200% *.jpg
批量轉 90 度：
mogrify -path newdir -rotate -90 *.png
批量傾斜校正（可能造成鋸齒化和體積增加）：
mogrify -path newdir -background white -deskew 40% *.tif
以上都是簡單命令，還可以結合 CMD 設置複雜化的命令。

## 隨手記
*sslibrary.com 的頁面中，所有書籍都是通過點擊一個形如 javascript:readbook('showbook.do?dxNumber=12216071&d=7A09A5D8BF97916219FDE690CBBE0044&fenleiID=0B202030&username=shfddx'); 的鏈接來激活超星閱讀器看 pdg 的。其中， readbook 函數則是在一個 JavaScript 中寫成的 http://edu.sslibrary.com/sslibrary1.5/js/readbook.js ， dxNumber=12216071&d=7A09A5D8BF97916219FDE690CBBE0044&fenleiID=0B202030 部分則和讀秀的鏈接重合。在 consol 批量取 book 鏈的腳本呼之欲出了。


## 結論
一、要下就下清晰或印前 pdg
二、下載漢學書籍必備華東理工、寧波園區、貴州大學這三大機構，高檔機構多多益善
三、清晰 pdg 需要超星、棒棒糖協作下載，然後用 UnicornViewer 閱讀
四、自己下不到，就去求書
五、求書帖沒人搭理，再下大圖
六、叢書儘量別自己慢慢下
七、下載回來的東西儘量不做有損處理，以免他日後悔，要麼就備份後再處理