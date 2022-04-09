# -*- coding: utf-8 -*-

import platform
from kivy.app import App
makineadi1=platform.machine()
makine_versionu=platform.version()
makine_platform=platform.platform()
makine_adi=platform.uname()
makine_system=platform.system()
makine_islemci=platform.processor()
class olayUyg(App):
    def build(self):
        self.root.ids.mesaj1.text='makine info: {} !'.format(makineadi1)
        self.root.ids.mesaj2.text='makine versionu: {} !'.format(makine_versionu)
        self.root.ids.mesaj3.text='makine platform: {} !'.format(makine_platform)
        self.root.ids.mesaj4.text='makine adı: {} !'.format(makine_adi)
        self.root.ids.mesaj5.text='makine system: {} !'.format(makine_system)
        self.root.ids.mesaj6.text='makine işlemci: {} !'.format(makine_islemci)
    def sifredogrula(self):
        kulladi1 = self.root.ids.kulladi.text
        kullsifre1=self.root.ids.kullsifre.text
        if kulladi1=="DexmoD" and kullsifre1=="DexmoD":
            self.root.ids.mesaj.text='Merhaba {} !'.format(kulladi1)
        else:
            self.root.ids.mesaj.text='Kullanıcı adı veya Kullanıcı Şifresi Hatalı'
        

olayUyg().run()

