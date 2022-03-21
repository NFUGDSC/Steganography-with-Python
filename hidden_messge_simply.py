# 檔案頭資料塊IHDR（header chunk）：包含有圖像基本資訊，作為第一個資料塊出現並只出現一次。
# 調色盤資料塊PLTE（palette chunk）：必須放在圖像資料塊之前。
# 圖像資料塊IDAT（image data chunk）：儲存實際圖像資料。PNG資料允許包含多個連續的圖像資料塊。
# 圖像結束資料IEND（image trailer chunk）：放在檔案尾部，表示PNG資料流結束。

# ihdr=89 50 4E 47 0D 0A 1A 0A
# iend=49 45 4E 44 AE 42 60 82

end_hex = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
def hiddenmessage(str):
    with open('gurapng.png','ab') as f:
        f.write(str)

def getmessage():
    with open('gurapng.png','rb') as f:
        content=f.read()
        offset=content.index(end_hex)
        f.seek(offset+len(end_hex))
        print(f.read())

getmessage()