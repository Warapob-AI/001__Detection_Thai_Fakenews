from pythainlp.corpus import thai_stopwords, thai_words
from pythainlp.tokenize import Tokenizer
from pythainlp.util import dict_trie

custom_words_list = set(thai_words())
custom_words_list.update([
    'รัฐมนตรีว่าการ', 'สำนักงานกองทุนสนับสนุนการสร้างเสริมสุขภาพ', 'ตำรวจไซเบอร์',
    'ไม้มิสวาก', 'ไม่มี', 'สำนักงานคณะกรรมการกำกับหลักทรัพย์และตลาดหลักทรัพย์',
    'คอล', 'ผู้บัญชาการไซเบอร์', 'ของฟรีไม่มีในโลก', 'ล้านบาท', 'ทุบสถิติ',
    'ไม่ให้', 'แสนราย', 'พันล้าน', 'กาซ่า', 'กองทุนการออมแห่งชาติ', 'ต้องการ',
    'แรงงาน', 'จูราสสิคเวิลด์', 'ไม่ใช่', 'จู่โจม', 'กรมสวัสดิการและคุ้มครองแรงงาน',
    'กรมควบคุมโรค', 'อนามัย', 'บุหรี่ไฟฟ้า', 'องค์กรพลังงาน', 'แล้ว', 'คริป',
    'คริปโต', 'กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์', 'อันตราย', 'องค์การค้า',
    'คริสไรท์', 'ไม่น่า', 'รูบิโอ', 'เนทันยาฮู', 'สีจิ้นผิง', 'ทรีนิตี้',
    'เฟนทานิล', 'อ่าว', 'กวนตานาโม', 'กล้าธรรม', 'เซเลนสกี', 'ดีอี', 'ออนแทรีโอ',
    'สมศักดิ์', 'อิชิบะ', 'บิ๊กอ้วน', 'บูลลี่', 'ผู้บัญชาการทหารสูงสุด', 'ขึ้น',
    'ราชกรมทัณฑ์', 'รายงาน', 'สํานักงานคณะกรรมการอาหารและยา',
    'คณะกรรมการกิจการกระจายเสียงกิจการโทรทัศน์และกิจการโทรคมนาคมแห่งชาติ', 'ชูรูป'
])

trie = dict_trie(dict_source=custom_words_list)
_tokenizer = Tokenizer(custom_dict=trie, engine='newmm')

def Tokenization(text):
    tokens = _tokenizer.word_tokenize(text)
    return " ".join(tokens)
