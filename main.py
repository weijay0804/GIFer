'''
Author: weijay
Date: 2023-03-04 17:33:27
LastEditors: weijay
LastEditTime: 2023-03-04 22:34:39
Description: jpg to gif GUI
'''

import wx
from convert import convert_to_gif

class ToGIF(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, None, title = "Image To GIF", size = (400, 350))

        # 建立開啟檔案按鈕
        self.open_file_btn = wx.Button(self, label = "選擇檔案", size = (100, -1))
        self.open_file_btn.Bind(wx.EVT_BUTTON, self.onOpenFile)

        # 建立清除選取按鈕
        self.delete_file_btn = wx.Button(self, label = "清除檔案", size = (100, -1))
        self.delete_file_btn.Bind(wx.EVT_BUTTON, self.onClearFile)

        # 建立顯示選取的檔案 Box
        self.list_box = wx.ListBox(self, style=wx.LB_SINGLE)

        # 建立調整速度輸入區塊
        speed_text = wx.StaticText(self, -1, label = "設定播放速度 (s)")

        self.speed_text_ctrl = wx.TextCtrl(self, size = (150, 20))
        self.speed_text_ctrl.Value = "2"

        speed_block = wx.BoxSizer(wx.VERTICAL)
        speed_block.Add(speed_text, 0, wx.BOTTOM, 10)
        speed_block.Add(self.speed_text_ctrl, 0)

        self.speed_block = speed_block

        # 建立儲存位置按鈕
        self.save_file_btn = wx.Button(self, label = "選擇儲存位置", size = (100, -1))
        self.save_file_btn.Bind(wx.EVT_BUTTON, self.onSaveFile)

        # 建立執行按鈕
        self.run_btn = wx.Button(self, label = "執行", size = (100, -1))
        self.run_btn.Bind(wx.EVT_BUTTON, self.onRun)


        run_block = wx.BoxSizer(wx.HORIZONTAL)
        run_block.Add(self.save_file_btn, 0, wx.ALL, 10)
        run_block.Add(self.run_btn, 0, wx.ALL, 10)

        self.run_block = run_block

        self.save_path = None

        self._set_layout()

    def _set_layout(self):
        """ 設定佈局 """

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.open_file_btn, 0,  wx.ALL, 10)
        hbox.Add(self.delete_file_btn, 0, wx.ALL, 10)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, 0)
        vbox.Add(self.list_box, 1, wx.EXPAND|wx.ALL, 10)
        vbox.Add(self.speed_block, 0, wx.ALL, 10)
        vbox.Add(self.run_block, 0, wx.UP|wx.BOTTOM, 10)

        self.SetSizer(vbox)


    def onOpenFile(self, evnet):
        """ 開啟檔案動作 """

        dlg = wx.FileDialog(
            self, message = "選擇一個或多個檔案", defaultDir="", wildcard="Image files (*.jpg;*.png)|*.jpg;*.png",
            style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST|wx.FD_MULTIPLE|wx.FD_CHANGE_DIR
        )

        if dlg.ShowModal() == wx.ID_OK:
            # 將選擇的檔案加入 ListBox
            paths = dlg.GetPaths()
            for path in paths:
                if path not in self.list_box.GetItems():
                    self.list_box.Append(path)
        dlg.Destroy()

    def onClearFile(self, event):
        """ 清除檔案動作 """
        
        self.list_box.Clear()

    def onSaveFile(self, event):
        """ 儲存檔案動作 """

        dlg = wx.FileDialog(
            self, message = "選擇儲存位置",
            style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT|wx.FD_CHANGE_DIR
        )

        dlg.SetFilename("test.gif")

        if dlg.ShowModal() == wx.ID_OK:

            path = dlg.GetPath()

            self.save_path = path

        dlg.Destroy()

    def onRun(self, evnet):
        """ 執行轉換動作 """

        input_files = self.list_box.GetItems()

        if not input_files:
            wx.MessageBox("請至少選擇一個檔案")
            return
        
        save_path = self.save_path

        if not save_path:
            wx.MessageBox("請選擇儲存位置")
            return
        
        speed = self.speed_text_ctrl.Value

        try:
            speed = int(speed)

        except Exception as e:
            wx.MessageBox("請輸入數字")
            return

        busy = wx.BusyInfo("Processing data, please wait...")
        wx.BeginBusyCursor()
        convert_to_gif(input_files, save_path, speed = speed)
        wx.EndBusyCursor()
        del busy

        wx.MessageBox("轉換完成")

if __name__ == "__main__":

    app = wx.App()
    frame = ToGIF()
    frame.Show()
    app.MainLoop()
