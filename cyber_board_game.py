import tkinter as tk
from tkinter import messagebox
import random

# สถานการณ์ตัวอย่าง
SCENARIOS = [
    {
        'event': 'มีอีเมลน่าสงสัยส่งถึงผู้บริหาร พร้อมไฟล์แนบ',
        'risk': 'หากไม่ลงทุน อาจติดมัลแวร์และข้อมูลรั่วไหล',
        'cost': 20000,
        'damage': 100000
    },
    {
        'event': 'พบช่องโหว่ในระบบบัญชี',
        'risk': 'หากไม่ลงทุน อาจถูกแฮกเกอร์ขโมยข้อมูลการเงิน',
        'cost': 30000,
        'damage': 150000
    },
    {
        'event': 'ได้รับแจ้งเตือนจากหน่วยงานรัฐเรื่องภัยไซเบอร์',
        'risk': 'หากไม่ลงทุน อาจถูกปรับและเสียชื่อเสียง',
        'cost': 15000,
        'damage': 80000
    },
    {
        'event': 'มีไวรัสเรียกค่าไถ่โจมตีองค์กรอื่นในวงการเดียวกัน',
        'risk': 'หากไม่ลงทุน อาจถูกโจมตีและต้องจ่ายค่าไถ่',
        'cost': 25000,
        'damage': 120000
    },
]

class CyberBoardGame:
    def __init__(self, master):
        self.master = master
        master.title('เกมตัดสินใจลงทุนความมั่นคงไซเบอร์')
        self.budget = 100000
        self.round = 0
        self.max_rounds = 5
        self.label = tk.Label(master, text='', font=('TH SarabunPSK', 18))
        self.label.pack(pady=20)
        self.invest_btn = tk.Button(master, text='ลงทุน', command=self.invest, font=('TH SarabunPSK', 16))
        self.invest_btn.pack(side='left', padx=40, pady=20)
        self.skip_btn = tk.Button(master, text='ไม่ลงทุน', command=self.skip, font=('TH SarabunPSK', 16))
        self.skip_btn.pack(side='right', padx=40, pady=20)
        self.next_scenario()

    def next_scenario(self):
        if self.round >= self.max_rounds or self.budget <= 0:
            self.end_game()
            return
        self.current = random.choice(SCENARIOS)
        self.label.config(text=f'รอบที่ {self.round+1}\nงบประมาณคงเหลือ: {self.budget:,} บาท\n\nสถานการณ์: {self.current["event"]}')

    def invest(self):
        self.budget -= self.current['cost']
        messagebox.showinfo('ผลลัพธ์', f'คุณเลือกลงทุน ({self.current["cost"]:,} บาท)\nลดความเสี่ยง: {self.current["risk"]}')
        self.round += 1
        self.next_scenario()

    def skip(self):
        if random.random() < 0.7:
            self.budget -= self.current['damage']
            messagebox.showwarning('เกิดความเสียหาย', f'คุณไม่ลงทุน\n{self.current["risk"]}\nความเสียหาย: {self.current["damage"]:,} บาท')
        else:
            messagebox.showinfo('รอดปลอดภัย', 'รอบนี้ไม่มีเหตุการณ์ร้ายแรงเกิดขึ้น')
        self.round += 1
        self.next_scenario()

    def end_game(self):
        msg = f'จบเกม!\nงบประมาณคงเหลือ: {self.budget:,} บาท\nขอบคุณที่ร่วมเรียนรู้ความมั่นคงไซเบอร์'
        messagebox.showinfo('สรุปผล', msg)
        self.master.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    game = CyberBoardGame(root)
    root.mainloop()
