import tkinter as tk
from tkinter import messagebox
import random

SCAMS = [
    {
        'scenario': 'คุณได้รับข้อความจากเพจ Facebook ปลอม อ้างว่าได้รับรางวัลใหญ่ และขอให้คลิกลิงก์เพื่อยืนยันตัวตน',
        'answer': 'ระวัง',
        'explanation': 'อย่าคลิกลิงก์หรือให้ข้อมูลส่วนตัวกับเพจที่ไม่น่าเชื่อถือ'
    },
    {
        'scenario': 'มีเว็บไซต์โฆษณาลงทุนหุ้นผลตอบแทนสูงเกินจริง พร้อมรีวิวปลอม',
        'answer': 'ระวัง',
        'explanation': 'เว็บไซต์ลงทุนที่ให้ผลตอบแทนสูงผิดปกติ มักเป็นกลโกงหลอกลวง'
    },
    {
        'scenario': 'คุณได้รับข้อความจากร้านค้าออนไลน์ที่ไม่รู้จัก เสนอขายสินค้าราคาถูกมาก',
        'answer': 'ระวัง',
        'explanation': 'ร้านค้าที่ไม่รู้จักและราคาถูกผิดปกติ อาจเป็นมิจฉาชีพหลอกขายของปลอม'
    },
    {
        'scenario': 'มี SMS แจ้งว่าคุณมีพัสดุตกค้าง ให้คลิกลิงก์เพื่อตรวจสอบ',
        'answer': 'ระวัง',
        'explanation': 'SMS ปลอมมักหลอกให้คลิกลิงก์เพื่อขโมยข้อมูลหรือเงิน'
    },
    {
        'scenario': 'เว็บไซต์ธนาคารปลอมที่หน้าตาคล้ายของจริง ส่งลิงก์มาทางอีเมล',
        'answer': 'ระวัง',
        'explanation': 'ควรเข้าธนาคารผ่านแอปหรือเว็บไซต์ทางการเท่านั้น'
    },
    {
        'scenario': 'เพื่อนใน LINE ขอให้โอนเงินด่วน โดยอ้างว่ากำลังเดือดร้อน',
        'answer': 'ระวัง',
        'explanation': 'ควรโทรสอบถามเพื่อนก่อนโอนเงิน เพราะอาจถูกแฮกบัญชี'
    },
]

class ScamAwarenessGame:
    def __init__(self, master):
        self.master = master
        master.title('เกมรู้เท่าทันมิจฉาชีพออนไลน์')
        self.score = 0
        self.round = 0
        self.max_rounds = 5
        self.label = tk.Label(master, text='', font=('TH SarabunPSK', 18), wraplength=400)
        self.label.pack(pady=20)
        self.safe_btn = tk.Button(master, text='ปลอดภัย', command=lambda: self.check_answer('ปลอดภัย'), font=('TH SarabunPSK', 16))
        self.safe_btn.pack(side='left', padx=40, pady=20)
        self.careful_btn = tk.Button(master, text='ระวัง', command=lambda: self.check_answer('ระวัง'), font=('TH SarabunPSK', 16))
        self.careful_btn.pack(side='right', padx=40, pady=20)
        self.next_scenario()

    def next_scenario(self):
        if self.round >= self.max_rounds:
            self.end_game()
            return
        self.current = random.choice(SCAMS)
        self.label.config(text=f'สถานการณ์ที่ {self.round+1}\n\n{self.current["scenario"]}')

    def check_answer(self, answer):
        if answer == self.current['answer']:
            self.score += 1
            messagebox.showinfo('ถูกต้อง', f'เยี่ยมมาก! {self.current["explanation"]}')
        else:
            messagebox.showwarning('ผิดพลาด', f'ควรระวัง! {self.current["explanation"]}')
        self.round += 1
        self.next_scenario()

    def end_game(self):
        percent = (self.score / self.max_rounds) * 100
        msg = (
            f'จบเกม!\n'
            f'คุณตอบถูก {self.score} จาก {self.max_rounds} สถานการณ์\n'
            f'คิดเป็น {percent:.0f}% ของคะแนนเต็ม\n'
            'ขอบคุณที่ร่วมเรียนการรู้เท่าทันมิจฉาชีพออนไลน์'
        )
        messagebox.showinfo('สรุปผล', msg)
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    game = ScamAwarenessGame(root)
    root.mainloop()
